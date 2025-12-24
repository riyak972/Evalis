def equal_opportunity(df, sensitive_attr, target, label=1):
    """
    Equal Opportunity:
    True Positive Rate (TPR) should be similar across groups
    """
    groups = df[sensitive_attr].unique()
    tpr = {}

    for group in groups:
        subset = df[df[sensitive_attr] == group]
        positives = subset[subset[target] == label]

        if len(positives) == 0:
            tpr[group] = 0
        else:
            tpr[group] = len(positives) / len(subset)

    return tpr
