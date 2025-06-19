import json
import uuid
import random
from datetime import datetime, timedelta
import base64
import os

# 기본 설정
CHAPTERS = ["1111", "2222", "3333", "4444"]
SEED_MONEY = {"1111": 700, "2222": 2000, "3333": 5000, "4444": 10000}
RISK_LEVELS = ["고위험 고수익", "중위험 균형형", "저위험 저수익"]
INVESTMENT_TYPES = ["안정형", "안정추구형", "위험중립형", "적극투자형", "공격투자형"]
NEWS_TAGS = ["all", "high", "mid"]
TRANSACTION_TYPES = ["BUY", "SELL", "KEEP"]
SCENARIO_ID = {'1111': ['cf5096fc-f688-48de-a7f5-0e1da42427d2',
  'fa384163-cc57-45d4-ae42-d233b987cc08',
  'a2be0f02-14c4-4a10-9c49-cbbac74bee08',
  '70ea61da-70d3-42b7-bccf-b24c5ed27fa4',
  'e4d301f5-cfc9-41b0-9caf-d713fe7361c8',
  '3242f82b-0bd2-4f9a-9b21-5ccfa0ffc25c',
  'c04d0415-eee8-4fc9-8e87-1d91ce6cbaea',
  '97ad7e42-3675-4e27-b9d5-be0a8e6a9981',
  'af12c58d-f3c1-450b-bd79-e22e080d261f',
  '3cf01464-fd5b-445e-9c47-b65046af5a04',
  'df694cd0-efbe-4b38-b332-0ff82a885afb',
  'd31b4f13-be8f-4e05-a8ac-b3f8fc4c711b',
  'eab5bd7d-49f3-45b2-98da-ca6efce926e0',
  'ca0163d3-a9dc-49f9-a7eb-439cdcc99259',
  '7548eaac-69bc-4883-b302-331f25c97928',
  '90847083-c09a-4e38-aa67-f07502418e98',
  '21fb2f09-4303-4d7f-abfe-e4f01d604fbc',
  'aeeb2ad0-5768-48af-a858-602ca9b486cc',
  '75fa7fd3-b2ef-45c5-b518-e5b5ae8981bd',
  'd6474e0e-9b85-44ac-aaeb-04a4396804c5',
  'b534c0b1-5130-4e3c-961e-1c58b4b1ff39',
  '01e9154f-716a-4bdf-bbc1-dffc5bbc5305',
  '8da28cf2-22c1-438b-a169-71f33408fde2'],
 '2222': ['eac53c18-0503-4859-8f28-f916b84fb2d2',
  '76ffeedd-674e-4f99-b783-234d543d98b4',
  'd0fa81a4-54e0-48b7-917f-3f997761fc75',
  '89565e93-67b1-45e9-8a9d-f8e5a0a7f41d',
  '57886c1a-07cb-48fe-9588-bc3171e4ca78',
  '6663e9ec-eed8-4cfc-8aeb-29ff973f6b88',
  '9736f068-e577-480e-bfb4-633f732d6047',
  'e7f634f8-3a4a-433d-9a3d-b945da07e777',
  '643d9f57-86cd-415d-9da3-8a6ffba84c15',
  'd1400232-7632-4700-a2ed-108043b95b62',
  '407273a5-6dc8-41e7-b5f0-80acbe5c17d1'],
 '3333': ['eb9100dc-3e3f-4f68-ba9f-e47d57d2ca5f',
  'd784e15f-3d18-4065-831b-8b9854771dae',
  'a3b86127-568d-4a46-a749-9666591827ae',
  '2f0a61ae-d4f5-4618-8fa0-b3f1ce82a324',
  'fb0406a3-bf07-44f3-a365-50a584285322',
  '915ab338-4315-47fe-b3c3-e79f0ac2d836',
  '7bda23f1-81b4-4719-8d73-c6b3f86f84f4',
  'ad3ddc52-e115-41cc-9b17-a1fbf2064d2f',
  '7ec6c655-8b78-4dc1-bce4-579a7e83bc61'],
 '4444': ['1510c2f4-92d0-4eae-9d60-2b084a7ded45']}


