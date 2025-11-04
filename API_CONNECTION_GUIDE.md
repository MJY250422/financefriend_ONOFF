# API 연결 가이드 - FinanceFriend Backend

> **팀원용 API 연동 가이드**  
> 작성일: 2025.11.04  
> Backend 버전: 1.0.0

---

## 📋 기본 정보

### Base URL
```
http://localhost:8000 (로컬 개발)
```

### API 문서
```
http://localhost:8000/docs (Swagger UI)
http://localhost:8000/redoc (ReDoc)
```

### 데이터베이스
- **현재**: Supabase PostgreSQL (팀 협업용)
- **이전**: SQLite (로컬 개발, 더 이상 사용 안 함)
- **장점**: 팀원 모두 같은 데이터 공유, 동시 접속 가능

### 인증 정보
- **현재 상태**: 인증 없음 (개발 단계)
- **추후 계획**: JWT Bearer Token 방식 예정

---

## 🔗 API 엔드포인트 목록

### 1. 뉴스 상호작용 (`user_news_interactions` 테이블)

#### ✅ 엔드포인트
```
POST /api/v1/news/{news_id}/interactions?user_id={user_id}
```

#### 📝 요청 예시
```json
POST /api/v1/news/123/interactions?user_id=550e8400-e29b-41d4-a716-446655440000

Body:
{
  "interaction_type": "click"
}
```

#### ✅ 성공 응답 (201 Created)
```json
{
  "interaction_id": 1,
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "news_id": 123,
  "interaction_type": "click",
  "created_at": "2025-11-04T12:00:00"
}
```

#### ❌ 에러 응답
```json
// 404 Not Found - 뉴스가 없을 때
{
  "detail": "News not found"
}

// 422 Validation Error - 잘못된 타입
{
  "detail": [
    {
      "loc": ["body", "interaction_type"],
      "msg": "value is not a valid enumeration member",
      "type": "type_error.enum"
    }
  ]
}
```

#### 필수 필드
- ✅ `news_id` (path parameter, integer)
- ✅ `user_id` (query parameter, string UUID)
- ✅ `interaction_type` (body, enum: "click", "view", "share", "like", "bookmark", "comment")

---

### 2. 챗봇 대화 (`dialogues` 테이블)

#### ✅ 엔드포인트
```
POST /api/v1/dialogues/
```

#### 📝 요청 예시
```json
POST /api/v1/dialogues/

Body:
{
  "session_id": 1,
  "sender_type": "user",
  "content": "양적완화가 뭐야?",
  "intent": "question"
}
```

#### ✅ 성공 응답 (201 Created)
```json
{
  "dialogue_id": 789,
  "session_id": 1,
  "sender_type": "user",
  "content": "양적완화가 뭐야?",
  "intent": "question",
  "created_at": "2025-11-04T12:00:00"
}
```

#### ❌ 에러 응답
```json
// 404 Not Found - 세션이 없을 때
{
  "detail": "Session not found"
}
```

#### 필수 필드
- ✅ `session_id` (integer) - **반드시 먼저 세션을 생성해야 함**
- ✅ `sender_type` (enum: "user", "assistant", "system")
- ✅ `content` (string) - 메시지 내용

#### 선택 필드
- ⭕ `intent` (string, max 50자) - 의도 분류 (예: "question", "greeting", "feedback")

---

### 3. 에이전트 작업 (`agent_tasks` 테이블)

#### ✅ 엔드포인트
```
POST /api/v1/agent-tasks/
```

#### 📝 요청 예시
```json
POST /api/v1/agent-tasks/

Body:
{
  "agent_id": 1,
  "session_id": 1,
  "dialogue_id": 789,
  "input_data": {
    "message": "양적완화가 뭐야?",
    "context": "news_detail"
  }
}
```

#### ✅ 성공 응답 (201 Created)
```json
{
  "task_id": 456,
  "agent_id": 1,
  "session_id": 1,
  "dialogue_id": 789,
  "input_data": {
    "message": "양적완화가 뭐야?",
    "context": "news_detail"
  },
  "output_data": null,
  "status": "pending",
  "error_reason": null,
  "duration_ms": null,
  "created_at": "2025-11-04T12:00:00"
}
```

