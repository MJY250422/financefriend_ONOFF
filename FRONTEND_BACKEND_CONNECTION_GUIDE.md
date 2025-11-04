# 프론트엔드-백엔드 연결 가이드

> **작성일**: 2025.11.04  
> **대상**: 프론트엔드 개발 팀원

---

## 📌 개요

이 문서는 팀원이 만든 프론트엔드를 FinanceFriend 백엔드 API와 연결하는 방법을 설명합니다.

---

## 🎯 백엔드 정보

### 1. Base URL
```
로컬 개발: http://localhost:8000
네트워크:   http://192.168.80.78:8000
```

### 2. API 문서 (Swagger UI)
```
http://localhost:8000/docs
```
→ 여기서 모든 API 엔드포인트를 테스트할 수 있습니다!

### 3. 데이터베이스
- **Supabase PostgreSQL** (클라우드)
- 팀원 모두 같은 데이터 공유
- 실시간 동기화

### 4. 인증
- **현재**: 인증 없음 (개발 단계)
- **추후**: JWT Bearer Token 예정

---

## 🔌 연결 방법

### Step 1: 백엔드 서버 실행 확인

백엔드 담당자가 서버를 실행했는지 확인:

```bash
# 백엔드 서버 실행 (백엔드 담당자가 실행)
cd system_design
.\venv311\Scripts\activate
python main.py
```

서버 실행 확인:
```
http://localhost:8000/health
```
응답:
```json
{
  "status": "ok",
  "message": "Server is running"
}
```

---

### Step 2: CORS 설정 추가

프론트엔드 주소를 백엔드에 등록해야 합니다.

#### 2-1. 프론트엔드 주소 확인
- React: `http://localhost:3000` (기본)
- Vue.js: `http://localhost:5173` (Vite 기본)
- Next.js: `http://localhost:3000`
- Streamlit: `http://localhost:8501`

#### 2-2. 백엔드 `.env` 파일 수정
**백엔드 담당자에게 요청:**

```env
# system_design/.env 파일에 프론트엔드 주소 추가
ALLOWED_ORIGINS=http://localhost:8501,http://192.168.80.78:8501,http://localhost:3000,http://localhost:5173
```

**프론트엔드 주소를 추가한 후 서버 재시작 필요!**

---

### Step 3: API 호출 예시

프론트엔드에서 백엔드 API를 호출하는 방법:

#### 3-1. JavaScript (React, Vue, Vanilla JS)

```javascript
// 1. 사용자 생성
async function createUser() {
  const response = await fetch('http://localhost:8000/api/v1/users/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      user_name: 'test_user',
      user_email: 'test@example.com',
      user_type: 'student'
    })
  });
  
  const data = await response.json();
  console.log('User created:', data);
  return data;
}

// 2. 뉴스 목록 조회
async function getNewsList() {
  const response = await fetch('http://localhost:8000/api/v1/news/?skip=0&limit=10');
  const data = await response.json();
  console.log('News:', data);
  return data;
}

// 3. 뉴스 클릭 이벤트 전송
async function recordNewsClick(newsId, userId) {
  const response = await fetch(
    `http://localhost:8000/api/v1/news/${newsId}/interactions?user_id=${userId}`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        interaction_type: 'click'
      })
    }
  );
  
  const data = await response.json();
  console.log('Interaction recorded:', data);
  return data;
}

// 4. 챗봇 대화 저장
async function sendChatMessage(sessionId, content, senderType = 'user') {
  const response = await fetch('http://localhost:8000/api/v1/dialogues/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      session_id: sessionId,
      sender_type: senderType,
      content: content,
      intent: 'question'
    })
  });
  
  const data = await response.json();
  console.log('Message saved:', data);
  return data;
}
```

#### 3-2. Python (Streamlit)

```python
import requests
import streamlit as st

# Base URL
BASE_URL = "http://localhost:8000"