# 사용자 ID 목록 (첨부된 CSV 파일 기반)
USER_IDS = [
    'd97a07eb-8dd9-4cbe-a4c4-8c61017ada71',
    'b650347b-cdaf-4248-bd63-7c16ace78286',
    'c929fc99-3407-4e67-b9bb-fe19745c61b8',
    'd7fbb0db-1929-4140-9b64-58d1659d9b3e',
    '5cf29ca0-65ad-45df-94af-1d625c45ed74',
    '2d0cd3c8-768f-4578-9d70-929e873abb29',
    '4e6e7fc1-fe03-41d5-8f02-0766a377bf31',
    '2617b0f9-026b-469b-a7ed-2489f37e3e5f',
    'bab047ff-e121-494a-855b-62fc714e0300',
    'c97b6d89-23b9-4216-af10-e22d6c44f1d1',
    '2bf33509-f117-49b9-98fb-89cdaab60408',
    'fa975c93-78ec-49c6-b60f-e70435f18c34',
    'd84bdd45-4ff2-41bc-9641-69ec3089175b',
    'f63ae87c-32e3-471e-99ff-feb60ec50760',
    '32803480-6b17-4d83-81b2-4684e033b9d2',
    'd4af0657-f9db-40ff-babd-68681db7ddeb',
    '160c52d9-fb17-4d67-a2af-6bed345f7ca5',
    'a79d7ff7-ed5e-4e8a-be4e-5b0b2c230d83',
    '237aac1b-4d6f-4ca9-9e4f-30719ea5967d',
    '3ed8a159-adb0-4380-a648-e015cb82690a',
    'fd966d82-9b94-4565-a3a6-ce3df23f69a8',
    '5bda4ade-431a-47ef-a62c-7bd895ece820',
    '956f51a8-d6a0-4a12-a22b-9da3cdffc879',
    'f0220d43-513a-4619-973d-4ed84a42bf6a',
    'da35e508-de86-44f7-b7bf-ebffd85a3b5c',
    '54c3318f-57ef-47a4-bc51-7b470e476e7d',
    '8dd27193-ae74-42ce-913f-c400bddcb4e8',
    'd0a188a3-e24e-4772-95f7-07e59ce8885e',
    'da3466ac-984a-4a19-af87-f28e4d76cf1f',
    '22b19e79-5822-46f9-8e3f-7e55e751f9dc',
    '8d8a3d15-4058-4e07-8ac6-2089f7f4c459'
 ]


def generate_binary_id():
    """UUID 형태의 문자열 ID 생성"""
    # 16바이트 랜덤 데이터 생성
    random_bytes = os.urandom(16)
    # UUID 객체로 변환 후 문자열로 반환
    uuid_str = str(uuid.UUID(bytes=random_bytes))
    return uuid_str

def calculate_stock_value(initial_value, turn, news_tag, risk_level, investment_type):
    """뉴스 태그와 투자 성향에 따른 주식 가치 계산"""
    base_change = random.uniform(-0.15, 0.15)  # 기본 변동률
    
    # 뉴스 태그에 따른 영향
    if news_tag == "high" and risk_level == "고위험 고수익":
        base_change += random.uniform(0.05, 0.25)
    elif news_tag == "mid" and risk_level == "중위험 균형형":
        base_change += random.uniform(0.03, 0.15)
    elif news_tag == "all":
        base_change += random.uniform(0.01, 0.08)
    
    # 투자 성향에 따른 변동성 조정
    volatility_multiplier = {
        "안정형": 0.5,
        "안정추구형": 0.7,
        "위험중립형": 1.0,
        "적극투자형": 1.3,
        "공격투자형": 1.6
    }
    
    base_change *= volatility_multiplier.get(investment_type, 1.0)
    
    # 위험도별 기본 변동성
    risk_multiplier = {
        "고위험 고수익": 1.5,
        "중위험 균형형": 1.0,
        "저위험 저수익": 0.6
    }
    
    base_change *= risk_multiplier[risk_level]
    
    new_value = int(initial_value * (1 + base_change))
    return max(50, min(200, new_value))  # 50~200 범위로 제한

def generate_investment_behavior(investment_type, current_point, stock_value, risk_level):
    """투자 성향에 따른 행동 패턴 생성"""
    behaviors = {
        "안정형": {"buy_prob": 0.2, "sell_prob": 0.1, "max_investment": 0.3},
        "안정추구형": {"buy_prob": 0.3, "sell_prob": 0.15, "max_investment": 0.4},
        "위험중립형": {"buy_prob": 0.4, "sell_prob": 0.2, "max_investment": 0.5},
        "적극투자형": {"buy_prob": 0.6, "sell_prob": 0.25, "max_investment": 0.7},
        "공격투자형": {"buy_prob": 0.8, "sell_prob": 0.3, "max_investment": 0.9}
    }
    
    behavior = behaviors[investment_type]
    
    # 거래 결정
    rand = random.random()
    if rand < behavior["buy_prob"]:
        transaction_type = "BUY"
        max_shares = int((current_point * behavior["max_investment"]) / stock_value)
        shares_change = random.randint(1, max(1, max_shares))
        plus_clicks = shares_change
        minus_clicks = 0
    elif rand < behavior["buy_prob"] + behavior["sell_prob"]:
        transaction_type = "SELL"
        shares_change = -random.randint(1, 5)
        plus_clicks = 0
        minus_clicks = abs(shares_change)
    else:
        transaction_type = "KEEP"
        shares_change = 0
        plus_clicks = random.randint(0, 3)
        minus_clicks = random.randint(0, 3)
    
    return transaction_type, shares_change, plus_clicks, minus_clicks

