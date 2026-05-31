import pandas as pd

def select_column(data, column):
    series = data[column]
    return {"values": series, "length": len(series)}