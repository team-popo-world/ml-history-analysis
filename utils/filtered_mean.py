
import pandas as pd

def filtered_mean(df, col, childId):

    col_mean = df.groupby("age")[f"{col}"].mean()
    df[f'{col}Mean'] = df['age'].map(col_mean)

    filtered_df = df[df["childId"]==childId]

    return filtered_df