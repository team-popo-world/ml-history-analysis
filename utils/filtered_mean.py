import pandas as pd

def filtered_mean(df, col, userId):

    # 우리 아이 나이 추출 (단일 값으로)
    child_age_series = df.loc[df["userId"] == userId, "age"]
    if child_age_series.empty:
        raise ValueError(f"userId '{userId}'에 해당하는 age 정보가 없습니다.")

    child_age = child_age_series.iloc[0]  # 단일 값

    # 우리 아이와 같은 나이만 필터링
    same_age_df = df[df["age"] == child_age].copy()

    # 컬럼이 하나일 경우: 문자열 -> 리스트로 변환
    if isinstance(col, str):
        col = [col]

    # 평균 계산 및 새로운 컬럼 추가
    for c in col:
        if c not in same_age_df.columns:
            raise KeyError(f"컬럼 '{c}'이(가) DataFrame에 존재하지 않습니다.")
        col_mean = same_age_df[c].mean()
        same_age_df[f'{c}Mean'] = col_mean

    # 우리아이 데이터만 필터링
    filtered_df = same_age_df[same_age_df["userId"]==userId]

    # age 컬럼 제거??
    filtered_df = filtered_df.drop(columns="age")

    return filtered_df