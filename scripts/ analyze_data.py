import pandas as pd
import argparse

# Function to calculate the Resiliency Score (RS)
def calculate_resiliency_score(row):
    B_n = row['normal_biomass']
    B_a = row['adverse_biomass']
    
    if B_n == 0:
        return 0
    return max(0, min(10, 10 * (B_a / B_n)))

def main(input_file, output_file):
    # Load the data
    data = pd.read_csv(input_file)
    
    if 'normal_biomass' not in data.columns or 'adverse_biomass' not in data.columns:
        raise ValueError("Input file must contain 'normal_biomass' and 'adverse_biomass' columns")
    
    # Calculate Resiliency Score for each plant
    data['resiliency_score'] = data.apply(calculate_resiliency_score, axis=1)
    
    data.to_csv(output_file, index=False)
    print(f"Resiliency Scores calculated and saved to {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate Resiliency Score from biomass data.')
    parser.add_argument('--input', type=str, required=True, help='Path to input CSV file containing biomass data.')
    parser.add_argument('--output', type=str, required=True, help='Path to output CSV file to save results.')
    
    args = parser.parse_args()
    main(args.input, args.output)