import pandas as pd
from core.bias_metrics import demographic_parity

def test_demographic_parity():
    data = {
        "gender": ["M", "F", "M", "F"],
        "shortlisted": [1, 1, 0, 0]
    }
    df = pd.DataFrame(data)
    dp = demographic_parity(df, "gender", "shortlisted")
    assert "M" in dp and "F" in dp