def generate_game_session():
    """하나의 게임 세션 데이터 생성"""
    session_id = generate_binary_id()
    chapter_id = random.choice(CHAPTERS)
    user_id = random.choice(USER_IDS)
    investment_type = random.choice(INVESTMENT_TYPES)
    scenario_id = random.choice(SCENARIO_ID[chapter_id])
    
    # 게임 시작 시간
    base_time = datetime.now() - timedelta(days=random.randint(1, 365))
    
    # 각 종목별 초기 설정
    stock_data = {}
    for risk_level in RISK_LEVELS:
        stock_data[risk_level] = {
            "initial_value": 100,
            "current_value": 100,
            "shares": 0,
            "total_cost": 0
        }
    
    session_documents = []
    current_point = SEED_MONEY[chapter_id]
    
    for turn in range(1, 7):
        # 턴별 뉴스 태그 결정
        news_tag = random.choice(NEWS_TAGS)
        
        # 턴 시작/종료 시간
        turn_start = base_time + timedelta(minutes=random.randint(0, 180))
        turn_duration = random.randint(5, 180)  # 5초~3분
        turn_end = turn_start + timedelta(seconds=turn_duration)
        
        turn_current_point = current_point
        turn_plus_clicks = 0
        turn_minus_clicks = 0
        
        # 각 종목별 문서 생성
        for risk_level in RISK_LEVELS:
            # 이전 가치 저장
            before_value = stock_data[risk_level]["current_value"] if turn > 1 else 0
            
            # 현재 가치 계산
            if turn == 1:
                current_value = 100
            else:
                current_value = calculate_stock_value(
                    stock_data[risk_level]["initial_value"], 
                    turn, news_tag, risk_level, investment_type
                )
            
            stock_data[risk_level]["current_value"] = current_value
            
            # 투자 행동 결정
            transaction_type, shares_change, plus_clicks, minus_clicks = generate_investment_behavior(
                investment_type, turn_current_point, current_value, risk_level
            )
            
            # 주식 수량 및 현금 업데이트
            old_shares = stock_data[risk_level]["shares"]
            new_shares = max(0, old_shares + shares_change)
            
            if transaction_type == "BUY" and shares_change > 0:
                cost = shares_change * current_value
                if cost <= turn_current_point:
                    stock_data[risk_level]["shares"] = new_shares
                    stock_data[risk_level]["total_cost"] += cost
                    turn_current_point -= cost
                else:
                    # 살 수 없는 경우 KEEP으로 변경
                    transaction_type = "KEEP"
                    shares_change = 0
                    new_shares = old_shares
                    plus_clicks = random.randint(0, 3)
                    minus_clicks = random.randint(0, 3)
            elif transaction_type == "SELL" and old_shares > 0:
                sell_shares = min(abs(shares_change), old_shares)
                revenue = sell_shares * current_value
                stock_data[risk_level]["shares"] = old_shares - sell_shares
                turn_current_point += revenue
                new_shares = stock_data[risk_level]["shares"]
            
            # 수익 계산
            if old_shares > 0 and stock_data[risk_level]["total_cost"] > 0:
                avg_cost = stock_data[risk_level]["total_cost"] / old_shares if old_shares > 0 else 0
                income = (old_shares - new_shares) * (current_value - avg_cost) if transaction_type == "SELL" else 0
            else:
                income = 0
            
            # 턴별 공통 값 업데이트 (첫 번째 종목에서만)
            if risk_level == RISK_LEVELS[0]:
                current_point = turn_current_point
                turn_plus_clicks = plus_clicks
                turn_minus_clicks = minus_clicks
            
            # 문서 생성
            document = {
                "_id": generate_binary_id(),
                "investSessionId": session_id,
                "chapterId": chapter_id,
                "scenarioId": scenario_id,
                "userId": user_id,
                "turn": turn,
                "riskLevel": risk_level,
                "currentPoint": current_point,
                "beforeValue": before_value,
                "currentValue": current_value,
                "initialValue": 100,
                "numberOfShares": new_shares,
                "income": int(income),
                "transactionType": transaction_type,
                "plusClick": turn_plus_clicks if risk_level == RISK_LEVELS[0] else 0,
                "minusClick": turn_minus_clicks if risk_level == RISK_LEVELS[0] else 0,
                "startedAt": {"$date": turn_start.isoformat() + "Z"},
                "endedAt": {"$date": turn_end.isoformat() + "Z"},
                "_class": "com.popoworld.backend.invest.entity.InvestHistory",
                "newsTag": news_tag
            }
            
            session_documents.append(document)
        
        base_time = turn_end
    
    return session_documents

def generate_all_data():
    """전체 더미 데이터 생성"""
    all_documents = []
    
    print("더미 데이터 생성 중...")
    
    for i in range(8050):
        if i % 500 == 0:
            print(f"진행률: {i}/8050 ({i/8050*100:.1f}%)")
        
        session_docs = generate_game_session()
        all_documents.extend(session_docs)
    
    print(f"총 {len(all_documents)}개의 문서 생성 완료")
    return all_documents

# 데이터 생성 및 저장
dummy_data = generate_all_data()

# JSON 파일로 저장
output_filename = ".\data\investment_game_dummy_data.json"
with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(dummy_data, f, ensure_ascii=False, indent=2)

print(f"더미 데이터가 '{output_filename}' 파일로 저장되었습니다.")
print(f"총 문서 수: {len(dummy_data)}")
print(f"파일 크기: {os.path.getsize(output_filename) / (1024*1024):.2f} MB")
