import pandas as pd
from scipy import stats
import argparse

# Function to perform ANOVA
def perform_anova(data):
    conditions = data['condition'].unique()
    groups = [data[data['condition'] == cond]['biomass'] for cond in conditions]
    
    anova_result = stats.f_oneway(*groups)
    
    print(f"ANOVA result: F-statistic = {anova_result.statistic}, p-value = {anova_result.pvalue}")
    
    if anova_result.pvalue < 0.05:
        print("There are significant differences between the conditions.")
    else:
        print("No significant differences were found between the conditions.")

def main(input_file):
    data = pd.read_csv(input_file)
    
    if 'condition' not in data.columns or 'biomass' not in data.columns:
        raise ValueError("Input file must contain 'condition' and 'biomass' columns")
    
    perform_anova(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Perform ANOVA statistical analysis on biomass data.')
    parser.add_argument('--input', type=str, required=True, help='Path to input CSV file containing biomass data.')
    
    args = parser.parse_args()
    main(args.input)