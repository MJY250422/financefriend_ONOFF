# Supabase PostgreSQL 전환 가이드

> **SQLite → Supabase PostgreSQL 마이그레이션**  
> 팀 협업을 위한 클라우드 데이터베이스 설정

---

## 🎯 왜 Supabase?

- ✅ **무료**: 500MB 데이터베이스 (프로젝트에 충분)
- ✅ **팀 협업**: 모든 팀원이 같은 DB 공유
- ✅ **클라우드**: 24/7 접근 가능
- ✅ **웹 UI**: SQL 쿼리, 데이터 확인 가능
- ✅ **백업**: 자동 백업 및 복구
- ✅ **프로덕션 준비**: 실제 배포 시에도 그대로 사용

---

## 📋 전체 작업 순서

1. ✅ Supabase 가입 및 프로젝트 생성 (5분)
2. ✅ 연결 정보 확인 (1분)
3. ✅ 로컬 환경 설정 (3분)
4. ✅ 데이터베이스 연결 테스트 (2분)
5. ✅ 테이블 생성 및 샘플 데이터 (2분)
6. ✅ 팀원과 공유 (1분)

**총 소요 시간: 약 15분**

---

## 1️⃣ Supabase 프로젝트 생성

### Step 1: 가입하기

1. **Supabase 웹사이트 접속**
   ```
   https://supabase.com
   ```

2. **Sign Up** 클릭
   - GitHub 계정으로 로그인 (추천)
   - 또는 이메일로 가입

### Step 2: 프로젝트 생성

1. **"New Project" 클릭**

2. **프로젝트 정보 입력**
   ```
   Name: financefriend
   Database Password: [강력한 비밀번호 생성 및 저장!]
   Region: Northeast Asia (Seoul) - 한국이면 이것 선택
   ```

   ⚠️ **중요**: Database Password를 반드시 저장하세요!

3. **"Create new project" 클릭**
   - 약 2-3분 대기 (프로비저닝 중)

### Step 3: 연결 정보 확인

1. **Settings (설정) → Database 클릭**

2. **Connection String 섹션에서 "URI" 선택**

3. **연결 문자열 복사**
   ```
   postgresql://postgres.[PROJECT_REF]:[YOUR_PASSWORD]@aws-0-ap-northeast-2.pooler.supabase.com:6543/postgres
   ```

   형식:
   ```
   postgresql://postgres:[PASSWORD]@[HOST]:5432/postgres
   ```

   ⚠️ `[YOUR-PASSWORD]`를 실제 비밀번호로 바꿔야 합니다!

4. **Connection Pooler 사용 (선택)**
   - Pooler 모드 권장: `Transaction` 또는 `Session`
   - Port 6543 사용 시 → Pooler 사용
   - Port 5432 사용 시 → Direct 연결

---

## 2️⃣ 로컬 환경 설정

### Step 1: PostgreSQL 드라이버 설치

```powershell
# 프로젝트 디렉토리로 이동
cd system_design

# 가상 환경 활성화
.\venv311\Scripts\Activate.ps1

# PostgreSQL 드라이버 설치
pip install psycopg2-binary

# 설치 확인
pip show psycopg2-binary
```

### Step 2: .env 파일 생성

**파일 위치**: `system_design/.env`

```env
# Supabase PostgreSQL 연결
DATABASE_URL=postgresql://postgres:[YOUR_PASSWORD]@db.[PROJECT_REF].supabase.co:5432/postgres

# API 설정
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=True

# CORS 설정 (팀원 IP 추가 가능)
ALLOWED_ORIGINS=http://localhost:8501,http://localhost:3000
```

**⚠️ 중요**:
- `[YOUR_PASSWORD]`를 실제 Supabase 비밀번호로 교체
- `[PROJECT_REF]`를 실제 프로젝트 참조로 교체
- 이 파일을 Git에 커밋하지 마세요! (`.gitignore`에 추가됨)

### Step 3: .env.example 파일 생성 (팀원 공유용)

**파일 위치**: `system_design/.env.example`

```env
# Supabase PostgreSQL 연결
# Supabase 프로젝트 관리자에게 실제 연결 문자열을 받으세요
DATABASE_URL=postgresql://postgres:[PASSWORD]@db.[PROJECT_REF].supabase.co:5432/postgres

# API 설정
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=True

# CORS 설정
ALLOWED_ORIGINS=http://localhost:8501
```

이 파일은 Git에 커밋하고, 팀원들이 복사해서 사용하도록 합니다.

---

## 3️⃣ 연결 테스트

### 자동 테스트 스크립트 실행

```powershell
cd system_design
python test_supabase_connection.py
```

