# Scripts for Resiliency Analysis

This folder contains Python scripts used for analyzing plant resiliency data, calculating Resiliency Scores, performing statistical analysis, and generating visualizations. These scripts automate key tasks, making it easier for researchers to work with experimental data.

## Scripts Overview

### 1. analyze_data.py

This script calculates the Resiliency Score for each plant based on its biomass under normal and adverse conditions. The results are saved to a CSV file.

•	**Inputs:**

•	normal_biomass: Column containing biomass data for plants grown under normal conditions.

•	adverse_biomass: Column containing biomass data for plants grown under adverse conditions.

•	**Outputs:**

•   A new CSV file with a Resiliency Score for each plant, scaled between 0-10.

## 2. visualize_data.py
This script generates visualizations, such as box plots and histograms, to help researchers understand the distribution of biomass across conditions and visualize the Resiliency Scores.


## 3. statistical_analysis.py
This script performs ANOVA (Analysis of Variance) to determine if there are statistically significant differences in biomass between different conditions.



## Installation Instructions

Before running these scripts, ensure the required Python packages are installed. Use the provided requirements.txt file to install them:

```bash
pip install -r ../requirements.txt
```



