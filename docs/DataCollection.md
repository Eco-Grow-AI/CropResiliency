# EcoGrow AI: Resiliency Data Collection Methods and Research Conditions

This repository outlines the methodology used by EcoGrow AI to determine plant resilience under various climate conditions. The following steps describe the process for conducting controlled experiments to measure plant resiliency, along with data collection techniques and analysis methods.

## 1. Define Experimental Conditions

### Normal Conditions:
Define optimal growing conditions for the plant species in question. This may include:
- **Temperature:** 18-25°C
- **Soil moisture:** 50-60%
- **Light exposure:** 12-16 hours per day
- **Nutrients:** Standard recommended fertilizer levels
- **Humidity:** 60-80%

### Adverse Conditions:
These are the stress conditions to which plants will be exposed:
- **Drought:** Soil moisture reduced to 10-20%.
- **Waterlogging:** Soil kept saturated with excess water.
- **High Heat:** Sustained temperatures above 35°C.
- **Cold Stress:** Temperatures below 10°C.
- **Nutrient Deficiency:** Reduce key nutrients by 50%.
- **Low Light:** Reduced light exposure to 4-6 hours/day.

## 2. Conduct Experiments

### Control Group:
Grow plants under normal conditions as a baseline reference.

### Experimental Groups:
Grow plants under adverse conditions. Create groups for each stressor (drought, waterlogging, high heat, etc.). Ensure sufficient replication for reliable data.

## 3. Measure Biomass

At the end of the growing period, measure several factors to determine biomass:
- **Dry weight** of above-ground plant material (leaves, stems).
- **Dry weight** of roots.
- **Total leaf area** and **number of leaves**.

## 3.5 Collect Other Data
In addition to Biomass, ensure you collect a wide variety of agornomic features for each group and plant, this step is essential.

## 4. Calculate Resiliency Score

To quantify resiliency, normalize the biomass measurements on a 0-10 scale:
. Set Up Control Group (Normal Conditions):

  •	Plant one group in normal conditions (optimal temperature, moisture, light, nutrients).
  •	Measure the biomass of the plants in this group at the end of the growing period to establish a baseline. This will give you  B_n  (biomass under normal conditions).

2. Set Up Experimental Group (Adverse Conditions):

	•	Grow a separate group of plants in adverse conditions (e.g., drought, heat, poor soil, etc.).
	•	Allow these plants to grow fully under these adverse conditions and measure their biomass at the end of the experiment. This gives you  B_a  (biomass under adverse conditions).

3. Compare the Two Groups:

	•	Now, compare the biomass of the plants in the adverse group  B_a  to the biomass in the control group  B_n  to determine how much biomass was retained.
	•	The ratio (Ba / Bn) gives the percentage of biomass retained, which will be converted into a resiliency score.

## Resiliency Score Formula

The Resiliency Score (RS) is calculated based on the biomass retained under adverse conditions compared to normal conditions, using the following formula:

RS = max(0, min(10, 10 × (Ba / Bn)))

Where:
- Bn = Biomass under **normal conditions** (control group).
- Ba = Biomass under **adverse conditions** (experimental group).
- (Ba / Bn) is the ratio of biomass retained under adverse conditions to biomass under normal conditions.

### Example:
- For drought tolerance, if a plant under drought stress retains 80% of the biomass compared to the control, it would receive a resiliency score of 8 for drought conditions.

## 5. Data Analysis
**Goal: After collecting data from experiments, this step helps you analyze the results to determine the resiliency of the plants under adverse conditions. The following questions will guide your analysis.**

## 5.1. Have we observed significant differences between normal and adverse conditions?


  •	**Question:** Are there significant differences in biomass between the control group (normal conditions) and the experimental groups (adverse conditions)?

  •	**Action:** Use statistical tests, such as ANOVA, to determine if there is a statistically significant difference in biomass between the groups.

  •	**Output:** A statistical result (p-value) indicating whether the differences are significant.
  •	**Implementation:**

  •	Compare the average biomass between normal and adverse conditions.

  •	If the p-value is below 0.05, the difference is considered statistically significant.



### 5.2. What does the distribution of biomass look like across different conditions?
	
  • **Question:** How is biomass distributed across different conditions, and can we identify any patterns or trends?
 
  •	**Action:** Visualize the biomass data using bar charts or box plots to observe patterns in the distribution across different conditions (normal vs. adverse).
  
  •	**Output:** Graphs showing biomass distribution, allowing visual comparison of different conditions.

### 5.3. How much biomass was retained under adverse conditions?**

  •	**Question:** What percentage of biomass was retained under adverse conditions compared to normal conditions?
  
  •	**Action:** Calculate the biomass retention percentage by comparing biomass under adverse conditions to biomass under normal conditions for each group.
 
  •	**Output:** Biomass retention percentages, which can be used to calculate the Resiliency Score.

### 5.4. What is the Resiliency Score for each condition?
	
  •	**Question:** Based on the biomass retention percentage, what is the Resiliency Score (RS) for each plant under each adverse condition?
 
  •	**Action:** Use the formula to calculate the Resiliency Score for each plant:

### 5.5. What is the overall resiliency of the plant across all tested conditions?

  •	**Question:** What is the average Resiliency Score across all adverse conditions, giving a general assessment of the plant’s resilience?
 
  •	**Action:** Calculate the average Resiliency Score across all adverse conditions.
 
  •	**Output:** A single average Resiliency Score that represents the plant’s overall ability to withstand adverse conditions.
 



