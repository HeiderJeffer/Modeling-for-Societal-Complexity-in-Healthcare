# Qualitative Analysis of Stakeholder Engagement Simulation

*By Heider Jeffer*

The **qualitative analysis** in the code performs a series of interpretative assessments on the simulation results of stakeholder engagement over a period of 12 months. Below is a detailed breakdown of the steps involved in this analysis and the type of output it generates.

---

## **Qualitative Analysis Process:**

### 1. **Stakeholder Engagement Trends**
   - For each stakeholder (Patients, Doctors, Nurses, Administrators), the analysis explores how engagement with various activities (e.g., "Participation in Care", "Feedback and Communication") fluctuates over time.
   
   **Key Points**:
   - The average engagement for each activity is extracted.
   - Fluctuations in engagement are highlighted. If the engagement level for an activity fluctuates by more than 0.1 (i.e., there is a significant variation between the maximum and minimum engagement values for the activity), it’s flagged as needing attention. The code suggests strategies to stabilize these fluctuations.
   - For activities with stable engagement (small fluctuations), the code remarks that the engagement is fairly steady.

   **Output Example**:
   ```
   Stakeholder Engagement Trends:
   
   Patients:
     - Participation in Care: Avg Engagement = 0.60
       * Engagement is fairly stable for this activity.
     - Feedback and Communication: Avg Engagement = 0.50
       * Noticeable fluctuation in engagement from 0.45 to 0.55. Consider strategies to stabilize this.
   ```

---

### 2. **Stakeholder Comparison**
   - This compares the average engagement (uptake rate) of each stakeholder across all their activities.
   
   **Key Points**:
   - Stakeholders with an average uptake rate below 0.6 are considered to have potential areas for improvement in engagement. 
   - Stakeholders with an average uptake rate above 0.6 are viewed positively, suggesting good engagement.
   
   **Output Example**:
   ```
   Comparison of Stakeholder Engagement Levels:
   - Patients: Below average uptake rate (0.55). This suggests potential areas for further engagement or outreach.
   - Doctors: Above average uptake rate (0.72). This is a positive indicator of stakeholder engagement.
   ```

---

### 3. **Identifying Key Activities for Improvement**
   - The analysis also identifies specific activities that might require more attention based on their average engagement levels across all stakeholders.
   
   **Key Points**:
   - Activities with an average engagement rate below 0.6 are flagged for improvement.
   - Activities with positive engagement (average above 0.6) are noted as having a healthy level of engagement.
   
   **Output Example**:
   ```
   Identifying Key Activities for Improvement:
   - Activity: Participation in Care has a lower than average engagement (0.58). This might need more attention.
   - Activity: Direct Care Delivery shows positive engagement levels (0.75).
   ```

---

## **Qualitative Analysis Output Summary:**

After running the qualitative analysis, the output consists of:

- **Stakeholder Engagement Trends**: A detailed examination of how each stakeholder's engagement with different activities evolves, including observations on fluctuations.
- **Stakeholder Comparison**: A comparison of the average engagement levels (uptake rates) for each stakeholder, highlighting those below the desired threshold (0.6) and suggesting further outreach for those with low engagement.
- **Identifying Key Activities for Improvement**: Activities that need attention due to low engagement levels are identified, while those with high engagement are flagged as areas of strength.

---

## **Visual Output:**

- **Engagement Trends**: A line plot visualizes how the engagement levels for different activities fluctuate over the months.
- **Uptake Rates**: A second plot shows how each stakeholder's overall engagement changes monthly, helping to visualize trends in uptake over time.
- **Distribution of Engagement**: Boxplots provide a summary of engagement distribution for each stakeholder, showing the spread of engagement across different activities, helping to visually identify where fluctuations occur.

These qualitative insights are valuable for improving the effectiveness of stakeholder engagement in a healthcare context, pointing to areas that require intervention (e.g., activities with low engagement) and recognizing strengths (e.g., activities with stable or high engagement).


**The Output of Qualitative Analysis of Stakeholder Engagement. Developed using Python by Heider Jeffer**


