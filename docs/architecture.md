# Evalis – Architecture Overview

Evalis is designed as a modular fairness evaluation tool
for ML-based decision systems.

## Architecture Layers

### 1. UI Layer
- Built using Streamlit
- Handles dataset upload and user interaction

### 2. Core Logic
- Bias metrics (demographic parity, disparate impact)
- Fairness tests (equal opportunity)

### 3. Reporting
- Generates plain-English fairness reports
- Designed for non-technical stakeholders

### 4. Extensibility
- Future support for model-based evaluation
- Explainability using SHAP
- Additional fairness metrics

This modular design allows Evalis to scale without refactoring.
