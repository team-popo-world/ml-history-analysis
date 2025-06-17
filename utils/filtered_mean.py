import pandas as pd

def filtered_mean(df, col, userId):

<<<<<<< HEAD
    # 우리 아이랑 같은 나이를 갖는 행만 필터링
    child_age = df.loc[df["userId"]==userId, "age"] 
    df = df[df["age"] == child_age]

    # 우리아이 나이대 평균
    col_mean = df[f"{col}"].mean()
    df[f'{col}Mean'] = col_mean

    # 우리아이 데이터만 필터링
    filtered_df = df[df["userId"]==userId]
=======
    col_mean = df.groupby("age")[f"{col}"].mean()
    df[f'{col}Mean'] = df['age'].map(col_mean)

    filtered_df = df[df["childId"]==userId]
    filtered_df.drop(columns="age", inplace=True)
>>>>>>> 3a638d832466262e71b6e1cce3a9f0eb8aec9ac5

    return filtered_df