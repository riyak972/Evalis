# Fairness Metrics Used in Evalis

## 1. Demographic Parity
Measures whether different groups receive positive outcomes
at similar rates.

Example:
If 60% of males are shortlisted but only 40% of females,
demographic parity is violated.

## 2. Disparate Impact
Ratio of the minimum to maximum selection rate across groups.

Threshold:
- DI < 0.8 → Potential bias
- DI ≥ 0.8 → Acceptable fairness

## 3. Equal Opportunity
Ensures that qualified individuals have equal chances
of receiving positive outcomes across groups.

Evalis uses Equal Opportunity to compare true positive rates.
