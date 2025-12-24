def generate_report(dp_rates, di_score, sensitive_attr):
    report = f"""
Evalis – Fairness Evaluation Report
Sensitive Attribute: {sensitive_attr}

Group-wise Selection Rates:
"""

    for group, rate in dp_rates.items():
        report += f"- {group}: {rate:.2f}\n"

    report += f"\nDisparate Impact Score: {di_score:.2f}\n"

    if di_score < 0.8:
        report += (
            "\n Fairness Risk Detected.\n"
            "The model shows unequal selection rates across groups.\n"
            "Review features and thresholds before deployment."
        )
    else:
        report += (
            "\n No major fairness risk detected.\n"
            "Selection rates are within acceptable limits."
        )

    return report