#### 작업 완료 시 업데이트
```json
POST /api/v1/agent-tasks/456/complete

Body:
{
  "output_data": {
    "answer": "양적완화는...",
    "answer_len": 150,
    "via": "openai"
  },
  "duration_ms": 1500
}
```

#### 필수 필드
- ✅ `agent_id` (integer) - 에이전트 ID
- ✅ `session_id` (integer)
- ✅ `status` (자동 설정: "pending")

#### 선택 필드
- ⭕ `dialogue_id` (integer) - 연결된 대화 ID
- ⭕ `input_data` (JSON object)
- ⭕ `output_data` (JSON object) - 작업 완료 시 저장
- ⭕ `duration_ms` (integer) - 실행 시간

---

### 4. 세션 관리 (`sessions` 테이블)

#### ✅ 세션 생성
```
POST /api/v1/sessions/
```

#### 📝 요청 예시
```json
POST /api/v1/sessions/

Body:
{
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "context": {
    "surface": "home",
    "device": "desktop"
  }
}
```

#### ✅ 성공 응답 (201 Created)
```json
{
  "session_id": 1,
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "session_token": "abc123...",
  "created_at": "2025-11-04T12:00:00",
  "expires_at": "2025-11-05T12:00:00",
  "context": {
    "surface": "home",
    "device": "desktop"
  }
}
```

#### ✅ 세션 컨텍스트 업데이트 (부분 업데이트)
```
PUT /api/v1/sessions/{session_id}/context
```

#### 📝 요청 예시
```json
PUT /api/v1/sessions/1/context

Body:
{
  "surface": "news_detail",
  "source": "news_list",
  "term": "양적완화",
  "click_count": 5,
  "scroll_depth": 75.5,
  "view_duration": 120.5
}
```

**⚠️ 중요: 이 엔드포인트는 context를 완전히 교체합니다 (전체 교체)**

#### 필수 필드
- ✅ `user_id` (string UUID)

#### 선택 필드
- ⭕ `context` (JSON object) - 자유 형식

---

### 5. 복합 이벤트 처리

**❌ 현재 통합 엔드포인트 없음**

여러 테이블을 동시에 업데이트하려면 순차적으로 API를 호출해야 합니다.

#### 예시: 챗봇 응답 시 필요한 API 호출 순서
```
1. POST /api/v1/dialogues/          (사용자 메시지 저장)
2. POST /api/v1/agent-tasks/        (에이전트 작업 생성)
3. POST /api/v1/agent-tasks/{id}/complete  (작업 완료)
4. POST /api/v1/dialogues/          (AI 응답 저장)
```

---

### 6. 배치 전송

**❌ 현재 배치 전송 엔드포인트 없음**

각 이벤트는 개별 API 호출로 전송해야 합니다.

**추천**: 중요도가 낮은 이벤트(스크롤, 체류시간 등)는 로컬에 모아두었다가 주기적으로 전송하는 것을 고려하세요.

---

## 🔄 데이터 타입 변환 가이드

### 1. Session ID 변환

**문제점**:
- Streamlit: `session_id`는 STRING (UUID 형식)
- 서버 DB: `session_id`는 INTEGER

**해결책**:
1. 세션 생성 시 서버가 반환한 `session_id` (integer)를 저장
2. Streamlit의 `st.session_state`에 매핑 테이블 관리:
   ```python
   st.session_state["backend_session_id"] = 1  # 서버에서 받은 integer
   st.session_state["session_id"] = "uuid..."  # Streamlit 내부용
   ```

### 2. News ID 변환

**문제점**:
- Streamlit: `news_id`는 STRING (예: "news001")
- 서버 DB: `news_id`는 INTEGER

**해결책**:
- 서버에서 뉴스 목록을 가져올 때 받은 `news_id` (integer)를 그대로 사용
- 예: `GET /api/v1/news/` → `news_id: 1, 2, 3...`

### 3. 익명 사용자 처리

