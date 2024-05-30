import pandas as pd
import matplotlib.pyplot as plt

# Read the data into a pandas DataFrame
df = pd.read_csv('~/non_attribute_metadata_202405231646.csv', delimiter="\t")  # Update the path as needed

# Convert the status_date column to datetime
df['status_date'] = pd.to_datetime(df['status_date'], format='ISO8601')
df['month'] = df['status_date'].dt.to_period('M')

# Specify the packages you want to include
selected_packages = [
    'Generic.1.0',
    'MIMS.me.human-gut.6.0',
    'MIMS.me.soil.6.0',
    'SARS-CoV-2.cl.1.0',
]

# Filter the DataFrame to include only the selected packages
filtered_df = df[df['package'].isin(selected_packages)]

# Group the data by package and month, counting the number of observations
package_counts = filtered_df.groupby(['package', 'month']).size().reset_index(name='count')

# Pivot the data to create a DataFrame with packages as columns and months as rows
package_counts_pivoted = package_counts.pivot(index='month', columns='package', values='count')

# Fill missing values with 0
package_counts_pivoted.fillna(0, inplace=True)

# Calculate the cumulative sum for each package
cumulative_counts = package_counts_pivoted.cumsum()

# Plot the data as a line plot
fig, ax = plt.subplots(figsize=(12, 8))
cumulative_counts.plot(ax=ax, linewidth=3)

# Set the plot title and labels
ax.set_title('Cumulative Number of Biosamples by Selected Packages over Time')
ax.set_xlabel('Year')
ax.set_ylabel('Cumulative Number of Biosamples')

# Enable a log scale for the y-axis if needed
ax.set_yscale('log')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Add a legend inside the plot in the upper left corner
ax.legend(title='Package', loc='upper left')

# Adjust the layout to prevent the legend from being cut off
plt.tight_layout()

# Display the plot
plt.show()

# Save the plot as an image file if needed
# plt.savefig('cumulative_counts.png', dpi=300)

# Save the plot as a PDF file if needed
# plt.savefig('cumulative_counts.pdf', format='pdf')

# Save cumulative_counts as a tsv file
cumulative_counts.to_csv('cumulative_counts.tsv', sep='\t')
