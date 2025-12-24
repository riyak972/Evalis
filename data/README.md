# Data Directory

This directory contains **simulated datasets** used to demonstrate and test the
fairness evaluation capabilities of **Evalis**.

All datasets are **synthetic**, **anonymized**, and created solely for
educational and experimental purposes.


## Included Datasets

### 1️ `sample_student.csv`

This dataset simulates a **student performance evaluation system**.

#### Columns
- `student_id` – Unique identifier  
- `gender` – Sensitive attribute (M/F)  
- `age` – Student age  
- `attendance` – Attendance percentage  
- `internal_marks` – Internal assessment score  
- `final_score` – Final evaluation score  
- `passed` – Binary outcome (1 = Pass, 0 = Fail)

#### Use Case
- Evaluating fairness in academic grading systems
- Auditing pass/fail outcomes across demographic groups


### 2️ `student_resume.csv`

This dataset simulates a **resume screening / shortlisting system**.

#### Columns
- `candidate_id` – Unique identifier  
- `gender` – Sensitive attribute  
- `college_tier` – Proxy attribute (1 = Top tier, 3 = Lower tier)  
- `cgpa` – Academic performance  
- `internships` – Number of internships  
- `projects` – Number of projects  
- `skills_score` – Normalized skills score (0–100)  
- `shortlisted` – Binary outcome (1 = Shortlisted, 0 = Rejected)

#### Use Case
- Auditing fairness in hiring or ATS-style systems
- Detecting bias linked to institutional or demographic factors


## ⚠️ Important Notes

- These datasets **do not represent real individuals**
- Values are intentionally designed to surface **potential bias patterns**
- Datasets should **not** be used for real-world decision-making
- They exist purely to demonstrate Evalis’s fairness metrics

---

## Extending the Data

Users can:
- Replace these files with their own CSV datasets
- Add new sensitive attributes (e.g., region, background)
- Experiment with different outcome distributions

Ensure that:
- The target column is **binary (0/1)**
- Sensitive attributes are categorical

---

## Ethical Disclaimer

These datasets are provided for **educational, testing, and demonstration purposes only**.
They must not be interpreted as real hiring or academic evaluation data.