# 1. 사용자 생성
def create_user(user_name, user_email, user_type="student"):
    response = requests.post(
        f"{BASE_URL}/api/v1/users/",
        json={
            "user_name": user_name,
            "user_email": user_email,
            "user_type": user_type
        }
    )
    return response.json()

# 2. 뉴스 목록 조회
def get_news_list(skip=0, limit=10):
    response = requests.get(f"{BASE_URL}/api/v1/news/?skip={skip}&limit={limit}")
    return response.json()

# 3. 뉴스 클릭 이벤트 전송
def record_news_click(news_id, user_id):
    response = requests.post(
        f"{BASE_URL}/api/v1/news/{news_id}/interactions?user_id={user_id}",
        json={"interaction_type": "click"}
    )
    return response.json()

# 4. 챗봇 대화 저장
def send_chat_message(session_id, content, sender_type="user"):
    response = requests.post(
        f"{BASE_URL}/api/v1/dialogues/",
        json={
            "session_id": session_id,
            "sender_type": sender_type,
            "content": content,
            "intent": "question"
        }
    )
    return response.json()
```

#### 3-3. Axios (React/Vue 추천)

```javascript
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  }
});

// 1. 사용자 생성
export const createUser = async (userData) => {
  const response = await API.post('/api/v1/users/', userData);
  return response.data;
};

// 2. 뉴스 목록 조회
export const getNewsList = async (skip = 0, limit = 10) => {
  const response = await API.get(`/api/v1/news/?skip=${skip}&limit=${limit}`);
  return response.data;
};

// 3. 뉴스 클릭 이벤트
export const recordNewsClick = async (newsId, userId, interactionType = 'click') => {
  const response = await API.post(
    `/api/v1/news/${newsId}/interactions?user_id=${userId}`,
    { interaction_type: interactionType }
  );
  return response.data;
};

// 4. 챗봇 대화 저장
export const sendChatMessage = async (sessionId, content, senderType = 'user') => {
  const response = await API.post('/api/v1/dialogues/', {
    session_id: sessionId,
    sender_type: senderType,
    content: content,
    intent: 'question'
  });
  return response.data;
};
```

---

## 📋 주요 API 엔드포인트

### 1. **사용자 (Users)**
| Method | Endpoint | 설명 |
|--------|----------|------|
| POST | `/api/v1/users/` | 사용자 생성 |
| GET | `/api/v1/users/{user_id}` | 사용자 조회 |
| GET | `/api/v1/users/` | 사용자 목록 |

### 2. **뉴스 (News)**
| Method | Endpoint | 설명 |
|--------|----------|------|
| POST | `/api/v1/news/` | 뉴스 생성 |
| GET | `/api/v1/news/{news_id}` | 뉴스 상세 조회 |
| GET | `/api/v1/news/` | 뉴스 목록 조회 |
| POST | `/api/v1/news/{news_id}/interactions` | 뉴스 상호작용 기록 |

### 3. **세션 (Sessions)**
| Method | Endpoint | 설명 |
|--------|----------|------|
| POST | `/api/v1/sessions/` | 세션 생성 |
| GET | `/api/v1/sessions/{session_id}` | 세션 조회 |
| PATCH | `/api/v1/sessions/{session_id}` | 세션 업데이트 |

### 4. **대화 (Dialogues)**
| Method | Endpoint | 설명 |
|--------|----------|------|
| POST | `/api/v1/dialogues/` | 대화 저장 |
| GET | `/api/v1/dialogues/session/{session_id}` | 세션의 대화 목록 |

### 5. **에이전트 작업 (Agent Tasks)**
| Method | Endpoint | 설명 |
|--------|----------|------|
| POST | `/api/v1/agent-tasks/` | 에이전트 작업 생성 |
| GET | `/api/v1/agent-tasks/{task_id}` | 작업 조회 |

---

## 🔧 데이터 타입 매핑

### 1. **User Type (사용자 유형)**
```
Enum: "student", "office_worker", "investor", "researcher"
```

### 2. **Interaction Type (상호작용 유형)**
```
Enum: "click", "view", "share", "like", "bookmark", "comment"
```

### 3. **Sender Type (발신자 유형)**
```
Enum: "user", "agent"
```

### 4. **Task Status (작업 상태)**
```
Enum: "pending", "in_progress", "completed", "failed"
```

---

## 🎨 실전 예시: 뉴스 앱 흐름

```javascript
// 1. 앱 시작 시 사용자 생성 또는 가져오기
const user = await createUser({
  user_name: "김철수",
  user_email: "chulsoo@example.com",
  user_type: "student"
});

