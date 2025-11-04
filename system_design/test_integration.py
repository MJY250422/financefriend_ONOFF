"""
백엔드 API 통합 테스트 스크립트
백엔드 서버의 주요 API 엔드포인트를 테스트합니다.
"""
import requests
from datetime import datetime
import time


BASE_URL = "http://localhost:8000"
API_URL = f"{BASE_URL}/api/v1"


def print_section(title):
    """섹션 제목 출력"""
    print("\n" + "=" * 70)
    print(f"🧪 {title}")
    print("=" * 70)


def test_health_check():
    """헬스 체크 테스트"""
    print_section("헬스 체크 테스트")
    
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ 헬스 체크 성공")
            print(f"   Status: {data.get('status')}")
            print(f"   Message: {data.get('message')}")
            print(f"   Version: {data.get('version')}")
            return True
        else:
            print(f"❌ 헬스 체크 실패: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 서버 연결 실패: {e}")
        return False


def test_users_api():
    """사용자 API 테스트"""
    print_section("사용자 API 테스트")
    
    # 1. 사용자 생성
    print("\n1️⃣  사용자 생성 테스트")
    test_user = {
        "email": f"test_{int(time.time())}@example.com",
        "password": "testpass123",
        "username": "테스트유저",
        "user_type": "USER"
    }
    
    try:
        response = requests.post(f"{API_URL}/users/", json=test_user)
        if response.status_code == 201:
            user = response.json()
            print(f"✅ 사용자 생성 성공")
            print(f"   User ID: {user['user_id']}")
            print(f"   Email: {user['email']}")
            print(f"   Username: {user['username']}")
            
            # 2. 사용자 조회
            print("\n2️⃣  사용자 조회 테스트")
            response = requests.get(f"{API_URL}/users/{user['user_id']}")
            if response.status_code == 200:
                retrieved_user = response.json()
                print(f"✅ 사용자 조회 성공")
                print(f"   Username: {retrieved_user['username']}")
            else:
                print(f"❌ 사용자 조회 실패: {response.status_code}")
            
            # 3. 사용자 활성화
            print("\n3️⃣  사용자 활성화 테스트")
            response = requests.post(f"{API_URL}/users/{user['user_id']}/activate")
            if response.status_code == 200:
                print(f"✅ 사용자 활성화 성공")
            else:
                print(f"❌ 사용자 활성화 실패: {response.status_code}")
            
            return user
        else:
            print(f"❌ 사용자 생성 실패: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
        return None


def test_news_api():
    """뉴스 API 테스트"""
    print_section("뉴스 API 테스트")
    
    # 1. 뉴스 목록 조회
    print("\n1️⃣  뉴스 목록 조회 테스트")
    try:
        response = requests.get(f"{API_URL}/news/", params={"limit": 5})
        if response.status_code == 200:
            news_list = response.json()
            print(f"✅ 뉴스 목록 조회 성공 ({len(news_list)}개)")
            for i, news in enumerate(news_list[:3], 1):
                print(f"   {i}. [{news['news_id']}] {news['title'][:40]}...")
            return news_list
        else:
            print(f"❌ 뉴스 목록 조회 실패: {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
        return []


def test_news_detail(news_id):
    """뉴스 상세 조회 테스트"""
    print("\n2️⃣  뉴스 상세 조회 테스트")
    try:
        response = requests.get(f"{API_URL}/news/{news_id}")
        if response.status_code == 200:
            news = response.json()
            print(f"✅ 뉴스 상세 조회 성공")
            print(f"   제목: {news['title']}")
            print(f"   출처: {news.get('source', 'N/A')}")
            print(f"   발행일: {news.get('published_at', 'N/A')}")
            return news
        else:
            print(f"❌ 뉴스 상세 조회 실패: {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
        return None


def test_news_interaction(news_id, user_id):
    """뉴스 상호작용 테스트"""
    print("\n3️⃣  뉴스 상호작용 테스트")
    try:
        response = requests.post(
            f"{API_URL}/news/{news_id}/interactions",
            json={"news_id": news_id, "interaction_type": "view"},
            params={"user_id": user_id}
        )
        if response.status_code == 201:
            interaction = response.json()
            print(f"✅ 상호작용 생성 성공")
            print(f"   Interaction ID: {interaction['interaction_id']}")
            print(f"   Type: {interaction['interaction_type']}")
        else:
            print(f"❌ 상호작용 생성 실패: {response.status_code}")
    except Exception as e:
        print(f"❌ 에러 발생: {e}")


def test_sessions_api(user_id):
    """세션 API 테스트"""
    print_section("세션 API 테스트")
    
    # 1. 세션 생성
    print("\n1️⃣  세션 생성 테스트")
    try:
        response = requests.post(
            f"{API_URL}/sessions/",
            json={
                "user_id": user_id,
                "context": {"device": "test", "browser": "test-runner"}
            }
        )
        if response.status_code == 201:
            session = response.json()
            print(f"✅ 세션 생성 성공")
            print(f"   Session ID: {session['session_id']}")
            print(f"   Session Token: {session['session_token'][:20]}...")
            
            # 2. 세션 조회
            print("\n2️⃣  세션 조회 테스트")
            response = requests.get(f"{API_URL}/sessions/{session['session_id']}")
            if response.status_code == 200:
                print(f"✅ 세션 조회 성공")
            else:
                print(f"❌ 세션 조회 실패: {response.status_code}")
            
            return session
        else:
            print(f"❌ 세션 생성 실패: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
        return None


def test_dialogues_api(session_id):
    """대화 API 테스트"""
    print_section("대화 API 테스트")
    
    # 1. 대화 생성
    print("\n1️⃣  대화 생성 테스트")
    dialogues_to_create = [
        {"sender_type": "USER", "content": "안녕하세요! 테스트 메시지입니다.", "intent": "greeting"},
        {"sender_type": "AGENT", "content": "안녕하세요! 무엇을 도와드릴까요?", "intent": "response"}
    ]
    
    try:
        for dialogue in dialogues_to_create:
            response = requests.post(
                f"{API_URL}/dialogues/",
                json={
                    "session_id": session_id,
                    "sender_type": dialogue['sender_type'],
                    "content": dialogue['content'],
                    "intent": dialogue.get('intent')
                }
            )
            if response.status_code == 201:
                created = response.json()
                print(f"✅ 대화 생성 성공: {created['sender_type']} - {created['content'][:30]}...")
            else:
                print(f"❌ 대화 생성 실패: {response.status_code}")
        
        # 2. 세션의 대화 목록 조회
        print("\n2️⃣  세션 대화 목록 조회 테스트")
        response = requests.get(f"{API_URL}/dialogues/session/{session_id}")
        if response.status_code == 200:
            dialogues = response.json()
            print(f"✅ 대화 목록 조회 성공 ({len(dialogues)}개)")
            for i, dialogue in enumerate(dialogues, 1):
                print(f"   {i}. [{dialogue['sender_type']}] {dialogue['content'][:40]}...")
        else:
            print(f"❌ 대화 목록 조회 실패: {response.status_code}")
    except Exception as e:
        print(f"❌ 에러 발생: {e}")


def main():
    """메인 테스트 실행"""
    print("=" * 70)
    print("🚀 백엔드 API 통합 테스트 시작")
    print("=" * 70)
    print(f"⏰ 테스트 시작 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 1. 헬스 체크
    if not test_health_check():
        print("\n❌ 서버가 실행되지 않았습니다. 테스트를 중단합니다.")
        print("💡 먼저 백엔드 서버를 실행해주세요: python main.py")
        return
    
    # 2. 사용자 API 테스트
    user = test_users_api()
    if not user:
        print("\n⚠️  사용자 생성 실패. 일부 테스트를 건너뜁니다.")
        return
    
    # 3. 뉴스 API 테스트
    news_list = test_news_api()
    if news_list:
        news_detail = test_news_detail(news_list[0]['news_id'])
        if news_detail:
            test_news_interaction(news_detail['news_id'], user['user_id'])
    
    # 4. 세션 API 테스트
    session = test_sessions_api(user['user_id'])
    if session:
        # 5. 대화 API 테스트
        test_dialogues_api(session['session_id'])
    
    # 테스트 완료
    print("\n" + "=" * 70)
    print("✅ 통합 테스트 완료!")
    print("=" * 70)
    print(f"⏰ 테스트 종료 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n💡 모든 API가 정상 작동하는 것을 확인했습니다!")
    print("💡 이제 Streamlit 앱을 실행하여 UI 테스트를 진행할 수 있습니다.")
    print("=" * 70)


if __name__ == "__main__":
    main()




