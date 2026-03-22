# Evalis 
### Fairness Evaluation for ML-Based Decision Systems

Evalis is an open-source fairness auditing tool designed to evaluate bias in machine learning–based decision systems such as **student evaluation models** and **resume screening systems**.  
It helps developers **detect, visualize, and explain unfair outcomes** before deployment.

Evalis focuses on **Responsible AI**, making fairness evaluation simple, transparent, and accessible.


## Problem Statement

Machine learning models are increasingly used in:
- Student grading and evaluation  
- Resume screening and shortlisting  
- Admissions and eligibility decisions  

These models may unintentionally favor or disadvantage certain groups based on **gender, institution, or proxy attributes**.

Most existing fairness tools are:
- Too academic  
- Difficult to use  
- Closed-source or enterprise-only  

**Evalis bridges this gap** by providing a lightweight, developer-friendly fairness evaluation framework.


## Objectives

- Detect bias across sensitive attributes  
- Quantify fairness using standard metrics  
- Visualize group-wise decision differences  
- Generate human-readable fairness reports  
- Provide an extensible base for explainable AI  


## Features

- CSV dataset upload  
- Multiple sensitive attribute support (e.g., gender, college tier)  
- Demographic Parity analysis  
- Disparate Impact calculation  
- Equal Opportunity testing  
- Visual bias comparison charts  
- Plain-English fairness reports  
- Unit test coverage for core logic  


## Tech Stack

- **Language:** Python  
- **UI:** Streamlit  
- **Data Handling:** Pandas, NumPy  
- **ML Utilities:** scikit-learn  
- **Visualization:** Matplotlib  
- **Testing:** PyTest  


## Project Structure

``` markdown
evalis/
├── app.py
├── core/
│   ├── bias_metrics.py
│   ├── fairness_tests.py
│   ├── explainability.py
│   └── __init__.py
├── reports/
│   ├── report_generator.py
│   └── __init__.py
├── utils/
│   ├── file_loader.py
│   ├── validators.py
│   ├── constants.py
│   └── __init__.py
├── data/
│   ├── sample_student_evaluation.csv
│   └── student_resume.csv
├── models/
│   ├── sample_model.pkl
│   └── README.md
├── tests/
│   ├── test_bias_metrics.py
│   └── test_reports.py
├── docs/
│   ├── architecture.md
│   └── fairness_metrics.md
├── requirements.txt
├── LICENSE
└── README.md
```


## Fairness Metrics Used

### 1. Demographic Parity
Measures whether different groups receive positive outcomes at similar rates.

**Example:**  
If 60% of males are shortlisted but only 40% of females, demographic parity is violated.


### 2. Disparate Impact
Ratio of the minimum selection rate to the maximum selection rate.

**Threshold:**
- DI < 0.8 → Potential fairness risk  
- DI ≥ 0.8 → Acceptable fairness range  


### 3. Equal Opportunity
Ensures qualified individuals have equal chances of receiving positive outcomes.

Evalis compares **true positive rates across groups**.

---

## Sample Datasets

### Student Evaluation Dataset
- Gender  
- Attendance  
- Internal marks  
- Final score  
- Pass/Fail outcome  

### Resume Screening Dataset
- Gender  
- College tier  
- CGPA  
- Internships  
- Projects  
- Skills score  
- Shortlisting decision  

⚠️ All datasets are **simulated** and used strictly for demonstration.

---

## ▶ How to Run Evalis

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the application
```bash
python -m streamlit run app.py
```

### 3. Use the UI

Once the application is running in the browser:

1. Upload a CSV dataset using the **Upload CSV dataset** button  
   - Example files:
     - `data/sample_student_evaluation.csv`
     - `data/student_resume.csv`

2. Select a **Sensitive Attribute**  
   - Examples:
     - `gender`
     - `college_tier`

3. Select the **Target Column**  
   - This should be a **binary decision column**  
   - Examples:
     - `passed`
     - `shortlisted`

4. Click **Run Fairness Evaluation**

Evalis will then:
- Calculate fairness metrics
- Display group-wise selection rates
- Show a visual comparison chart
- Generate a plain-English fairness report


## Output Explanation

After running the evaluation, the following outputs are shown:

### 🔹 Demographic Parity Rates
Shows the proportion of positive outcomes for each group.

Example:
M: 0.50
F: 0.67


### 🔹 Disparate Impact Score
Measures fairness as a ratio of minimum to maximum selection rate.

Example:
Disparate Impact = 0.75


- DI < 0.8 → Potential fairness risk
- DI ≥ 0.8 → Acceptable range



### 🔹 Visual Bias Chart
A bar chart displaying selection rates across groups for quick comparison.

This helps identify bias patterns at a glance.


### 🔹 Fairness Evaluation Report
A human-readable report summarizing:
- Sensitive attribute audited
- Group-wise selection rates
- Fairness risk warning or confirmation

This report is designed for **non-technical stakeholders**.


## Test Cases

Evalis includes unit tests to validate fairness calculations and report generation.

### Test Case 1: Demographic Parity Calculation
**File:** `tests/test_bias_metrics.py`

- Input: Dataset with multiple sensitive groups and binary target
- Expected Output: Correct selection rate for each group


### Test Case 2: Disparate Impact Calculation

- Input: Group-wise selection rates
- Expected Output: Correct min/max ratio returned


### Test Case 3: Report Generation
**File:** `tests/test_reports.py`

- Input: Fairness metrics and sensitive attribute
- Expected Output:
  - Report title present
  - Group-wise results included
  - Fairness warning or confirmation displayed


### Run Tests
```bash
pytest tests/
```

## Limitations

- Evalis currently evaluates **model outcomes**, not internal model weights or training processes  
- Explainability is implemented as a placeholder; **SHAP-based feature attribution** is planned  
- Intersectional fairness (e.g., gender + college tier combined) is not yet supported  
- Datasets included are **simulated** and meant only for demonstration purposes  
- Evalis is not a production-ready decision system  

These limitations are intentional to keep the tool lightweight, transparent, and easy to extend.


## Future Scope

- SHAP-based feature-level explainability  
- Model-based prediction followed by fairness auditing  
- Downloadable fairness reports (TXT / CSV / PDF)  
- Intersectional fairness analysis  
- Threshold sensitivity and what-if analysis  
- Support for additional fairness metrics  


## Ethical Disclaimer

Evalis is a **diagnostic and educational tool** designed to support responsible AI development.

It does **not** make real-world decisions and must not be used as a standalone system for:
- Hiring
- Grading
- Admissions
- Any high-stakes automated decision-making

Users are responsible for ensuring ethical and legal compliance when applying fairness analysis.


## Contributing

Contributions are welcome.

You can contribute by:
- Adding new fairness metrics  
- Improving explainability modules  
- Enhancing visualizations  
- Writing additional test cases  
- Improving documentation  

Please open an issue or submit a pull request.


## License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this software.


## Acknowledgements

This project was built as part of an effort to promote:
- Responsible AI  
- Fairness-aware machine learning  
- Transparency in automated decision systems  

Evalis is intended to help developers **think beyond accuracy** and consider fairness as a first-class concern.
Updated README 🚀