// 2. 세션 생성
const session = await fetch('http://localhost:8000/api/v1/sessions/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    user_id: user.user_id,
    session_token: `session_${Date.now()}`
  })
}).then(r => r.json());

// 3. 뉴스 목록 가져오기
const newsList = await getNewsList(0, 10);

// 4. 사용자가 뉴스 클릭
newsList.forEach(news => {
  // 뉴스 항목에 클릭 이벤트 연결
  newsElement.addEventListener('click', async () => {
    // 클릭 이벤트를 백엔드에 기록
    await recordNewsClick(news.news_id, user.user_id);
    
    // 뉴스 상세 페이지로 이동
    showNewsDetail(news);
  });
});

// 5. 챗봇 질문
async function handleChatSubmit(message) {
  // 사용자 메시지 저장
  await sendChatMessage(session.session_id, message, 'user');
  
  // AI 응답 (여기서는 간단히 예시)
  const aiResponse = "양적완화는 중앙은행이 시중에 돈을 푸는 정책입니다.";
  
  // AI 응답 저장
  await sendChatMessage(session.session_id, aiResponse, 'agent');
}
```

---

## ⚠️ 주의사항

### 1. **CORS 에러 발생 시**
```
Access to fetch at 'http://localhost:8000' from origin 'http://localhost:3000' 
has been blocked by CORS policy
```

**해결 방법:**
- 백엔드 담당자에게 프론트엔드 주소를 `ALLOWED_ORIGINS`에 추가 요청
- 서버 재시작 필요

### 2. **네트워크 연결 시**
- 로컬 개발: `http://localhost:8000`
- 같은 네트워크: `http://192.168.80.78:8000`
- 방화벽 확인 필요

### 3. **에러 처리**
```javascript
try {
  const data = await createUser(userData);
  console.log('Success:', data);
} catch (error) {
  console.error('Error:', error);
  // 사용자에게 에러 메시지 표시
}
```

---

## 📚 추가 자료

### 1. **API 상세 문서**
- `API_CONNECTION_GUIDE.md` - 모든 API 엔드포인트 상세 설명
- `http://localhost:8000/docs` - Swagger UI (실시간 테스트)

### 2. **데이터베이스 스키마**
- `system_design/db_schema_design.py` - 테이블 구조
- `MIGRATION_COMPLETE_SUMMARY.md` - 전체 프로젝트 구조

### 3. **샘플 데이터**
```bash
# 백엔드에서 샘플 데이터 생성 (백엔드 담당자)
cd system_design
python create_sample_data.py
```

---

## 🚀 시작하기

### 프론트엔드 개발자가 할 일:

1. ✅ 백엔드 담당자에게 프론트엔드 URL 전달
   - 예: `http://localhost:3000`

2. ✅ Swagger UI에서 API 테스트
   - `http://localhost:8000/docs`

3. ✅ 첫 API 호출 테스트
   ```javascript
   // Health check
   fetch('http://localhost:8000/health')
     .then(r => r.json())
     .then(data => console.log(data));
   ```

4. ✅ 실제 기능 연동 시작

---

## 💬 문의사항

- 백엔드 담당자: [이름]
- API 에러 발생 시: Swagger UI에서 먼저 테스트
- CORS 문제: 백엔드 담당자에게 프론트엔드 URL 전달

---

**Happy Coding! 🎉**

