import pandas as pd

def analyze_dataset(df: pd.DataFrame):
    col_types={}

    for col in df.columns:
        if df[col].dtype in ['int64','float64']:
            col_types[col]="numerical"
        else:
            col_types[col]  ="categorical"
    
    missing_values=df.isnull().sum().to_dict()

    return {
    "rows":df.shape[0],
    "columns":df.shape[1],
    "column_types":col_types,
    "missing_values":missing_values
        }

