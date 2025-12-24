def demographic_parity(df, sensitive_attr, target):
    """
    Calculates selection rate for each group
    """
    groups = df[sensitive_attr].unique()
    rates = {}

    for group in groups:
        subset = df[df[sensitive_attr] == group]
        rates[group] = subset[target].mean()

    return rates


def disparate_impact(dp_rates):
    """
    Ratio of minimum to maximum selection rate
    """
    values = list(dp_rates.values())

    if min(values) == 0:
        return 0.0

    return round(min(values) / max(values), 3)
