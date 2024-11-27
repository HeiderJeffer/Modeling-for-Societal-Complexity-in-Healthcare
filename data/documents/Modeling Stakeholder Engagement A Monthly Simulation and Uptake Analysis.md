# Modeling Stakeholder Engagement: A Monthly Simulation and Uptake Analysis
*By Heider Jeffer*
## Step 1: Define Initial Engagement Levels
We begin with the following initial engagement levels for each stakeholder:

- **Patients**: 0.6 (60% engaged)
- **Doctors**: 0.8 (80% engaged)
- **Nurses**: 0.75 (75% engaged)
- **Administrators**: 0.5 (50% engaged)

---

## Step 2: Simulate Engagement Fluctuations for 12 Months
Random fluctuations (within the range [-0.05, +0.05]) are applied each month to the initial engagement levels. Below is the simulation for the first few months.

### Month 1
**Initial Engagement (all stakeholders):**
- Patients: 0.6
- Doctors: 0.8
- Nurses: 0.75
- Administrators: 0.5

### Month 2 (First Fluctuation)
**Random fluctuations:**
- Patients: Δ = +0.03
- Doctors: Δ = -0.02
- Nurses: Δ = +0.01
- Administrators: Δ = +0.04

**New Engagement Calculation:**
\[ \text{New Engagement}_t = \max(0, \min(1, \text{Previous Engagement}_{t-1} + \Delta)) \]

- Patients: \( 0.6 + 0.03 = 0.63 \)
- Doctors: \( 0.8 - 0.02 = 0.78 \)
- Nurses: \( 0.75 + 0.01 = 0.76 \)
- Administrators: \( 0.5 + 0.04 = 0.54 \)

**Month 2 Engagement Levels:**
- Patients: 0.63
- Doctors: 0.78
- Nurses: 0.76
- Administrators: 0.54

---

## Step 3: Calculate Uptake Rate for Month 2
The uptake rate is the average engagement across all stakeholders:
\[
\text{Uptake Rate} = \frac{\sum \text{Engagement Levels}}{N}
\]

For Month 2:
\[
\text{Uptake Rate} = \frac{0.63 + 0.78 + 0.76 + 0.54}{4} = \frac{2.71}{4} = 0.68
\]

**Uptake Rate for Month 2**: 0.68

---

## Step 4: Simulate for Month 3
**Random fluctuations:**
- Patients: Δ = -0.02
- Doctors: Δ = +0.01
- Nurses: Δ = -0.03
- Administrators: Δ = -0.01

**New Engagement Calculation:**
- Patients: \( 0.63 - 0.02 = 0.61 \)
- Doctors: \( 0.78 + 0.01 = 0.79 \)
- Nurses: \( 0.76 - 0.03 = 0.73 \)
- Administrators: \( 0.54 - 0.01 = 0.53 \)

**Month 3 Engagement Levels:**
- Patients: 0.61
- Doctors: 0.79
- Nurses: 0.73
- Administrators: 0.53

---

## Step 5: Calculate Uptake Rate for Month 3
\[
\text{Uptake Rate} = \frac{0.61 + 0.79 + 0.73 + 0.53}{4} = \frac{2.66}{4} = 0.665
\]

**Uptake Rate for Month 3**: 0.665

---

## Summary of the First 3 Months
| Month | Patients | Doctors | Nurses | Administrators | Uptake Rate |
|-------|----------|---------|--------|----------------|-------------|
| 1     | 0.6      | 0.8     | 0.75   | 0.5            | -           |
| 2     | 0.63     | 0.78    | 0.76   | 0.54           | 0.68        |
| 3     | 0.61     | 0.79    | 0.73   | 0.53           | 0.665       |

---

## Step 6: Repeat for Remaining Months
The same process is repeated for the remaining months (Month 4 to Month 12). New fluctuations are applied each month, and engagement levels and uptake rates are calculated. The final uptakes are plotted over time to visualize the model’s performance.

---

## Final Thoughts
This numerical example illustrates:
1. Engagement levels fluctuate based on random changes each month.
2. The uptake rate is calculated as the average of the engagement levels.
3. A feedback loop exists, where each month's engagement influences the next, revealing trends when visualized.
