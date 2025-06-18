# 거래 횟수
def transaction_num(df):
    nt = df[['investSessionId', 
          'turn',
          'riskLevel',
          'plusClick',
          'minusClick']].copy()

    nt['click'] = nt['plusClick'] + nt['minusClick']
    transactionNum = nt.groupby('investSessionId')[['click']].mean().reset_index()

    return transactionNum