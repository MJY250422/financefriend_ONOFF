"""
event_id 컬럼명 변경 테스트 스크립트
"""
import requests
from datetime import datetime

# 배포된 백엔드 URL
BASE_URL = "https://financefriend-onoff-backend.onrender.com/api/v1"

print("🧪 event_id 변경 테스트 시작...\n")

# 1. 헬스체크
print("1️⃣ 백엔드 헬스체크...")
health = requests.get(f"{BASE_URL.replace('/api/v1', '')}/health", timeout=10)
print(f"   상태: {health.json()}\n")

# 2. 이벤트 로그 생성 (session_id 없이 테스트)
print("2️⃣ 이벤트 로그 생성...")
event_data = {
    "event_time": datetime.utcnow().isoformat(),
    "event_name": "test_event_id_rename",
    "surface": "test",
    "source": "api_test",
    "payload": {"test": "event_id rename test"}
}

try:
    response = requests.post(f"{BASE_URL}/event-logs/", json=event_data, timeout=10)
    if response.status_code == 201:
        result = response.json()
        print(f"   ✅ 생성 성공!")
        print(f"   event_id: {result.get('event_id')}")  # id가 아닌 event_id로 반환되는지 확인
        print(f"   event_name: {result.get('event_name')}\n")
        
        event_id = result.get('event_id')
        
        # 3. 생성된 이벤트 조회
        print(f"3️⃣ 생성된 이벤트 조회 (event_id={event_id})...")
        get_response = requests.get(f"{BASE_URL}/event-logs/{event_id}", timeout=10)
        if get_response.status_code == 200:
            event = get_response.json()
            print(f"   ✅ 조회 성공!")
            print(f"   event_id: {event.get('event_id')}")
            print(f"   event_name: {event.get('event_name')}\n")
        else:
            print(f"   ❌ 조회 실패: {get_response.status_code}")
        
        # 4. 삭제
        print(f"4️⃣ 테스트 이벤트 삭제...")
        delete_response = requests.delete(f"{BASE_URL}/event-logs/{event_id}", timeout=10)
        if delete_response.status_code == 204:
            print(f"   ✅ 삭제 성공!\n")
        else:
            print(f"   ❌ 삭제 실패: {delete_response.status_code}\n")
            
    else:
        print(f"   ❌ 생성 실패: {response.status_code}")
        print(f"   에러: {response.text}\n")
        
except Exception as e:
    print(f"   ❌ 에러 발생: {e}\n")

print("✅ 테스트 완료!")
print("\n만약 모든 테스트가 통과했다면:")
print("   → event_logs.id → event_id 변경 성공! 🎉")

