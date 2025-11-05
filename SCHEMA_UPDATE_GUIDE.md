# 📊 데이터베이스 스키마 업데이트 가이드

**업데이트 일시**: 2025.11.05  
**목적**: 뉴스 요약 기능 및 이벤트 로깅 기능 추가

---

## 🎯 변경 사항 요약

### 1. News 테이블에 `summary` 컬럼 추가
- AI 또는 수동으로 생성된 뉴스 요약 저장
- TEXT 타입, NULL 허용

### 2. EventLog 테이블 신설
- 사용자 행동 이벤트 추적
- 세션 및 대화와 연결
- JSON payload로 유연한 데이터 저장

---

## ✅ Step 1: Supabase 데이터베이스 업데이트

### 1-1. Supabase Dashboard 접속

1. https://supabase.com/dashboard 접속
2. 프로젝트 선택: `financefriend`
3. 좌측 메뉴에서 **SQL Editor** 클릭

### 1-2. 마이그레이션 SQL 실행

**New query** 클릭 후 다음 SQL 실행:

```sql
-- 1. News 테이블에 summary 컬럼 추가
ALTER TABLE news ADD COLUMN IF NOT EXISTS summary TEXT;

-- 2. Event Logs 테이블 생성
CREATE TABLE IF NOT EXISTS event_logs (
    id           BIGSERIAL PRIMARY KEY,
    event_time   TIMESTAMPTZ NOT NULL,
    session_id   INTEGER REFERENCES sessions(session_id),
    dialogue_id  BIGINT REFERENCES dialogues(dialogue_id),
    event_name   TEXT NOT NULL,
    surface      TEXT,
    source       TEXT,
    ref_id       TEXT,
    payload      JSONB,
    created_at   TIMESTAMPTZ DEFAULT NOW()
);

-- 인덱스 생성 (성능 최적화)
CREATE INDEX IF NOT EXISTS idx_event_logs_event_time ON event_logs(event_time DESC);
CREATE INDEX IF NOT EXISTS idx_event_logs_session_id ON event_logs(session_id);
CREATE INDEX IF NOT EXISTS idx_event_logs_dialogue_id ON event_logs(dialogue_id);
CREATE INDEX IF NOT EXISTS idx_event_logs_event_name ON event_logs(event_name);
```

### 1-3. 실행 확인

**Run** 버튼 클릭 (또는 Ctrl+Enter)

성공 메시지 확인:
```
Success. No rows returned
```

### 1-4. 테이블 확인

좌측 메뉴 **Table Editor** 클릭:
- `news` 테이블에 `summary` 컬럼 확인
- `event_logs` 테이블 생성 확인

---

## ✅ Step 2: 로컬 개발 환경 업데이트

### 2-1. 백엔드 코드 확인

이미 다음 파일들이 업데이트되었습니다:

**업데이트된 파일:**
- ✅ `system_design/db_schema_design.py` - SQLAlchemy 모델 업데이트
- ✅ `system_design/schemas.py` - Pydantic 스키마 업데이트
- ✅ `system_design/routers/event_logs.py` - 이벤트 로그 API 라우터 추가
- ✅ `system_design/main.py` - 라우터 등록

### 2-2. 로컬 테스트

백엔드 서버 재시작:

```bash
cd system_design
python main.py
```

성공 메시지 확인:
```
[INFO] Starting News Agent API...
[SUCCESS] Database initialized
```

### 2-3. API 문서 확인

브라우저에서 확인:
```
http://localhost:8000/docs
```

**새로운 엔드포인트 확인**:
- `POST /api/v1/event-logs/` - 이벤트 로그 생성
- `GET /api/v1/event-logs/` - 이벤트 로그 목록
- `GET /api/v1/event-logs/{id}` - 특정 이벤트 로그 조회

**News 엔드포인트 확인**:
- `POST /api/v1/news/` 스키마에 `summary` 필드 추가 확인

---

## 📝 사용 예시

### 1. 뉴스 요약과 함께 생성

```python
import requests

response = requests.post(
    "http://localhost:8000/api/v1/news/",
    json={
        "title": "한국은행 금리 인상",
        "url": "https://example.com/news/123",
        "content": "한국은행이 기준금리를 0.25%p 인상했습니다...",
        "summary": "한국은행, 기준금리 0.25%p 인상 결정",  # 요약 추가
        "source": "경제신문"
    }
)
print(response.json())
```

### 2. 이벤트 로그 생성

```python
from datetime import datetime
import requests

response = requests.post(
    "http://localhost:8000/api/v1/event-logs/",
    json={
        "event_time": datetime.utcnow().isoformat(),
        "session_id": 1,
        "event_name": "news_viewed",
        "surface": "news_feed",
        "source": "web",
        "ref_id": "news_123",
        "payload": {
            "duration_seconds": 45,
            "scroll_percentage": 80,
            "device": "desktop"
        }
    }
)
print(response.json())
```

### 3. 세션별 이벤트 조회

```python
response = requests.get(
    "http://localhost:8000/api/v1/event-logs/session/1/events"
)
events = response.json()
for event in events:
    print(f"{event['event_name']} at {event['event_time']}")
```

