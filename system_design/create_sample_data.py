"""
테스트용 샘플 데이터 생성 스크립트
백엔드 API를 사용하여 테스트 데이터를 생성합니다.
"""
import requests
from datetime import datetime, timedelta
import random


BASE_URL = "http://localhost:8000/api/v1"


def create_sample_users():
    """샘플 사용자 생성"""
    print("📝 Creating sample users...")
    
    users = [
        {
            "email": "user1@example.com",
            "password": "password123",
            "username": "김철수",
            "user_type": "USER"
        },
        {
            "email": "user2@example.com",
            "password": "password123",
            "username": "이영희",
            "user_type": "USER"
        },
        {
            "email": "admin@example.com",
            "password": "admin123!",
            "username": "관리자",
            "user_type": "ADMIN"
        }
    ]
    
    created_users = []
    for user in users:
        try:
            response = requests.post(f"{BASE_URL}/users/", json=user)
            if response.status_code == 201:
                created_user = response.json()
                created_users.append(created_user)
                print(f"✅ User created: {created_user['email']} (ID: {created_user['user_id']})")
            elif response.status_code == 400:
                print(f"⚠️  User already exists: {user['email']}")
                # 기존 사용자 가져오기
                response = requests.get(f"{BASE_URL}/users/")
                if response.status_code == 200:
                    all_users = response.json()
                    existing = next((u for u in all_users if u['email'] == user['email']), None)
                    if existing:
                        created_users.append(existing)
            else:
                print(f"❌ Failed to create user: {user['email']} - {response.text}")
        except Exception as e:
            print(f"❌ Error creating user {user['email']}: {e}")
    
    return created_users


