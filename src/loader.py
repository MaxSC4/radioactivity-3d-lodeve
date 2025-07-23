import pandas as pd

def load_points_csv(filepath: str) -> pd.DataFrame:
    """Load CSV with X, Y, Z, R columns and clean headers."""
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip().str.upper()
    return df
