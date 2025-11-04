# 🚀 빠른 시작 가이드

## 📋 필요한 것
- Python 3.11 설치됨
- 가상환경 `venv311` 생성됨

---

## ⚡ 첫 설정 (최초 1회)

### Windows 관리자 권한으로 실행:
```bash
setup.bat
```

이 스크립트가 자동으로:
- ✅ Python 버전 확인
- ✅ pip 설치/업그레이드
- ✅ 모든 필요한 패키지 설치
- ✅ 설치 검증

---

## 🎯 서버 실행

### 방법 1: 백엔드만
```bash
start_backend.bat
```

### 방법 2: Streamlit만
```bash
start_streamlit.bat
```

### 방법 3: 둘 다 동시에
```bash
run_servers.bat
```

---

## 📊 샘플 데이터 생성

백엔드가 실행 중일 때:
```bash
venv311\Scripts\python.exe create_sample_data.py
```

---

## 🔗 접속 URL

| 서비스 | URL |
|--------|-----|
| Streamlit 앱 | http://localhost:8501 |
| 백엔드 API | http://localhost:8000 |
| API 문서 | http://localhost:8000/docs |

---

## 🐛 문제 해결

### 패키지 설치 오류
→ CMD를 **관리자 권한**으로 실행 후 `setup.bat` 재실행

### 백엔드 연결 실패
→ 먼저 `start_backend.bat` 실행 후 Streamlit 실행

### 포트 충돌
```bash
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

---

## 📚 주요 파일

### 실행 스크립트
- `setup.bat` - 초기 설정 ⭐
- `start_backend.bat` - 백엔드 실행
- `start_streamlit.bat` - Streamlit 실행
- `run_servers.bat` - 모두 실행

### 테스트
- `create_sample_data.py` - 샘플 데이터 생성
- `test_integration.py` - API 테스트

### 설정
- `.env.example` - 환경 설정 템플릿
- `requirements_minimal.txt` - 필수 패키지 목록

---

## ✅ 실행 순서

```bash
# 1. 초기 설정 (최초 1회, 관리자 권한)
setup.bat

# 2. 백엔드 실행
start_backend.bat

# 3. 샘플 데이터 (새 터미널)
venv311\Scripts\python.exe create_sample_data.py

# 4. Streamlit (새 터미널)
start_streamlit.bat
```

---

**이제 http://localhost:8501 에서 앱을 사용할 수 있습니다!** 🎉