def create_sample_news():
    """샘플 뉴스 생성"""
    print("\n📰 Creating sample news...")
    
    news_items = [
        {
            "title": "한국은행, 기준금리 3.5% 동결...물가 안정 우선",
            "url": "https://example.com/news/1",
            "content": "한국은행 금융통화위원회가 기준금리를 3.5%로 동결했습니다. 이창용 한국은행 총재는 물가 안정을 최우선 과제로 삼고 있다고 밝혔습니다.",
            "source": "연합뉴스",
            "published_at": (datetime.now() - timedelta(hours=2)).isoformat()
        },
        {
            "title": "삼성전자, 3분기 배당금 30% 증액 발표",
            "url": "https://example.com/news/2",
            "content": "삼성전자가 3분기 배당금을 전년 대비 30% 증액한다고 발표했습니다. 주주 가치 제고를 위한 조치로 풀이됩니다.",
            "source": "매일경제",
            "published_at": (datetime.now() - timedelta(hours=5)).isoformat()
        },
        {
            "title": "원/달러 환율 1,300원 돌파...수출기업 수혜 예상",
            "url": "https://example.com/news/3",
            "content": "원/달러 환율이 1,300원을 돌파하며 연중 최고치를 기록했습니다. 수출 기업들의 실적 개선이 예상됩니다.",
            "source": "한국경제",
            "published_at": (datetime.now() - timedelta(hours=1)).isoformat()
        },
        {
            "title": "코스피, 외국인 매수에 2,500선 회복",
            "url": "https://example.com/news/4",
            "content": "코스피 지수가 외국인의 순매수에 힘입어 2,500선을 회복했습니다. 기술주와 금융주가 강세를 보였습니다.",
            "source": "이데일리",
            "published_at": (datetime.now() - timedelta(hours=3)).isoformat()
        },
        {
            "title": "정부, 부동산 규제 완화 추진...주택 공급 확대",
            "url": "https://example.com/news/5",
            "content": "정부가 부동산 규제 완화를 통한 주택 공급 확대 방안을 추진합니다. 재건축·재개발 규제 완화가 핵심입니다.",
            "source": "조선일보",
            "published_at": (datetime.now() - timedelta(hours=6)).isoformat()
        },
        {
            "title": "현대차, 전기차 신모델 출시로 점유율 상승 기대",
            "url": "https://example.com/news/6",
            "content": "현대자동차가 신형 전기차 모델을 출시하며 전기차 시장 점유율 상승을 기대하고 있습니다.",
            "source": "서울경제",
            "published_at": (datetime.now() - timedelta(hours=4)).isoformat()
        },
        {
            "title": "SK하이닉스, AI 반도체 수요 증가로 실적 호조",
            "url": "https://example.com/news/7",
            "content": "SK하이닉스가 AI 반도체 수요 증가에 힘입어 양호한 실적을 기록했습니다. HBM 제품 매출이 크게 증가했습니다.",
            "source": "전자신문",
            "published_at": (datetime.now() - timedelta(hours=7)).isoformat()
        },
        {
            "title": "금융위, 가상자산 규제 강화 방안 발표",
            "url": "https://example.com/news/8",
            "content": "금융위원회가 가상자산 투자자 보호를 위한 규제 강화 방안을 발표했습니다. 거래소 인가제가 도입됩니다.",
            "source": "파이낸셜뉴스",
            "published_at": (datetime.now() - timedelta(hours=8)).isoformat()
        },
        {
            "title": "KB금융, 디지털 전환 가속화로 비대면 서비스 확대",
            "url": "https://example.com/news/9",
            "content": "KB금융그룹이 디지털 전환을 가속화하며 비대면 금융 서비스를 확대하고 있습니다.",
            "source": "뉴스핌",
            "published_at": (datetime.now() - timedelta(hours=9)).isoformat()
        },
        {
            "title": "네이버, 클라우드 사업 본격화...B2B 시장 공략",
            "url": "https://example.com/news/10",
            "content": "네이버가 클라우드 사업을 본격화하며 B2B 시장 공략에 나섰습니다. AI 기술 접목이 핵심 전략입니다.",
            "source": "디지털타임스",
            "published_at": (datetime.now() - timedelta(hours=10)).isoformat()
        }
    ]
    
    created_news = []
    for news in news_items:
        try:
            response = requests.post(f"{BASE_URL}/news/", json=news)
            if response.status_code == 201:
                created = response.json()
                created_news.append(created)
                print(f"✅ News created: {created['title'][:50]}... (ID: {created['news_id']})")
            elif response.status_code == 400:
                print(f"⚠️  News already exists: {news['title'][:50]}...")
            else:
                print(f"❌ Failed to create news: {news['title'][:50]}... - {response.text}")
        except Exception as e:
            print(f"❌ Error creating news: {e}")
    
    return created_news


def create_sample_interactions(users, news_items):
    """샘플 상호작용 생성"""
    print("\n💬 Creating sample interactions...")
    
    interaction_types = ["click", "view", "like", "share"]
    
    created_interactions = 0
    for user in users[:2]:  # 처음 2명의 사용자만
        # 각 사용자가 무작위로 3-7개의 뉴스와 상호작용
        num_interactions = random.randint(3, 7)
        selected_news = random.sample(news_items, min(num_interactions, len(news_items)))
        
        for news in selected_news:
            interaction_type = random.choice(interaction_types)
            try:
                response = requests.post(
                    f"{BASE_URL}/news/{news['news_id']}/interactions",
                    json={"news_id": news['news_id'], "interaction_type": interaction_type},
                    params={"user_id": user['user_id']}
                )
                if response.status_code == 201:
                    created_interactions += 1
                    print(f"✅ Interaction created: {user['username']} {interaction_type} news #{news['news_id']}")
            except Exception as e:
                print(f"❌ Error creating interaction: {e}")
    
    print(f"\n✨ Total interactions created: {created_interactions}")