**예상 출력**:
```
[INFO] Testing Supabase connection...
[INFO] Database URL: postgresql://postgres:***@db.xxxxx.supabase.co:5432/postgres
[SUCCESS] Connected to Supabase PostgreSQL!
[INFO] Server version: PostgreSQL 15.x on x86_64-pc-linux-gnu
[SUCCESS] Connection test passed!
```

### 문제 발생 시

#### 에러 1: "could not connect to server"
```
원인: 잘못된 HOST 또는 네트워크 문제
해결:
1. Supabase 대시보드에서 HOST 다시 확인
2. 인터넷 연결 확인
3. 방화벽 확인
```

#### 에러 2: "password authentication failed"
```
원인: 비밀번호 오류
해결:
1. .env 파일의 비밀번호 확인
2. 특수문자는 URL 인코딩 필요 (예: @ → %40)
3. Supabase에서 비밀번호 재설정
```

#### 에러 3: "No module named 'psycopg2'"
```
원인: 드라이버 미설치
해결:
pip install psycopg2-binary
```

---

## 4️⃣ 데이터베이스 테이블 생성

### 자동 생성 (권장)

```powershell
cd system_design
python main.py
```

서버 시작 시 자동으로 테이블이 생성됩니다:
```
[INFO] Starting News Agent API...
[OK] Database tables created successfully
```

### 수동 생성 (Supabase SQL Editor 사용)

1. **Supabase 대시보드 → SQL Editor**

2. **"New query" 클릭**

3. **스키마 확인 쿼리 실행**:
   ```sql
   -- 생성된 테이블 확인
   SELECT table_name 
   FROM information_schema.tables 
   WHERE table_schema = 'public';
   ```

   **예상 결과**:
   ```
   users
   sessions
   news
   news_embeddings
   user_news_interactions
   agent_info
   agent_tasks
   dialogues
   ```

---

## 5️⃣ 샘플 데이터 생성

### 방법 1: Python 스크립트 (권장)

```powershell
cd system_design
python create_sample_data.py
```

**예상 출력**:
```
[INFO] Creating sample data...
[OK] Created 3 users
[OK] Created 10 news articles
[OK] Created 3 sessions
[OK] Created 6 dialogues
[OK] Created 11 interactions
[SUCCESS] Sample data creation completed!
```

### 방법 2: Supabase Table Editor

1. **Supabase 대시보드 → Table Editor**
2. 각 테이블 선택 → "Insert row"
3. 데이터 직접 입력

---

## 6️⃣ 팀원과 공유하기

### 팀원에게 전달할 정보

#### 방법 1: Supabase 프로젝트 초대 (추천)

1. **Supabase 대시보드 → Settings → Team**
2. **"Invite member" 클릭**
3. 팀원 이메일 입력
4. Role 선택:
   - `Owner`: 모든 권한 (신중히)
   - `Developer`: 데이터베이스 접근 및 수정
   - `Read-only`: 조회만 가능

#### 방법 2: 연결 문자열 직접 공유

**팀원에게 보낼 메시지**:

```
안녕하세요!

프로젝트 데이터베이스를 Supabase PostgreSQL로 전환했습니다.

📋 설정 방법:

1. PostgreSQL 드라이버 설치:
   cd system_design
   pip install psycopg2-binary

2. .env 파일 생성 (system_design/.env):
   DATABASE_URL=postgresql://postgres:[PASSWORD]@db.[PROJECT_REF].supabase.co:5432/postgres
   API_HOST=0.0.0.0
   API_PORT=8000
   API_RELOAD=True
   ALLOWED_ORIGINS=http://localhost:8501

3. [PASSWORD]와 [PROJECT_REF]를 실제 값으로 교체
   (별도 메시지로 전달)

4. 서버 실행:
   python main.py

✅ 연결 확인: http://localhost:8000/docs

문제 발생 시 SUPABASE_SETUP.md 참고하세요!
```

**⚠️ 보안 주의사항**:
- 연결 문자열을 안전하게 공유 (Slack DM, 암호화된 메시지 등)
- Git에 .env 파일 커밋 금지
- 비밀번호는 주기적으로 변경

---

## 7️⃣ 데이터베이스 접근 및 관리

### Supabase 웹 UI 사용

#### 데이터 조회
1. **Table Editor** → 테이블 선택
2. 데이터를 엑셀처럼 확인/수정 가능

#### SQL 쿼리 실행
1. **SQL Editor** → New query
2. SQL 작성 및 실행

예시:
```sql
-- 모든 사용자 조회
SELECT * FROM users;

-- 최근 뉴스 10개
SELECT * FROM news ORDER BY published_at DESC LIMIT 10;

-- 사용자별 상호작용 수
SELECT user_id, COUNT(*) as interaction_count
FROM user_news_interactions
GROUP BY user_id;
```

#### 로그 확인
1. **Logs** → Database Logs
2. 쿼리 성능, 에러 확인 가능

