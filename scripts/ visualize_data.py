import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def main(input_file):
    # Load the data
    data = pd.read_csv(input_file)
    
    if 'condition' not in data.columns or 'biomass' not in data.columns:
        raise ValueError("Input file must contain 'condition' and 'biomass' columns")
    
    # Plot biomass distribution
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='condition', y='biomass', data=data)
    plt.title('Biomass Distribution Across Conditions')
    plt.xlabel('Condition')
    plt.ylabel('Biomass (g)')
    plt.show()

    # If Resiliency Scores are available, plot those as well
    if 'resiliency_score' in data.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(data['resiliency_score'], kde=True, bins=10)
        plt.title('Distribution of Resiliency Scores')
        plt.xlabel('Resiliency Score')
        plt.ylabel('Frequency')
        plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Visualize biomass and Resiliency Score data.')
    parser.add_argument('--input', type=str, required=True, help='Path to input CSV file containing biomass data.')
    
    args = parser.parse_args()
    main(args.input)