**문제점**:
- 로그인 전 사용자는 `user_id: "anon"`으로 표시

**해결책**:
1. **방법 1 (권장)**: 익명 사용자를 서버에 먼저 생성
   ```json
   POST /api/v1/users/
   {
     "email": "anon_<uuid>@temp.local",
     "password": "temporary_password",
     "username": "익명 사용자",
     "user_type": "guest"
   }
   ```
   → 반환된 `user_id` (UUID)를 사용

2. **방법 2**: 백엔드에 익명 사용자용 디폴트 UUID 사전 생성
   - 예: `00000000-0000-0000-0000-000000000000`

### 4. Agent ID 매핑

**문제점**:
- Streamlit: `via: "openai"` (문자열)
- 서버: `agent_id` (integer)

**해결책**:
1. 서버에 에이전트 정보 사전 등록 필요 (현재 API 없음)
2. **임시 방안**: 하드코딩 매핑
   ```python
   AGENT_MAPPING = {
       "openai": 1,
       "claude": 2,
       "local": 3
   }
   ```

**⚠️ 주의**: 실제로는 `GET /api/v1/agents/` 같은 엔드포인트가 필요함 (현재 미구현)

---

## 📊 이벤트 타입 매핑 규칙

### Streamlit 이벤트 → 서버 interaction_type

| Streamlit 이벤트 | 서버 interaction_type | 저장 위치 |
|-----------------|---------------------|---------|
| `news_click` | `click` | `user_news_interactions` |
| `news_view` | `view` | `user_news_interactions` |
| `news_share` | `share` | `user_news_interactions` |
| `news_like` | `like` | `user_news_interactions` |
| `news_bookmark` | `bookmark` | `user_news_interactions` |
| `chat_question` | N/A | `dialogues` (sender_type: "user") |
| `chat_answer` | N/A | `dialogues` (sender_type: "assistant") |
| `scroll_depth` | N/A | `sessions.context` JSON |
| `view_duration` | N/A | `sessions.context` JSON |

### 가용한 Enum 값

#### InteractionType
```python
"click", "view", "share", "like", "bookmark", "comment"
```

#### SenderType
```python
"user", "assistant", "system"
```

#### TaskStatus
```python
"pending", "in_progress", "completed", "failed", "cancelled"
```

#### UserType
```python
"admin", "user", "guest", "premium"
```

---

## ⚡ 추천 구현 패턴

### 패턴 1: 뉴스 클릭 이벤트
```python
import requests

def log_news_click(user_id: str, news_id: int):
    response = requests.post(
        f"http://localhost:8000/api/v1/news/{news_id}/interactions",
        params={"user_id": user_id},
        json={"interaction_type": "click"}
    )
    if response.status_code == 201:
        print("✅ 상호작용 저장 완료")
    else:
        print(f"❌ 에러: {response.json()}")
```

### 패턴 2: 챗봇 대화 저장
```python
def save_chat_message(session_id: int, is_user: bool, content: str):
    sender_type = "user" if is_user else "assistant"
    
    response = requests.post(
        "http://localhost:8000/api/v1/dialogues/",
        json={
            "session_id": session_id,
            "sender_type": sender_type,
            "content": content,
            "intent": "question" if is_user else None
        }
    )
    return response.json() if response.status_code == 201 else None
```

### 패턴 3: 세션 컨텍스트 업데이트
```python
def update_session_context(session_id: int, **kwargs):
    """
    예시:
    update_session_context(
        session_id=1,
        surface="news_detail",
        scroll_depth=75.5,
        view_duration=120.5
    )
    """
    response = requests.put(
        f"http://localhost:8000/api/v1/sessions/{session_id}/context",
        json=kwargs
    )
    return response.status_code == 200
```

---

## 🔧 트랜잭션 및 에러 처리

### 트랜잭션
- ✅ 각 API 호출은 독립적인 트랜잭션
- ❌ 여러 테이블 동시 업데이트 시 트랜잭션 보장 안 됨
- **권장**: 중요한 작업은 순차적으로 호출하고, 실패 시 로직으로 롤백 처리

