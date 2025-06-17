# 평균 tag 뉴스 발생 턴 체류 시간
def tag_avg_stay_time(df):
    tag_turn_df = df[['investSessionId',
                        'userId',
                        'age',
                        'turn',
                        'newsTag',
                        'startedAt',
                        'endedAt']].drop_duplicates()

    tag_turn_df = tag_turn_df[tag_turn_df['newsTag'] != "all"]
    tag_turn_df["turnDuration"] = tag_turn_df["endedAt"] - tag_turn_df["startedAt"]
    tagAvgStayTime = tag_turn_df.groupby(["investSessionId", 'userId', 'age'])["turnDuration"].mean().reset_index().rename(columns={"turnDuration":"tagTrunDuraion"})

    return tagAvgStayTime