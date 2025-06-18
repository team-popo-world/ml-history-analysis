import pandas as pd

def filtered_mean(df, col, userId):

    # 우리 아이랑 같은 나이를 갖는 행만 필터링
    child_age = df.loc[df["userId"]==userId, "age"] 
    df = df[df["age"] == child_age]

    # 우리아이 나이대 평균
    col_mean = df[f"{col}"].mean()
    df[f'{col}Mean'] = col_mean

    # 우리아이 데이터만 필터링
    filtered_df = df[df["userId"]==userId]

    # age 컬럼 제거??
    filtered_df = filtered_df.drop(columns="age")

    return filtered_df