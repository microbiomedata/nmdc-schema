import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the file paths and sheet name
heatmap_file_path = "~/ncbi_attributes_all_long_non_attribute_metadata_202405231341.xlsx"
heatmap_sheet_name = "ncbi_attributes_all_long_non_at"
package_usage_file_path = "~/Downloads/2024-02-26-package-usage.tsv"

# Load the heatmap data from the Excel sheet into a DataFrame
heatmap_df = pd.read_excel(heatmap_file_path, sheet_name=heatmap_sheet_name)

# Option to remove rows with NaN in harmonized_name
remove_nan_harmonized_name = True

if remove_nan_harmonized_name:
    heatmap_df = heatmap_df.dropna(subset=['harmonized_name'])

# Option to filter packages based on substrings
filter_packages = True
package_substrings = [
    '1.0',
    'MIMS',
    'gut',
    'soil',
]

if filter_packages:
    pattern = '|'.join(package_substrings)
    heatmap_df = heatmap_df[heatmap_df['package'].str.contains(pattern, na=False)]

# Load the package usage data from the TSV file into a DataFrame
package_usage_df = pd.read_csv(package_usage_file_path, delimiter='\t')

# Filter package usage data to match the filtered heatmap_df
package_usage_df = package_usage_df[package_usage_df['package'].isin(heatmap_df['package'].unique())]

# Pivot the heatmap DataFrame to have packages as rows and harmonized_name as columns
heatmap_data = heatmap_df.pivot(index='package', columns='harmonized_name', values='count')

# Normalize the heatmap data by the biosamples per package counts
package_usage_df.set_index('package', inplace=True)
normalized_data = heatmap_data.div(package_usage_df['count'], axis=0)

# Define a threshold for the maximum percentage of zero or NA values allowed
threshold_percentage = 0.80

# Calculate the percentage of zero or NA values in each column
zero_or_na_percentage = (normalized_data.isna() | (normalized_data == 0)).mean()

# Filter out columns that exceed the threshold
filtered_data = normalized_data.loc[:, zero_or_na_percentage <= threshold_percentage]

# Set up the matplotlib figure
plt.figure(figsize=(50, 20))  # Adjust the figure size as needed

# Create the heatmap without the legend
sns.heatmap(filtered_data, cmap='Reds', cbar=True, linewidths=.5)

# Set the title and labels
plt.title('Normalized Annotations per Package and Harmonized Attribute (Filtered)')
plt.xlabel('Harmonized Name')
plt.ylabel('Package')

# Ensure all x-axis labels are shown
ax = plt.gca()
ax.set_xticks(range(len(filtered_data.columns)))
ax.set_xticklabels(filtered_data.columns, rotation=90, fontsize=10)

# Adjust the layout to make room for the labels and minimize whitespace
plt.tight_layout(rect=[0, 0, 1, 1])  # Adjust the rectangle parameters as needed

# Save the figure to a file (e.g., PNG) for use in PowerPoint
# plt.savefig('../../heatmap_annotations_enhanced.png', dpi=300)

# Optionally, save the plot as a PDF file
plt.savefig('../../heatmap_annotations_enhanced.pdf', format='pdf', dpi=300)


# Optionally, save the plot as a PDF file
plt.savefig('../../heatmap_annotations_enhanced.png', format='png', dpi=300)

# # Show the plot
# plt.show()
