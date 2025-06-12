def mongo_preprocess(df):
    ### 나중에 삭제될 코드 ###
    df.rename(columns={'childId': 'userId'}, inplace=True)
    ########################

    df['riskLevel'] = df['riskLevel'].replace({
        '고위험 고수익': 'high',
        '균형형': 'mid',
        '장기 안정형': 'low'
    })

    df.sort_values(by=['investSessionId', 'riskLevel', 'turn'], inplace=True)
    df['deltaShares'] = df.groupby(['investSessionId', 'riskLevel'])['numberOfShares'].diff()
    df['deltaShares'] = df['deltaShares'].fillna(df['numberOfShares'])
    df['deltaShares'] = df['deltaShares'].astype(int)

    return df