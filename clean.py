import pandas as pd

# (1) merge the two input data files based on the ID of each respondent.
def clean(contact_df, other_df):
    contact_df = pd.read_csv(contact_df)
    other_df = pd.read_csv(other_df)
    merged_df = pd.merge(contact_df, other_df, left_on='respondent_id', right_on='id').drop('id', axis=1)

# (2) drop any rows with missing values.
    merged_df.dropna(inplace=True)

# (3) drop rows if the job value contains 'insurance' or 'Insurance'.
    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]

    return merged_df

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='Contact info file (CSV)')
    parser.add_argument('other_info_file', help='Other info file (CSV)')
    parser.add_argument('output_file', help='Cleaned data file (CSV)')
    args = parser.parse_args()

# (4) write the cleaned data to the file specified by the output_file argument.
    cleaned = clean(args.contact_info_file, args.other_info_file)
    cleaned.to_csv(args.output_file, index=False)