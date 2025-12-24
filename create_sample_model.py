import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Sample resume-like data
data = {
    "cgpa": [8.9, 9.1, 7.2, 7.4, 8.1, 8.3, 6.8, 9.3],
    "internships": [2, 3, 1, 1, 2, 2, 0, 4],
    "projects": [4, 5, 2, 3, 3, 4, 1, 6],
    "skills_score": [85, 90, 60, 65, 78, 80, 55, 92],
    "shortlisted": [1, 1, 0, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df.drop("shortlisted", axis=1)
y = df["shortlisted"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "models/sample_model.pkl")

print("Sample model saved successfully.")
