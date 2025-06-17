# 평균 현금잔여율
def avg_cash_ratio(df):
    acr = df[['investSessionId', 
              'userId',
              'age',
              'seedMoney',
            'chapterId',
            'turn',
            'currentPoint']].copy()

    acr = acr.groupby(['investSessionId', 'userId', 'age', 'seedMoney', 'chapterId'])['currentPoint'].mean().reset_index(name='avgCurrentValue')
    
    acr['diff'] = acr['seedMoney'] - acr['avgCurrentValue']
    acr["avgCashRatio"] = acr["diff"] / acr["seedMoney"]
    averageCashRatio = acr[['investSessionId', 'userId', 'age', 'avgCashRatio']].copy()
        
    return averageCashRatio