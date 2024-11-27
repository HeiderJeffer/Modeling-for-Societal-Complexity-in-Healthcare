# Explanation of the Python Code
*By Heider Jeffer*

## Contents
1. [Part 1: Quantitative and Qualitative Analysis of Stakeholder Engagement Simulation](https://github.com/HeiderJeffer/Participatory-Modeling-for-Societal-Complexity-in-Healthcare/blob/main/data/documents/Explanation%20of%20the%20Python%20Code.md#part-1-quantitative-and-qualitative-analysis-of-stakeholder-engagement-simulation)
2. [Part 2: Engagement and Uptake Insights](https://github.com/HeiderJeffer/Participatory-Modeling-for-Societal-Complexity-in-Healthcare/blob/main/data/documents/Explanation%20of%20the%20Python%20Code.md#part-2-engagement-and-uptake-insights)
3. [Part 3: Statistical Distribution Representing the Stakeholders and Their Activities](https://github.com/HeiderJeffer/Participatory-Modeling-for-Societal-Complexity-in-Healthcare/blob/main/data/documents/Explanation%20of%20the%20Python%20Code.md#part-3-statistical-distribution-representing-the-stakeholders-and-their-activities)


# Part 1: Quantitative and Qualitative Analysis of Stakeholder Engagement Simulation

The provided code is a **simulation and analysis tool** for modeling **stakeholder engagement in healthcare**, developed in Python by Heider Jeffer. Below is a breakdown of its components:


## 1. Stakeholders and Activities Initialization

The `stakeholders` dictionary defines:
- **Four types of stakeholders** (`Patients`, `Doctors`, `Nurses`, `Administrators`).
- Each stakeholder has a set of **activities** with associated **base engagement levels** (a numerical value between 0 and 1).

Example:
```python
'Patients': {
    'Participation in Care': 0.6,
    'Feedback and Communication': 0.5,
}
```

## 2. Simulating Engagement Levels Over Time

### The `simulate_activity_engagement` function:

- Generates monthly engagement levels for each activity and stakeholder over a specified number of months (`months`).
- Adds a random fluctuation (within ±`fluctuation`) to simulate realistic variability.
- Clamps values between 0 and 1 to ensure they remain valid.
- Results are stored in a pandas DataFrame with columns: **Stakeholder**, **Activity**, **Month**, and **Engagement**.

### How It Works:

1. Iterates over stakeholders and their activities.
2. Initializes engagement levels for each activity.
3. Simulates random changes for each subsequent month.
4. Stores data for visualization and analysis.


# Explanation of the Code

The provided code is a **simulation and analysis tool** for modeling **stakeholder engagement in healthcare**, developed in Python by Heider Jeffer. Below is a breakdown of its components:

## 1. Stakeholders and Activities Initialization
The `stakeholders` dictionary defines:
- **Four types of stakeholders** (`Patients`, `Doctors`, `Nurses`, `Administrators`).
- Each stakeholder has a set of **activities** with associated **base engagement levels** (a numerical value between 0 and 1).

Example:

```Python
'Patients': {
    'Participation in Care': 0.6,
    'Feedback and Communication': 0.5,
   }
   ```

## 2. Simulating Engagement Levels Over Time

### The `simulate_activity_engagement` function:

- Generates monthly engagement levels for each activity and stakeholder over a specified number of months (`months`).
- Adds a random fluctuation (within ±`fluctuation`) to simulate realistic variability.
- Clamps values between 0 and 1 to ensure they remain valid.
- Results are stored in a pandas DataFrame with columns: `Stakeholder`, `Activity`, `Month`, and `Engagement`.

### How It Works:

1. Iterates over stakeholders and their activities.
2. Initializes engagement levels for each activity.
3. Simulates random changes for each subsequent month.
4. Stores data for visualization and analysis.


## 3. Data Visualization

### Engagement Levels by Activity:

- Line plot of engagement levels across months.
- `sns.lineplot` uses `hue='Activity'` to differentiate activities and `style='Stakeholder'` to identify stakeholders.

### Monthly Uptake Rates by Stakeholder:

- Shows the average engagement level for each stakeholder over time.


## 4. Analysis

### a. Average Engagement

Calculated for each stakeholder and activity:

```python
average_engagement = df_activity_engagement.groupby(['Stakeholder', 'Activity'])['Engagement'].mean()
```

### b. Uptake Rates
The `calculate_uptake_rate` function computes:

- The mean engagement across all activities for each stakeholder.

### c. Qualitative Analysis
The `qualitative_analysis` function:

#### Trends:
- Examines fluctuations and stability of engagement levels for each stakeholder's activities.
- Identifies stable activities and those needing intervention due to large fluctuations.

#### Stakeholder Comparison:
- Flags stakeholders with below-average uptake rates for potential improvement.

#### Key Activities for Improvement:
- Highlights activities with average engagement < 0.6, suggesting focus areas.


## 5. Usage

### Simulation

The simulation runs for 12 months by default. You can adjust months for a different timeframe:

```Python
df_activity_engagement = simulate_activity_engagement(stakeholders, months=months)
```
### Outputs
- Plots: Show engagement trends and stakeholder uptake over time.
- Printed Analysis: Provides actionable insights about trends, stakeholder performance, and activity improvement.


## 6. Expandable Design

- New stakeholders or activities can easily be added to the stakeholders dictionary.
- Fluctuation, simulation duration, or analysis methods can be tuned for specific scenarios.

## 7. Key Features
- Dynamic Simulation: Captures realistic, fluctuating engagement over time.
- Quantitative & Qualitative Analysis: Combines statistical metrics with interpretive insights.
- Visualization: Engages users with clear, insightful plots.
- Extensibility: Supports evolving healthcare scenarios and requirements.

This code is an excellent example of integrating data science tools (like pandas and seaborn) with healthcare management applications for informed decision-making.


# Part 2: Engagement and Uptake Insights

This document provides an overview of engagement trends, average engagement levels, and uptake rates for various stakeholders over a 12-month period. These insights help in identifying areas of improvement and designing targeted strategies for enhanced participation.

---

## 1. Engagement Trends by Activity
A visual representation of how engagement levels for each activity fluctuate over 12 months.

**Graph Description:**  
- Displays monthly engagement levels for activities like "Direct Care Delivery" (for doctors) and "Data-Driven Decision-Making" (for administrators).  
- Helps in identifying periods of high and low engagement for better resource allocation.


![Engagement Trends by Activity](https://drive.google.com/uc?id=109KVc6RpfEXbiYAisPQIXoxx0XvJJWXF)


---

## 2. Average Engagement Levels

### Average Engagement Levels by Stakeholder and Activity

| **Stakeholder**   | **Activity**                       | **Average Engagement Level** |
|--------------------|------------------------------------|------------------------------|
| Administrators     | Data-Driven Decision-Making       | 0.58                         |
|                    | Operational Oversight             | 0.52                         |
|                    | Stakeholder Coordination          | 0.49                         |
|                    | Strategic Planning                | 0.54                         |
| Doctors            | Collaboration                     | 0.76                         |
|                    | Direct Care Delivery              | 0.82                         |
|                    | Professional Development          | 0.72                         |
|                    | Research and Advocacy             | 0.67                         |
| **...**            | **...**                           | **...**                      |

---

## 3. Uptake Rates by Stakeholder

### Overall Uptake Rate by Stakeholder

| **Stakeholder**   | **Overall Uptake Rate** |
|--------------------|-------------------------|
| Administrators     | 0.54                    |
| Doctors            | 0.74                    |
| Nurses             | 0.71                    |
| Patients           | 0.59                    |

---

## 4. Monthly Uptake Rate Plot

A graph showing the aggregated uptake rates for each stakeholder group over the 12-month period.

**Graph Description:**  
- Highlights trends in uptake rates for stakeholders such as Administrators, Doctors, Nurses, and Patients.  
- Identifies seasonal or periodic variations for better planning and strategy.


![Monthly Uptake Rate Plot](https://drive.google.com/uc?id=109gvIClIPaZ1rKuUIj57dfTv5ix_-_kk)

---

### Summary
This detailed analysis provides actionable insights into:
- Activity-specific engagement trends to address stakeholder-specific needs.
- Monthly and overall uptake rates to identify and mitigate barriers to participation.
- Enhanced strategic planning for improving engagement and uptake.

<!--
For further information or to contribute to this analysis, please reach out to the KTH team.
-->

---


 
# Part 3: Statistical Distribution Representing the Stakeholders and Their Activities

 To design a statistical distribution representing the stakeholders and their activities, we can approach it in the following structured steps:

## Goal:

To visualize the distribution of engagement levels for each stakeholder and their activities over a simulated period. This distribution will highlight patterns, variability, and central tendencies.

## Design Plan:

1. Data Representation:

- Use the engagement simulation data for stakeholders and activities
```
(df_activity_engagement).
```

- Group engagement levels by stakeholder and activity.

2. Distribution Type:

- Use box plots to showcase engagement level distributions across months for each stakeholder and activity.
- Alternatively, use kernel density plots (KDE) or histograms for a smoothed view of engagement level distributions.

3. Implementation:

- Each stakeholder will have a separate visualization grouping their activities.
- We'll use subplots to show side-by-side comparisons of engagement distributions for activities.


4. Visualization:

- Label axes appropriately (Activity, Engagement Level).
- Add titles for clarity, e.g., "Engagement Level Distribution for Stakeholders and Activities."
- Ensure the legend identifies stakeholders or activities.

## Code Implementation

Here’s how you can create the distribution visualization:

```Python
# Statistical Distribution Visualization for Stakeholders and Activities
plt.figure(figsize=(16, 10))

# Create a subplot for each stakeholder
stakeholders_list = df_activity_engagement['Stakeholder'].unique()
for i, stakeholder in enumerate(stakeholders_list, 1):
    plt.subplot(2, 2, i)
    stakeholder_df = df_activity_engagement[df_activity_engagement['Stakeholder'] == stakeholder]
    
    # Create a boxplot for each activity
    sns.boxplot(data=stakeholder_df, x='Activity', y='Engagement', palette="viridis")
    
    # Enhance plot appearance
    plt.title(f"Engagement Level Distribution - {stakeholder}")
    plt.xlabel("Activity")
    plt.ylabel("Engagement Level")
    plt.ylim(0, 1)
    plt.xticks(rotation=30, ha='right')

# Adjust layout
plt.tight_layout()
plt.suptitle("Engagement Level Distribution for Stakeholders and Their Activities", fontsize=16, y=1.02)
plt.show()
```

## Explanation of the Visualization:


1. Boxplot:

- The box shows the interquartile range (IQR) of engagement levels for each activity (middle 50% of data).
- The line inside the box indicates the median engagement level.
- Whiskers and potential outliers show variability.

2. Customization:

- Stakeholders are grouped into separate subplots for clarity.
- Activities are plotted on the x-axis, engagement levels on the y-axis.

## Additional Insights (Optional):
- Overlay KDE or Histogram: For an individual stakeholder's activities, plot engagement levels as a density curve or histogram for better insight into engagement trends.
- Heatmap: Create a heatmap showing average engagement levels for stakeholders and activities.


