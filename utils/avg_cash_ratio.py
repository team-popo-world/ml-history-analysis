# 평균 현금잔여율
def avg_cash_ratio(df):
    acr = df[['investSessionId', 
              'userId',
              'age',
              'seedMoney',
            'chapterId',
            'turn',
            'currentPoint']]

    acr = acr.groupby(['investSessionId', 'userId', 'age', 'seedMoney', 'chapterId', 'turn'])['currentPoint'].mean().reset_index(name='avgCurrentValue')
    acr['diff'] = acr['seedMoney'] - acr['avgCurrentValue']
    averageCashRatio = acr.groupby(['investSessionId', 'userId', 'age'])['diff'].mean().reset_index(name="avgDiff")
        
    return averageCashRatio