def create_sample_sessions(users):
    """샘플 세션 생성"""
    print("\n🔐 Creating sample sessions...")
    
    created_sessions = []
    for user in users:
        try:
            response = requests.post(
                f"{BASE_URL}/sessions/",
                json={
                    "user_id": user['user_id'],
                    "context": {"device": "web", "browser": "chrome"}
                }
            )
            if response.status_code == 201:
                session = response.json()
                created_sessions.append(session)
                print(f"✅ Session created for {user['username']} (ID: {session['session_id']})")
        except Exception as e:
            print(f"❌ Error creating session: {e}")
    
    return created_sessions


def create_sample_dialogues(sessions):
    """샘플 대화 생성"""
    print("\n💭 Creating sample dialogues...")
    
    sample_conversations = [
        [
            {"sender_type": "USER", "content": "안녕하세요! 오늘 주요 금융 뉴스를 알려주세요.", "intent": "greeting"},
            {"sender_type": "AGENT", "content": "안녕하세요! 오늘의 주요 금융 뉴스를 요약해드리겠습니다. 한국은행이 기준금리를 3.5%로 동결했고, 삼성전자는 배당금을 30% 증액한다고 발표했습니다.", "intent": "response"},
            {"sender_type": "USER", "content": "원/달러 환율이 많이 올랐다고 하던데요?", "intent": "question"},
            {"sender_type": "AGENT", "content": "네, 맞습니다. 원/달러 환율이 1,300원을 돌파하며 연중 최고치를 기록했습니다. 이는 수출 기업들에게 긍정적인 영향을 줄 것으로 예상됩니다.", "intent": "response"}
        ],
        [
            {"sender_type": "USER", "content": "삼성전자 주식 전망이 어떤가요?", "intent": "question"},
            {"sender_type": "AGENT", "content": "삼성전자는 최근 배당금을 30% 증액한다고 발표했습니다. 이는 주주 가치 제고를 위한 긍정적인 신호로 해석됩니다.", "intent": "response"}
        ]
    ]
    
    created_dialogues = 0
    for i, session in enumerate(sessions[:2]):  # 처음 2개 세션에만
        if i < len(sample_conversations):
            for dialogue in sample_conversations[i]:
                try:
                    response = requests.post(
                        f"{BASE_URL}/dialogues/",
                        json={
                            "session_id": session['session_id'],
                            "sender_type": dialogue['sender_type'],
                            "content": dialogue['content'],
                            "intent": dialogue.get('intent')
                        }
                    )
                    if response.status_code == 201:
                        created_dialogues += 1
                        print(f"✅ Dialogue created: {dialogue['sender_type']} - {dialogue['content'][:30]}...")
                except Exception as e:
                    print(f"❌ Error creating dialogue: {e}")
    
    print(f"\n✨ Total dialogues created: {created_dialogues}")


def main():
    """메인 함수"""
    print("=" * 70)
    print("🚀 샘플 데이터 생성 시작")
    print("=" * 70)
    
    # 백엔드 서버 연결 확인
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print("✅ 백엔드 서버 연결 성공\n")
        else:
            print("❌ 백엔드 서버 응답 이상")
            return
    except Exception as e:
        print(f"❌ 백엔드 서버에 연결할 수 없습니다: {e}")
        print("💡 먼저 백엔드 서버를 실행해주세요: python main.py")
        return
    
    # 샘플 데이터 생성
    users = create_sample_users()
    news_items = create_sample_news()
    
    if news_items and users:
        create_sample_interactions(users, news_items)
    
    if users:
        sessions = create_sample_sessions(users)
        if sessions:
            create_sample_dialogues(sessions)
    
    print("\n" + "=" * 70)
    print("✨ 샘플 데이터 생성 완료!")
    print("=" * 70)
    print("\n📊 생성된 데이터:")
    print(f"   - 사용자: {len(users)}명")
    print(f"   - 뉴스: {len(news_items)}개")
    print(f"   - 세션: {len(sessions) if 'sessions' in locals() else 0}개")
    print("\n💡 이제 Streamlit 앱에서 데이터를 확인할 수 있습니다!")
    print("=" * 70)


if __name__ == "__main__":
    main()


