import pandas as pd


def sample_tsv(input_file: str, output_file: str, sample_percentage: float):
    # Read the TSV file into a DataFrame
    df = pd.read_csv(input_file, sep='\t')

    # Calculate the number of samples
    sample_size = int(len(df) * sample_percentage / 100)

    # Randomly sample the specified percentage of rows
    sampled_df = df.sample(n=sample_size)

    # Save the sampled DataFrame to a new TSV file
    sampled_df.to_csv(output_file, sep='\t', index=False)


# Specify the input and output file paths and the sample percentage
input_file = '~/export_202405282209.csv'
output_file = 'output_file.tsv'
sample_percentage = 0.1  # For example, 10% of the rows

# Call the function
sample_tsv(input_file, output_file, sample_percentage)