---

## 🎯 이벤트 로그 활용 예시

### 추적 가능한 이벤트

| 이벤트 이름 | 설명 | payload 예시 |
|------------|------|-------------|
| `session_started` | 세션 시작 | `{"device": "mobile", "browser": "Chrome"}` |
| `news_viewed` | 뉴스 조회 | `{"news_id": 123, "duration": 30}` |
| `news_clicked` | 뉴스 클릭 | `{"news_id": 123, "position": 1}` |
| `search_performed` | 검색 수행 | `{"query": "금리", "results": 10}` |
| `button_clicked` | 버튼 클릭 | `{"button_id": "share", "target": "twitter"}` |
| `page_viewed` | 페이지 조회 | `{"page": "dashboard", "referrer": "home"}` |
| `chat_message_sent` | 챗봇 메시지 | `{"message_length": 50, "intent": "question"}` |

### 분석 쿼리 예시

**가장 많이 본 뉴스:**
```sql
SELECT 
    ref_id as news_id,
    COUNT(*) as view_count
FROM event_logs
WHERE event_name = 'news_viewed'
GROUP BY ref_id
ORDER BY view_count DESC
LIMIT 10;
```

**사용자 세션 평균 시간:**
```sql
SELECT 
    session_id,
    MIN(event_time) as session_start,
    MAX(event_time) as session_end,
    EXTRACT(EPOCH FROM (MAX(event_time) - MIN(event_time))) as duration_seconds
FROM event_logs
GROUP BY session_id;
```

---

## 🔄 Render 배포 시 자동 적용

### 배포 시 스키마 업데이트

Render에 배포하면 자동으로 스키마가 업데이트됩니다:

1. **Render가 최신 코드 Pull**
2. **FastAPI 서버 시작**
3. **SQLAlchemy가 자동으로 테이블 생성/업데이트**
   - `init_db()` 함수에서 `Base.metadata.create_all()` 실행
   - 새로운 컬럼 및 테이블 자동 생성

⚠️ **주의**: Supabase에서 수동으로 먼저 실행하는 것을 권장합니다!

---

## ✅ 배포 전 체크리스트

### Supabase 데이터베이스

- [ ] SQL Editor에서 마이그레이션 SQL 실행
- [ ] `news` 테이블에 `summary` 컬럼 확인
- [ ] `event_logs` 테이블 생성 확인
- [ ] 인덱스 생성 확인

### 로컬 테스트

- [ ] 백엔드 서버 정상 시작
- [ ] API 문서에 새 엔드포인트 표시
- [ ] 뉴스 생성 시 `summary` 필드 작동
- [ ] 이벤트 로그 생성 테스트
- [ ] 이벤트 로그 조회 테스트

### Git 커밋

- [ ] 변경된 파일 커밋:
  ```bash
  git add system_design/
  git commit -m "feat: Add summary to news table and create event_logs table"
  git push origin feature/connect_streamlit_fastapi
  ```

### Render 배포

- [ ] Git push 후 자동 배포 대기
- [ ] 배포 로그 확인
- [ ] Health check 테스트
- [ ] API 문서 확인

---

## 🔧 문제 해결

### 문제 1: 컬럼 추가 실패

**에러:**
```
column "summary" of relation "news" already exists
```

**해결:**
- 이미 컬럼이 존재함 → 정상
- `IF NOT EXISTS` 사용했으므로 무시해도 됨

### 문제 2: 외래 키 제약 조건 에러

**에러:**
```
insert or update on table "event_logs" violates foreign key constraint
```

**해결:**
- 존재하는 `session_id` 또는 `dialogue_id` 사용
- NULL 허용되므로 생략 가능

### 문제 3: 인덱스 생성 실패

**에러:**
```
relation "idx_event_logs_event_time" already exists
```

**해결:**
- 이미 인덱스 존재 → 정상
- `IF NOT EXISTS` 사용했으므로 무시해도 됨

---

## 📊 스키마 다이어그램

### 업데이트된 News 테이블

```
news
├── news_id (PK)
├── title
├── url
├── content
├── summary          ← 새로 추가!
├── source
├── published_at
├── created_at
├── updated_at
└── deleted_at
```

### 신설된 EventLog 테이블

```
event_logs
├── id (PK)          ← BIGSERIAL
├── event_time       ← TIMESTAMPTZ
├── session_id (FK)  ← sessions.session_id
├── dialogue_id (FK) ← dialogues.dialogue_id
├── event_name
├── surface
├── source
├── ref_id
├── payload          ← JSONB
└── created_at
```

---

## 🎉 업데이트 완료!

이제 다음 기능을 사용할 수 있습니다:

1. ✅ 뉴스에 AI 생성 요약 저장
2. ✅ 사용자 행동 이벤트 추적
3. ✅ 세션별 이벤트 분석
4. ✅ 대화별 이벤트 분석
5. ✅ 유연한 이벤트 데이터 저장 (JSON)

**이제 Render 배포를 진행하세요!** 🚀

---

**작성일**: 2025.11.05  
**최종 수정**: 2025.11.05

