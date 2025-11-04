# 🚀 여기서 시작하세요!

Streamlit 앱과 백엔드 서버를 빠르게 실행하는 방법입니다.

---

## ⚡ 가장 빠른 방법 (3단계)

### 1️⃣ 백엔드 서버 실행

**새 터미널을 열고:**

```bash
cd system_design
start_backend.bat
```

**또는 PowerShell:**
```powershell
cd system_design
python main.py
```

✅ 백엔드가 정상 실행되면:
- 🌐 http://localhost:8000 (API 서버)
- 📚 http://localhost:8000/docs (API 문서)

---

### 2️⃣ Streamlit 앱 실행

**새 터미널을 열고:**

```bash
cd system_design
start_streamlit.bat
```

**또는 PowerShell:**
```powershell
cd system_design
start_streamlit.ps1
```

**또는 직접 실행:**
```bash
cd streamlit
..\system_design\venv311\Scripts\activate
streamlit run app.py
```

✅ Streamlit이 정상 실행되면:
- 🖥️ http://localhost:8501 (자동으로 브라우저가 열립니다)

---

### 3️⃣ 테스트

브라우저에서 http://localhost:8501 접속 후:

1. **사이드바에서 "연결 확인" 버튼 클릭**
   - ✅ 성공 메시지가 나오면 정상!

2. **뉴스 목록 탭에서 "뉴스 조회" 클릭**
   - 샘플 데이터가 없으면 아래 명령 실행:
   ```bash
   cd system_design
   python create_sample_data.py
   ```

---

## 🎯 전체 서버 동시 실행 (한 번에)

**PowerShell (권장):**
```powershell
cd system_design
.\run_servers.ps1
```

**또는 배치 파일:**
```bash
cd system_design
run_servers.bat
```

이 방법은 백엔드와 Streamlit을 자동으로 모두 실행합니다.

---

## 🧪 샘플 데이터 생성

뉴스가 표시되지 않으면 샘플 데이터를 생성하세요:

```bash
cd system_design
venv311\Scripts\activate
python create_sample_data.py
```

**생성되는 데이터:**
- 👥 사용자 3명
- 📰 뉴스 10개
- 💬 상호작용 데이터

---

## 📊 접속 URL 요약

| 서비스 | URL |
|--------|-----|
| **Streamlit 앱** | http://localhost:8501 |
| **백엔드 API** | http://localhost:8000 |
| **API 문서** | http://localhost:8000/docs |
| **API 문서 (ReDoc)** | http://localhost:8000/redoc |

---

## ❌ 문제 해결

### Streamlit이 열리지 않으면?

1. **백엔드가 실행 중인지 확인**
   ```bash
   curl http://localhost:8000/health
   ```

2. **포트 확인**
   ```powershell
   netstat -ano | findstr :8501
   ```

3. **직접 실행**
   ```bash
   cd streamlit
   streamlit run app.py --server.port 8502
   ```

### 백엔드가 시작되지 않으면?

1. **.env 파일 확인**
   ```bash
   dir .env
   # 없으면: copy .env.example .env
   ```

2. **가상환경 확인**
   ```bash
   venv311\Scripts\activate
   pip install -r requirements.txt
   ```

### 한글이 깨지면?

PowerShell에서:
```powershell
chcp 65001
.\run_servers.ps1
```

또는 영문 메시지로 변경된 스크립트 사용 (이미 수정됨)

---

## 🎨 사용 가능한 기능

### Streamlit 앱 (`app.py`)
- ✅ 백엔드 연결 확인
- ✅ 뉴스 목록 조회
- ✅ 뉴스 검색
- ✅ 인기 뉴스 확인
- ✅ 챗봇 (세션 기반)

### 테스트 페이지 (`test_backend.py`)
```bash
cd streamlit
streamlit run test_backend.py
```

- ✅ 모든 API 테스트
- ✅ 사용자 관리
- ✅ 뉴스 관리
- ✅ 대화 관리

---

## 📚 더 알아보기

- **상세 가이드**: `TEST_GUIDE.md`
- **빠른 시작**: `QUICK_START.md`
- **통합 가이드**: `README_INTEGRATION.md`

---

## 🎯 다음 단계

1. ✅ 백엔드 실행
2. ✅ Streamlit 실행
3. ✅ 샘플 데이터 생성
4. ✅ 브라우저에서 테스트
5. 🚀 개발 시작!

---

**💡 Tip:** 개발 중에는 백엔드와 Streamlit을 각각 다른 터미널에서 실행하는 것이 로그를 확인하기 좋습니다!

**🎉 즐거운 개발 되세요!**




