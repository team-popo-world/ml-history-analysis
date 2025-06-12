# 평균 턴 체류시간
def avg_stay_time(df):
    turn = df[['investSessionId', 
                'turn',
                'startedAt',
                'endedAt']]
    
    avgStayTime = turn.drop_duplicates(subset=['investSessionId', 'turn']).copy()
    avgStayTime['stayTime'] = (avgStayTime['endedAt'] - avgStayTime['startedAt']).dt.total_seconds()
    avgStayTime.drop(columns=['startedAt', 'endedAt'], inplace=True)
    avgStayTime = avgStayTime.groupby('investSessionId')['stayTime'].mean().reset_index(name='avgStayTime')

    return avgStayTime