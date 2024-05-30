import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
import os
from joblib import Memory

# Parameters for the SQL query
package_value = 'MIMS.me.soil.6.0'
use_conditions = ['optional']  # Options: ['mandatory'], ['optional'], or ['mandatory', 'optional']

# Parameters for filtering
filter_mode = 'case_insensitive'  # Options: 'none', 'case_sensitive', 'case_insensitive'
match_type = 'startswith'  # Options: 'full', 'startswith'

additional_missing_indicators = [
    'NA']  # Add any additional missing indicators here like NA. They will only be checked verbatim

# Define missing indicators
insdc_missing_indicators = [
    'control sample',
    'data agreement established pre-2023',
    'endangered species',
    'human-identifiable',
    'lab stock',
    'missing',
    'not applicable',
    'not collected',
    'not provided',
    'restricted access',
    'sample group',
    'synthetic construct',
    'third party data',
]

# Database connection string
conn_string = "postgresql://biosample_guest:eatery5-upstart-hamper@localhost:15432/ncbi_biosamples_feb26"

# SQL query to fetch data
query_template = """
select
    distinct nam.accession, naal.harmonized_name, naal.value
from
    non_attribute_metadata nam
join ncbi_attributes_all_long naal on
    naal.raw_id = nam.raw_id
join ncbi_package_attribute_use npau on
    npau.package = nam.package
    and npau.attribute_harmonized_name = naal.harmonized_name
where
    nam.package = '{}'
    and ({})
;
"""

# Format the SQL query with parameters
use_conditions_str = ' or '.join(f"npau.use = '{condition}'" for condition in use_conditions)
query = query_template.format(package_value, use_conditions_str)

# Set up joblib cache
cache_dir = './cachedir'
memory = Memory(cache_dir, verbose=0)


@memory.cache
def query_database(query, conn_string):
    engine = create_engine(conn_string)
    try:
        return pd.read_sql(query, engine)
    finally:
        engine.dispose()


def print_edt_8601():
    """Print the current time in ISO 8601 format in Eastern Daylight Time (EDT)."""
    now_utc = datetime.now(pytz.utc)
    edt = pytz.timezone('US/Eastern')
    now_edt = now_utc.astimezone(edt)
    iso_timestamp = now_edt.isoformat()
    print(iso_timestamp)


def filter_results(df, filter_mode, match_type, additional_indicators):
    """Filter the DataFrame based on the given mode and match type."""
    if filter_mode == 'none':
        filtered_df = df
    else:
        if filter_mode == 'case_insensitive':
            df['value'] = df['value'].str.lower()
            indicators = [indicator.lower() for indicator in insdc_missing_indicators]
        else:
            indicators = insdc_missing_indicators

        if match_type == 'full':
            filtered_df = df[~df['value'].isin(indicators)]
        elif match_type == 'startswith':
            pattern = '|'.join(f'^{indicator}' for indicator in indicators)
            filtered_df = df[~df['value'].str.contains(pattern, regex=True)]

    # Always filter additional_missing_indicators verbatim
    filtered_df = filtered_df[~filtered_df['value'].isin(additional_indicators)]

    return filtered_df


def sample_accession(df, sample_fraction):
    """Sample a fraction of unique accession values and return the DataFrame containing all rows for those accessions."""
    unique_accessions = df['accession'].unique()
    sample_size = max(1, int(len(unique_accessions) * sample_fraction))
    sampled_accessions = pd.Series(unique_accessions).sample(sample_size, random_state=1).tolist()
    return df[df['accession'].isin(sampled_accessions)]


def main():
    try:
        print("Querying the database...")
        print_edt_8601()

        results = query_database(query, conn_string)
        print("Query complete")
        print_edt_8601()

        print(results)

    except Exception as error:
        print("Error:", error)
        return

    if results is not None:
        print("Writing the raw long results to a TSV file...")
        results.to_csv(f'{package_value}-mandatory.tsv', sep='\t')
        print("Results written to file")

        print(results.shape)
        print("Filtering out rows with missing indicators...")
        filtered_results = filter_results(results, filter_mode, match_type, additional_missing_indicators)
        print("Filtering complete")
        print(filtered_results.shape)

        print("Writing the filtered, subsetted results to a TSV file...")
        subset = sample_accession(filtered_results, 0.01)
        subset.to_csv(f'{package_value}-optionals-filtered-1-pct.tsv', sep='\t')
        print("Results written to file")

        # Drop the 'value' column and make results unique
        filtered_results = filtered_results.drop(columns='value').drop_duplicates()

        print("Pivoting the DataFrame...")
        pivoted_df = filtered_results.pivot_table(
            index='harmonized_name', columns='accession', values='harmonized_name',
            aggfunc=lambda x: 1, fill_value=float('nan')
        )
        print("Pivoting complete")

        print("Sorting on axis 0 and 1...")
        pivoted_df = pivoted_df.sort_index(axis=0).sort_index(axis=1)
        print("Sorting complete")

        print("Writing the pivoted results to a TSV file...")
        pivoted_df.to_csv(f'{package_value}-optionals-pivot.tsv', sep='\t')
        print("Results written to file")

        print("Calculating sparsity...")
        total_cells = pivoted_df.size
        nan_cells = pivoted_df.isna().sum().sum()
        sparsity = nan_cells / total_cells
        print(f"Sparsity: {sparsity:.4f}")

        # Print out query and filtering values used
        print("\nQuery and Filtering Parameters:")
        print(f"Package Value: {package_value}")
        print(f"Use Conditions: {use_conditions}")
        print(f"Filter Mode: {filter_mode}")
        print(f"Match Type: {match_type}")
        print(f"Additional Missing Indicators: {additional_missing_indicators}")


# heatmap_data = pivoted_df.fillna(0).replace(1, 1)
#
# # Create a figure and axes
# fig, ax = plt.subplots(figsize=(17, 10))
#
# # Display the heatmap
# im = ax.imshow(heatmap_data, cmap='binary', aspect='auto')
# # im = ax.imshow(heatmap_data, cmap='gray')
#
# # Remove the axis labels and ticks
# ax.set_xticks([])
# ax.set_yticks([])
# ax.axis('off')
#
# # Show the plot
# plt.tight_layout()
# plt.show()
#
# print(pivoted_df.columns)

if __name__ == "__main__":
    main()
