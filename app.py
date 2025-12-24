import streamlit as st
import pandas as pd
from core.bias_metrics import demographic_parity, disparate_impact
from reports.report_generator import generate_report

st.set_page_config(page_title="Evalis", layout="centered")

st.title("Evalis")
st.write("Fairness evaluation for ML-based decision systems")

uploaded_file = st.file_uploader(
    "Upload CSV dataset",
    type=["csv"],
    key="dataset_uploader"
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    possible_sensitive_attrs = [
    col for col in df.columns 
    if df[col].dtype == "object"
    ]

    sensitive_attr = st.selectbox(
        "Select sensitive attribute to audit",
        options=possible_sensitive_attrs,
        key="sensitive_attr"
    )

    target_col = st.selectbox(
        "Select target column (model decision)",
        options=df.columns
    )

    if st.button("Run Fairness Evaluation"):
        dp_rates = demographic_parity(df, sensitive_attr, target_col)
        di_score = disparate_impact(dp_rates)

        st.subheader("Demographic Parity Rates")
        st.write(dp_rates)
        
        st.subheader("Selection Rate by Group")

        groups = list(dp_rates.keys())
        rates = list(dp_rates.values())

        chart_df = pd.DataFrame({"group": groups, "selection_rate": rates})
        chart_df = chart_df.set_index("group")

        st.bar_chart(chart_df)


        st.subheader("Disparate Impact Score")
        st.write(round(di_score, 3))

        report = generate_report(dp_rates, di_score, sensitive_attr)

        st.subheader("Evaluation Report")
        st.text(report)