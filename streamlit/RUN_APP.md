# 🎨 Streamlit 앱 실행 가이드

## 🚀 빠른 실행

### 방법 1: 스크립트 사용 (권장)

```bash
cd ..\system_design
start_streamlit.bat
```

또는 PowerShell:
```powershell
cd ..\system_design
.\start_streamlit.ps1
```

### 방법 2: 직접 실행

```bash
# streamlit 디렉토리에서
..\system_design\venv311\Scripts\activate
streamlit run app.py
```

---

## 📱 사용 가능한 앱

### 1. 메인 앱 (`app.py`)

```bash
streamlit run app.py
```

**기능:**
- 📰 뉴스 목록 조회
- 🔍 뉴스 검색
- 🔥 인기 뉴스
- 💬 챗봇 (세션 기반)
- 🔌 백엔드 연결 확인

### 2. 테스트 페이지 (`test_backend.py`)

```bash
streamlit run test_backend.py
```

**기능:**
- 🧪 모든 API 테스트
- 👥 사용자 관리
- 📰 뉴스 관리
- 💬 대화 관리
- 📊 상세 데이터 조회

---

## ⚙️ 설정

### 백엔드 URL 변경

앱 실행 후 사이드바에서 변경 가능:
- 기본값: `http://localhost:8000`
- 다른 서버: `http://your-server:port`

### 포트 변경

```bash
streamlit run app.py --server.port 8502
```

---

## ❌ 문제 해결

### "백엔드에 연결할 수 없습니다"

1. 백엔드 서버 실행 확인:
   ```bash
   curl http://localhost:8000/health
   ```

2. 백엔드 시작:
   ```bash
   cd ..\system_design
   python main.py
   ```

### "뉴스가 없습니다"

샘플 데이터 생성:
```bash
cd ..\system_design
python create_sample_data.py
```

### 모듈 임포트 에러

패키지 설치:
```bash
pip install -r requirements.txt
```

---

## 📊 접속 정보

- **Streamlit 앱**: http://localhost:8501
- **백엔드 API**: http://localhost:8000
- **API 문서**: http://localhost:8000/docs

---

## 💡 개발 팁

### 자동 새로고침

Streamlit은 파일 수정 시 자동으로 새로고침됩니다.

### 캐시 초기화

앱 우측 상단 메뉴 → "Clear cache"

### 디버그 모드

```bash
streamlit run app.py --logger.level=debug
```

---

**🎉 즐거운 개발 되세요!**




