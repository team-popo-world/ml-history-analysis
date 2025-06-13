import pandas as pd

def filtered_mean(df, col, userId):

    col_mean = df.groupby("age")[f"{col}"].mean()
    df[f'{col}Mean'] = df['age'].map(col_mean)

    filtered_df = df[df["childId"]==userId]
    filtered_df.drop(columns="age", inplace=True)

    return filtered_df