### 재시도 정책
- **재시도 권장**: 5xx 에러, 네트워크 에러
- **재시도 비권장**: 4xx 에러 (클라이언트 오류)
- **재시도 횟수**: 최대 3회
- **재시도 간격**: 1초, 2초, 4초 (exponential backoff)

### 에러 응답 형식
```json
// FastAPI 기본 에러
{
  "detail": "에러 메시지"
}

// Validation 에러
{
  "detail": [
    {
      "loc": ["body", "field_name"],
      "msg": "error message",
      "type": "error_type"
    }
  ]
}
```

---

## 🚀 세션 생성 플로우

### 앱 시작 시
```python
# 1. 사용자 ID 확인 (로그인 or 익명)
if not st.session_state.get("user_id"):
    # 익명 사용자 생성 또는 기본값 사용
    user_id = "00000000-0000-0000-0000-000000000000"
else:
    user_id = st.session_state["user_id"]

# 2. 세션 생성
response = requests.post(
    "http://localhost:8000/api/v1/sessions/",
    json={"user_id": user_id}
)

if response.status_code == 201:
    session_data = response.json()
    st.session_state["backend_session_id"] = session_data["session_id"]
    st.session_state["session_token"] = session_data["session_token"]
```

---

## 📝 필수/선택 필드 요약

### user_news_interactions
- **필수**: `user_id`, `news_id`, `interaction_type`
- **자동**: `interaction_id`, `created_at`

### dialogues
- **필수**: `session_id`, `sender_type`, `content`
- **선택**: `intent`
- **자동**: `dialogue_id`, `created_at`

### agent_tasks
- **필수**: `agent_id`, `session_id`
- **선택**: `dialogue_id`, `input_data`, `output_data`, `duration_ms`
- **자동**: `task_id`, `status` (default: "pending"), `created_at`

### sessions
- **필수**: `user_id`
- **선택**: `context`
- **자동**: `session_id`, `session_token`, `created_at`, `expires_at`

---

## ⚠️ 현재 제약사항 및 누락된 기능

### 1. Agent Info API 없음
- **문제**: 에이전트 정보를 조회하거나 생성하는 API가 없음
- **임시 해결**: `agent_id`를 하드코딩 (예: 1, 2, 3...)
- **TODO**: 백엔드에 Agent Info CRUD API 추가 필요

### 2. 배치 전송 미지원
- **문제**: 여러 이벤트를 한 번에 보낼 수 없음
- **임시 해결**: 개별 API 호출
- **TODO**: 배치 엔드포인트 추가 고려

### 3. 인증 시스템 미구현
- **문제**: API 키나 토큰 없이 누구나 접근 가능
- **임시 해결**: 로컬 개발 환경이므로 OK
- **TODO**: JWT 인증 추가 필요

### 4. Rate Limiting 없음
- **현재**: 무제한 요청 가능
- **TODO**: 프로덕션 시 Rate Limiting 필요

---

## 📚 추가 유용한 API

### 뉴스 목록 조회
```
GET /api/v1/news/?skip=0&limit=20
```

### 사용자 상호작용 이력 조회
```
GET /api/v1/news/user/{user_id}/interactions?skip=0&limit=50
```

### 세션 대화 이력 조회
```
GET /api/v1/dialogues/session/{session_id}/history?limit=50
```

### 인기 뉴스 조회
```
GET /api/v1/news/trending/?limit=10&hours=24
```

---

## 🔗 전체 API 테스트

Swagger UI에서 모든 API를 테스트할 수 있습니다:
```
http://localhost:8000/docs
```

---

## 💡 질문 사항

1. **Agent Info API 추가 필요?**
   - 에이전트 정보를 동적으로 관리하려면 API 추가 필요

2. **배치 전송 필요?**
   - 성능 최적화가 필요하면 배치 엔드포인트 추가 가능

3. **추가 필드 필요?**
   - 로그에 더 많은 정보를 저장하려면 스키마 수정 필요

---

**작성자**: Backend Developer  
**업데이트**: 2025.11.04  
**문의**: 백엔드 관련 질문은 이슈로 남겨주세요!

