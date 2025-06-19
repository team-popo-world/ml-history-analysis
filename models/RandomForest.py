import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# 1. 데이터 예시 (가상의 데이터)
"""
# 투자 성향 클러스터링 data
- invest_session_id 
- child_id 
- sex 
- age 
- chapter_id
- trade_participation_turn (거래 참여 턴 개수)
- num_of_transaction (거래 횟수, +/- 클릭 횟수)
- avg_cash_ratio (평균 현금잔여율)
- turn_dwell_time (평균 턴 체류시간)
- buy_sell_ratio (고/중/저 구매/판매 비율)
- tag_turn_dwell_time (평균 tag 뉴스 발생 턴 체류시간)
- risk_tolerance (위험 감수율)
- bet_success_rate (배팅 성공율)
"""

def random_forest(df):
    # 입력(X), 타깃(y) 분리
    X = df.drop(columns=["investType"])
    y = df["investType"]

    # 데이터 분할
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 모델 정의 및 학습
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # 예측 및 평가
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

    # 학습 완료 후 저장
    joblib.dump(clf, "random_forest_model.pkl")


def rf_predict_invest_type(df):
    # 모델 불러오기
    clf = joblib.load("random_forest_model.pkl")

    # 예측 수행
    predictions = clf.predict(df)

    # 결과 반환
    df["predicted_investType"] = predictions
    return df
