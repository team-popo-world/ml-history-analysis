# 평균 현금잔여율
def avg_cash_ratio(df, seed):
    acr = df[['investSessionId', 
          'chapterId',
          'turn',
          'currentPoint']]

    acr = acr.groupby(['investSessionId', 'chapterId', 'turn'])['currentPoint'].mean().reset_index(name='avgCurrentValue')
    acr_merged = acr.merge(seed, on='chapterId', how='left')
    acr_merged['diff'] = acr_merged['seedMoney'] - acr_merged['avgCurrentValue']
    averageCashRatio = acr_merged.groupby('investSessionId')['diff'].mean().reset_index(name="avgDiff")
        
    return averageCashRatio