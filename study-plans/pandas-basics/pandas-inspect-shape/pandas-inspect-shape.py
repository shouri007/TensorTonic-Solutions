import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    df = pd.DataFrame(data=data)
    shape = df.shape
    cols = df.columns
    return {
        "rows": shape[0],
        "cols": shape[1],
        "columns": cols.tolist(),
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "total_values": shape[0] * shape[1]
    }
    pass