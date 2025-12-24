def validate_target_column(df, target_col):
    if df[target_col].nunique() > 2:
        raise ValueError("Target column must be binary (0/1)")
