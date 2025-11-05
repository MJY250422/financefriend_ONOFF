# 🚀 스키마 업데이트 포함 배포 가이드

**업데이트**: 2025.11.05  
**소요 시간**: 40분 (스키마 업데이트 10분 + 배포 30분)

---

## 📋 배포 순서

### Phase 1: 데이터베이스 스키마 업데이트 (10분) ⭐ 먼저 실행!

### Phase 2: Render 배포 (30분)

---

## ✅ Phase 1: Supabase 스키마 업데이트

### Step 1: Supabase Dashboard 접속 (1분)

1. https://supabase.com/dashboard 접속
2. 프로젝트 선택
3. 좌측 메뉴 **SQL Editor** 클릭

### Step 2: 마이그레이션 SQL 실행 (5분)

**New query** 버튼 클릭 후 다음 SQL 복사 & 붙여넣기:

```sql
-- 1. News 테이블에 summary 컬럼 추가
ALTER TABLE news ADD COLUMN IF NOT EXISTS summary TEXT;

COMMENT ON COLUMN news.summary IS '뉴스 요약 (AI 생성 또는 수동 입력)';

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

-- 코멘트 추가
COMMENT ON TABLE event_logs IS '사용자 이벤트 로그 테이블';
```

**Run** 버튼 클릭 (Ctrl+Enter)

### Step 3: 테이블 확인 (2분)

좌측 메뉴 **Table Editor** 클릭:

**확인사항:**
- [ ] `news` 테이블에 `summary` 컬럼 있음
- [ ] `event_logs` 테이블 생성됨
- [ ] 총 컬럼 수: 10개

### Step 4: 로컬 테스트 (2분)

```bash
cd system_design
python main.py
```

브라우저에서 확인:
```
http://localhost:8000/docs
```

**새로운 엔드포인트 확인:**
- [ ] `POST /api/v1/event-logs/`
- [ ] `GET /api/v1/event-logs/`
- [ ] News 스키마에 `summary` 필드

**서버 중지:** Ctrl+C

---

## ✅ Phase 2: Render 배포

### 이제 기존 배포 가이드를 따르세요!

**`START_DEPLOYMENT.md`** 파일 열고 Step 1~3 진행

**요약:**
1. Render 계정 생성 (5분)
2. Web Service 생성 (15분)
3. 배포 확인 (10분)

---

## 🎉 배포 완료 후 확인

### API 문서 확인

```
https://financefriend-backend.onrender.com/docs
```

**확인사항:**
- [ ] Event Logs 섹션 표시
- [ ] News 스키마에 `summary` 필드

### 기능 테스트

**1. 요약과 함께 뉴스 생성:**
```bash
curl -X POST https://financefriend-backend.onrender.com/api/v1/news/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "테스트 뉴스",
    "url": "https://example.com/test",
    "summary": "이것은 테스트 요약입니다",
    "source": "테스트"
  }'
```

**2. 이벤트 로그 생성:**
```bash
curl -X POST https://financefriend-backend.onrender.com/api/v1/event-logs/ \
  -H "Content-Type: application/json" \
  -d '{
    "event_time": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'",
    "event_name": "test_event",
    "surface": "web",
    "source": "curl"
  }'
```

---

## 📚 추가 문서

- **상세 스키마 가이드**: `SCHEMA_UPDATE_GUIDE.md`
- **배포 가이드**: `START_DEPLOYMENT.md`
- **체크리스트**: `DEPLOYMENT_CHECKLIST.md`

---

**스키마 업데이트 완료! 이제 배포하세요!** 🎉

