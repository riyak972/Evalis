from reports.report_generator import generate_report

def test_report_generation():
    rates = {"M": 0.6, "F": 0.4}
    report = generate_report(rates, 0.67, "gender")
    assert "Fairness Evaluation Report" in report
