# Supabase 빠른 시작 (1페이지 요약)

> **SQLite에서 Supabase PostgreSQL로 5분 전환**

---

## 🚀 단계별 가이드

### 1. Supabase 프로젝트 생성 (3분)

1. https://supabase.com 접속 → Sign Up (GitHub 계정 사용)
2. "New Project" 클릭
3. 입력:
   - **Name**: `financefriend`
   - **Password**: 강력한 비밀번호 (반드시 저장!)
   - **Region**: `Northeast Asia (Seoul)`
4. "Create project" 클릭 → 2-3분 대기

### 2. 연결 정보 확인 (1분)

**프로젝트 비밀번호가 이미 설정되어 있습니다!**

📄 **`system_design/CREDENTIALS_SETUP.md`** 파일을 확인하세요.
- 비밀번호: 문서에 기록됨
- 전체 연결 문자열 예시 포함
- 보안 주의사항 포함

**⚠️ 중요**: `CREDENTIALS_SETUP.md` 파일은 Git에 커밋되지 않습니다 (.gitignore에 포함)

---

### 3. 로컬 설정 (2분)

```powershell
# 1. 디렉토리 이동
cd system_design

# 2. 가상 환경 활성화
.\venv311\Scripts\Activate.ps1

# 3. PostgreSQL 드라이버 설치
pip install psycopg2-binary

# 4. .env 파일 생성
Copy-Item env_template.txt .env

# 5. .env 파일 수정
notepad .env
```

`.env` 파일 설정:

**방법 1: `CREDENTIALS_SETUP.md` 파일 참조** (권장)
```powershell
# 파일을 열어서 전체 연결 문자열 복사
notepad system_design\CREDENTIALS_SETUP.md
```

**방법 2: 직접 입력**
```env
DATABASE_URL=postgresql://postgres:K8CZGllYyplDcy0y@db.[PROJECT_REF].supabase.co:5432/postgres
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=True
ALLOWED_ORIGINS=http://localhost:8501
```

⚠️ `[PROJECT_REF]`는 Supabase 대시보드에서 확인하여 교체하세요!

---

### 4. 연결 테스트 (1분)

```powershell
python test_supabase_connection.py
```

**성공 시**:
```
[SUCCESS] Connected to Supabase PostgreSQL!
[SUCCESS] Connection test passed!
```

**실패 시**: `SUPABASE_SETUP.md` 참고

---

### 5. 서버 시작 (1분)

```powershell
python main.py
```

테이블이 자동 생성되고 서버가 시작됩니다:
- API: http://localhost:8000
- 문서: http://localhost:8000/docs

---

### 6. 샘플 데이터 생성 (선택)

```powershell
python create_sample_data.py
```

---

## ✅ 완료!

이제 팀원들과 같은 데이터베이스를 공유하며 협업할 수 있습니다.

---

## 📤 팀원과 공유

팀원에게 전달:

1. **이 저장소 URL**
2. **DATABASE_URL** (안전하게 공유)
3. **TEAM_SETUP_GUIDE.md** 문서

팀원은 5분 만에 설정 완료 가능!

---

## 🔧 문제 해결

| 에러 | 해결 |
|------|------|
| password authentication failed | .env 비밀번호 확인 |
| could not connect | 인터넷, HOST 확인 |
| psycopg2 not found | `pip install psycopg2-binary` |

더 자세한 내용: **SUPABASE_SETUP.md**

---

## 📊 Supabase 대시보드 활용

- **Table Editor**: 데이터를 엑셀처럼 확인/수정
- **SQL Editor**: SQL 쿼리 직접 실행
- **Logs**: 쿼리 로그 및 에러 확인

---

**총 소요 시간**: 약 8분  
**난이도**: ⭐⭐☆☆☆ (쉬움)

**더 자세한 가이드**: `SUPABASE_SETUP.md` (전체 30페이지)