![Engagement Trends by Activity](https://github.com/HeiderJeffer/Participatory-Modeling-for-Societal-Complexity-in-Healthcare/blob/main/data/images/4.png)

```Python output:```
```Python

Qualitative Analysis:

Stakeholder Engagement Trends:

Patients:
  - Participation in Care: Avg Engagement = 0.55
    * Noticeable fluctuation in engagement from 0.45 to 0.60. Consider strategies to stabilize this.
  - Feedback and Communication: Avg Engagement = 0.59
    * Noticeable fluctuation in engagement from 0.50 to 0.67. Consider strategies to stabilize this.
  - Health Literacy: Avg Engagement = 0.65
    * Noticeable fluctuation in engagement from 0.55 to 0.70. Consider strategies to stabilize this.
  - Preventative Care: Avg Engagement = 0.62
    * Noticeable fluctuation in engagement from 0.52 to 0.70. Consider strategies to stabilize this.

Doctors:
  - Direct Care Delivery: Avg Engagement = 0.81
    * Engagement is fairly stable for this activity.
  - Professional Development: Avg Engagement = 0.70
    * Noticeable fluctuation in engagement from 0.64 to 0.74. Consider strategies to stabilize this.
  - Collaboration: Avg Engagement = 0.75
    * Noticeable fluctuation in engagement from 0.70 to 0.85. Consider strategies to stabilize this.
  - Research and Advocacy: Avg Engagement = 0.66
    * Engagement is fairly stable for this activity.

Nurses:
  - Patient-Centered Care: Avg Engagement = 0.78
    * Noticeable fluctuation in engagement from 0.74 to 0.84. Consider strategies to stabilize this.
  - Coordination and Communication: Avg Engagement = 0.85
    * Noticeable fluctuation in engagement from 0.80 to 0.91. Consider strategies to stabilize this.
  - Professional Development: Avg Engagement = 0.67
    * Engagement is fairly stable for this activity.
  - Community Involvement: Avg Engagement = 0.75
    * Noticeable fluctuation in engagement from 0.60 to 0.86. Consider strategies to stabilize this.

Administrators:
  - Operational Oversight: Avg Engagement = 0.48
    * Noticeable fluctuation in engagement from 0.43 to 0.57. Consider strategies to stabilize this.
  - Stakeholder Coordination: Avg Engagement = 0.38
    * Noticeable fluctuation in engagement from 0.30 to 0.45. Consider strategies to stabilize this.
  - Strategic Planning: Avg Engagement = 0.58
    * Engagement is fairly stable for this activity.
  - Data-Driven Decision-Making: Avg Engagement = 0.67
    * Noticeable fluctuation in engagement from 0.60 to 0.73. Consider strategies to stabilize this.

Comparison of Stakeholder Engagement Levels:
  - Administrators: Below average uptake rate (0.53). This suggests potential areas for further engagement or outreach.
  - Doctors: Above average uptake rate (0.73). This is a positive indicator of stakeholder engagement.
  - Nurses: Above average uptake rate (0.76). This is a positive indicator of stakeholder engagement.
  - Patients: Above average uptake rate (0.60). This is a positive indicator of stakeholder engagement.

Identifying Key Activities for Improvement:
  - Activity: Data-Driven Decision-Making shows positive engagement levels (0.67).
  - Activity: Operational Oversight has a lower than average engagement (0.48). This might need more attention.
  - Activity: Stakeholder Coordination has a lower than average engagement (0.38). This might need more attention.
  - Activity: Strategic Planning has a lower than average engagement (0.58). This might need more attention.
  - Activity: Collaboration shows positive engagement levels (0.75).
  - Activity: Direct Care Delivery shows positive engagement levels (0.81).
  - Activity: Professional Development shows positive engagement levels (0.68).
  - Activity: Research and Advocacy shows positive engagement levels (0.66).
  - Activity: Community Involvement shows positive engagement levels (0.75).
  - Activity: Coordination and Communication shows positive engagement levels (0.85).
  - Activity: Patient-Centered Care shows positive engagement levels (0.78).
  - Activity: Feedback and Communication has a lower than average engagement (0.59). This might need more attention.
  - Activity: Health Literacy shows positive engagement levels (0.65).
  - Activity: Participation in Care has a lower than average engagement (0.55). This might need more attention.
  - Activity: Preventative Care shows positive engagement levels (0.62).
```