---

## 8️⃣ 백업 및 복구

### 자동 백업

Supabase는 자동으로 백업을 수행합니다:
- **일일 백업**: 최근 7일 보관
- **복구**: 대시보드에서 Point-in-Time Recovery

### 수동 백업 (로컬)

```powershell
# pg_dump 사용 (PostgreSQL 설치 필요)
pg_dump "postgresql://postgres:[PASSWORD]@db.[PROJECT_REF].supabase.co:5432/postgres" > backup.sql
```

### 데이터 내보내기 (CSV)

1. **Supabase Table Editor**
2. 테이블 선택 → Export → CSV

---

## 9️⃣ 성능 최적화 (선택)

### 인덱스 생성

자주 조회하는 컬럼에 인덱스 추가:

```sql
-- 뉴스 제목 검색 최적화
CREATE INDEX idx_news_title ON news USING gin(to_tsvector('english', title));

-- 사용자 상호작용 조회 최적화
CREATE INDEX idx_interactions_user ON user_news_interactions(user_id);
CREATE INDEX idx_interactions_news ON user_news_interactions(news_id);

-- 세션 조회 최적화
CREATE INDEX idx_sessions_user ON sessions(user_id);
CREATE INDEX idx_sessions_token ON sessions(session_token);
```

### Connection Pooling

이미 Supabase가 제공하는 Pooler를 사용 중이므로 별도 설정 불필요.

---

## 🔟 문제 해결 (Troubleshooting)

### 문제 1: "too many connections"

**원인**: 연결 제한 초과 (무료 tier: 동시 연결 60개)

**해결**:
```python
# database.py에 connection pool 설정 추가
engine = create_engine(
    DATABASE_URL,
    pool_size=5,          # 최대 5개 연결
    max_overflow=10,      # 추가 10개 허용
    pool_pre_ping=True
)
```

### 문제 2: "SSL connection required"

**원인**: SSL 없이 연결 시도

**해결**:
```python
# .env 파일 수정
DATABASE_URL=postgresql://postgres:[PASSWORD]@db.[PROJECT_REF].supabase.co:5432/postgres?sslmode=require
```

### 문제 3: "relation does not exist"

**원인**: 테이블이 생성되지 않음

**해결**:
```powershell
# 테이블 재생성
python main.py
```

### 문제 4: SQLite 파일 남아있음

**원인**: 기존 SQLite DB 파일이 남아있음

**해결**:
```powershell
# SQLite 파일 삭제 (선택)
Remove-Item system_design\financefriend.db
Remove-Item system_design\newsagent.db
```

---

## ✅ 체크리스트

전환 완료를 확인하세요:

- [ ] Supabase 프로젝트 생성 완료
- [ ] `.env` 파일에 DATABASE_URL 설정 완료
- [ ] `psycopg2-binary` 설치 완료
- [ ] 연결 테스트 성공
- [ ] 테이블 8개 모두 생성 확인
- [ ] 샘플 데이터 생성 완료
- [ ] FastAPI 서버 정상 실행 (http://localhost:8000/docs)
- [ ] API 호출 테스트 성공
- [ ] 팀원에게 연결 정보 공유 완료
- [ ] `.env` 파일을 `.gitignore`에 추가 확인

---

## 📚 추가 리소스

### Supabase 문서
- 공식 문서: https://supabase.com/docs
- Python 가이드: https://supabase.com/docs/reference/python
- SQL 튜토리얼: https://supabase.com/docs/guides/database

### PostgreSQL 문서
- 공식 문서: https://www.postgresql.org/docs/
- SQLAlchemy: https://docs.sqlalchemy.org/

### 유용한 도구
- **pgAdmin**: PostgreSQL GUI 클라이언트
- **DBeaver**: 범용 데이터베이스 도구
- **Postico** (Mac): PostgreSQL 클라이언트

---

## 🎓 다음 단계

PostgreSQL 전환 후 할 수 있는 것들:

1. **고급 쿼리**
   - Full-text search
   - JSON 쿼리
   - 복잡한 집계

2. **확장 기능**
   - PostGIS (지리 데이터)
   - pg_vector (벡터 검색)
   - pg_cron (스케줄링)

3. **모니터링**
   - Supabase 대시보드로 성능 확인
   - 슬로우 쿼리 최적화

4. **프로덕션 배포**
   - 현재 설정 그대로 배포 가능
   - 환경 변수만 관리

---

## 💬 도움이 필요하신가요?

- Supabase 가입 문제: support@supabase.com
- 프로젝트 문제: GitHub Issues
- 긴급 문제: 팀 리더에게 문의

---

**작성일**: 2025.11.04  
**작성자**: Backend Developer  
**버전**: 1.0.0

**🎉 성공적인 마이그레이션을 기원합니다!**

