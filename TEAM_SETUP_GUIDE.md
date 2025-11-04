# 팀원용 빠른 설정 가이드

> **신규 팀원이 프로젝트에 참여하기 위한 간단 가이드**

---

## 🚀 5분 만에 시작하기

### 필수 요구사항
- Python 3.11+
- Git

---

## 📋 설정 순서

### 1️⃣ 저장소 클론 (처음 한 번만)

```powershell
# 프로젝트 클론
git clone [REPOSITORY_URL]
cd financefriend_ONOFF
```

---

### 2️⃣ 백엔드 설정

```powershell
# system_design 디렉토리로 이동
cd system_design

# 가상 환경 생성
python -m venv venv311

# 가상 환경 활성화
.\venv311\Scripts\Activate.ps1

# 의존성 설치
pip install -r requirements.txt

# PostgreSQL 드라이버 설치
pip install psycopg2-binary
```

---

### 3️⃣ 데이터베이스 연결 설정

#### 방법 1: 자동 설정 (추천)

```powershell
# 설정 스크립트 실행
.\setup_supabase.ps1
```

스크립트가 안내하는 대로:
1. .env 파일이 자동 생성됨
2. Supabase 연결 정보를 팀 리더에게 받기
3. .env 파일 수정
4. 자동으로 연결 테스트

#### 방법 2: 수동 설정

1. **템플릿 복사**
   ```powershell
   Copy-Item env_template.txt .env
   ```

2. **.env 파일 수정**
   ```powershell
   notepad .env
   ```

3. **DATABASE_URL 설정** (팀 리더에게 받은 정보 입력)
   ```env
   DATABASE_URL=postgresql://postgres:[PASSWORD]@db.[PROJECT_REF].supabase.co:5432/postgres
   API_HOST=0.0.0.0
   API_PORT=8000
   API_RELOAD=True
   ALLOWED_ORIGINS=http://localhost:8501
   ```

4. **연결 테스트**
   ```powershell
   python test_supabase_connection.py
   ```

---

### 4️⃣ 서버 실행

```powershell
# 백엔드 서버 시작
python main.py
```

**확인**:
- 서버: http://localhost:8000
- API 문서: http://localhost:8000/docs

---

### 5️⃣ 프론트엔드 설정 (Streamlit)

```powershell
# 새 터미널 열기
cd ..
cd streamlit

# 의존성 설치
pip install -r requirements.txt

# Streamlit 앱 실행
streamlit run app.py
```

**확인**:
- 앱: http://localhost:8501

---

## ✅ 설정 완료 확인

모든 것이 정상적으로 작동하는지 확인:

1. **백엔드 API 테스트**
   ```
   http://localhost:8000/health
   ```
   응답: `{"status": "healthy", ...}`

2. **데이터 조회 테스트**
   ```
   http://localhost:8000/api/v1/news/
   ```
   응답: 뉴스 목록 (JSON)

3. **Streamlit 앱 접속**
   - 브라우저가 자동으로 열림
   - 앱이 정상적으로 표시됨

---

## ⚠️ 자주 발생하는 문제

### 문제 1: "psycopg2 not found"
```powershell
pip install psycopg2-binary
```

### 문제 2: "password authentication failed"
- .env 파일의 비밀번호 확인
- 팀 리더에게 올바른 연결 문자열 재확인

### 문제 3: "port 8000 already in use"
```powershell
# 프로세스 종료
Get-Process python | Stop-Process -Force
```

### 문제 4: "could not connect to server"
- 인터넷 연결 확인
- Supabase 프로젝트가 활성화되어 있는지 확인
- DATABASE_URL이 올바른지 확인

---

## 📚 추가 문서

더 자세한 정보는 다음 문서를 참고하세요:

- **SUPABASE_SETUP.md**: Supabase 설정 전체 가이드
- **API_CONNECTION_GUIDE.md**: API 엔드포인트 사용법
- **PROJECT_SUMMARY.md**: 프로젝트 전체 개요
- **QUICK_START.md**: 빠른 시작 가이드

---

## 💬 도움 요청

설정 중 문제가 발생하면:

1. **문서 확인**: 위 추가 문서 참고
2. **팀 채팅**: Slack/Discord에 질문
3. **이슈 등록**: GitHub Issues

---

## 🔐 보안 주의사항

- ⚠️ `.env` 파일을 Git에 커밋하지 마세요
- ⚠️ 데이터베이스 비밀번호를 공개하지 마세요
- ⚠️ Supabase 연결 문자열은 안전하게 공유하세요

---

## 🎯 다음 단계

설정 완료 후:

1. **코드 탐색**: 프로젝트 구조 파악
2. **브랜치 생성**: 새 기능 개발 시작
3. **API 테스트**: http://localhost:8000/docs 에서 테스트
4. **개발 시작**: 즐거운 코딩! 🚀

---

**질문이 있으신가요?**  
팀 리더 또는 팀 채팅방에 문의하세요!

**작성일**: 2025.11.04

