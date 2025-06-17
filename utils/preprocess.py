from bson.binary import Binary
import uuid

# Binary UUID를 문자열로 변환하는 함수
def binary_to_uuid_string(binary_uuid):
    if isinstance(binary_uuid, Binary):
        return str(uuid.UUID(bytes=binary_uuid))
    return binary_uuid

def mongo_preprocess(df):
    df.rename(columns={'childId':'userId'}, inplace=True)
    # childId(또는 userId) 컬럼의 Binary를 문자열 UUID로 변환
    """
    if 'childId' in df.columns:
        df['childId'] = df['childId'].apply(binary_to_uuid_string)
        df.rename(columns={'childId':'userId'}, inplace=True)
    elif 'userId' in df.columns:
        df['userId'] = df['userId'].apply(binary_to_uuid_string)
    """
    if 'userId' in df.columns:
        df['userId'] = df['userId'].apply(binary_to_uuid_string)

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