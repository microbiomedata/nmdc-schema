import pandas as pd

# Set pandas options to display all columns
pd.set_option('display.max_columns', None)

# Filepath for the input Excel file and the correct sheet name
input_excel_path = 'MIMS.me.soil.6.0-optionals-filtered-1-pct.xlsx'
sheet_name = 'MIMS.me.soil.6.0-optionals-filt'

# Read the hand-curated table from the specified sheet in the Excel file
curated_df = pd.read_excel(input_excel_path, sheet_name=sheet_name)
print(curated_df.shape)

# Filter out rows where 'ok' is 0
filtered_df = curated_df[curated_df['ok'] != 0]
print(filtered_df.shape)

# Extract unique accessions and harmonized names
all_accessions = curated_df['accession'].unique()
print(all_accessions.shape)
all_harmonized_names = curated_df['harmonized_name'].unique()
print(all_harmonized_names.shape)

# Create a complete DataFrame with all combinations of accessions and harmonized names
complete_df = pd.DataFrame(
    [(accession, harmonized_name) for accession in all_accessions for harmonized_name in all_harmonized_names],
    columns=['accession', 'harmonized_name'])
print(complete_df.shape)
print(complete_df.head(20))

# Merge the complete DataFrame with the filtered results to ensure all combinations are included
merged_df = complete_df.merge(filtered_df[['accession', 'harmonized_name', 'value']],
                              on=['accession', 'harmonized_name'], how='left')
print(merged_df.shape)
print(merged_df.head(20))

# Pivot the DataFrame to create the matrix
pivoted_df = merged_df.pivot_table(index='harmonized_name', columns='accession', values='value', aggfunc=lambda x: x,
                                   fill_value=pd.NA)
print(pivoted_df.shape)
# print(pivoted_df.head(20))

# Calculate sparsity
total_cells = pivoted_df.size
nan_cells = pivoted_df.isna().sum().sum()
sparsity = nan_cells / total_cells

print(f"Sparsity: {sparsity:.4f}")

# # Save the pivoted results to a TSV file
# pivoted_df.to_csv(f'{sheet_name}-pivot.tsv', sep='\t')

print("Pivoted results saved to file.")

# Additional information for debug/verification
print("\nFiltered DataFrame Shape:", filtered_df.shape)
print("Merged DataFrame Shape:", merged_df.shape)
print("Pivoted DataFrame Shape:", pivoted_df.shape)

# # Print the first few rows to verify the results
# print(merged_df.head())
# print(pivoted_df.head())
