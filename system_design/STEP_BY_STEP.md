# 🎯 단계별 해결 가이드

## 현재 문제
```
ModuleNotFoundError: No module named 'fastapi'
```

---

## ✅ 해결 순서 (반드시 순서대로!)

### 1단계: fresh_install.bat 실행

```bash
cd system_design
fresh_install.bat
```

**중요:** Y를 눌러 계속 진행하세요.

**확인사항:**
- 각 패키지 설치가 "Successfully installed ..." 메시지와 함께 완료되어야 함
- 마지막에 ✓ 표시가 나타나야 함

**만약 에러가 발생하면:**
- 에러 메시지를 모두 복사
- 어느 패키지에서 에러가 났는지 확인

---

### 2단계: test_imports.bat 실행

```bash
test_imports.bat
```

**예상 출력:**
```
✓ fastapi OK - 0.109.0
✓ uvicorn OK
✓ sqlalchemy OK
✓ requests OK
✓ pydantic OK
```

**만약 ✗가 나타나면:**
- 다시 1단계로 돌아가기
- 또는 수동 설치 (아래 참조)

---

### 3단계: 백엔드 실행

```bash
run_backend_direct.bat
```

**예상 출력:**
```
🚀 Starting News Agent API...
✅ Database initialized
INFO: Uvicorn running on http://0.0.0.0:8000
```

---

## 🚨 여전히 에러가 나면?

### 수동 설치 (터미널에서 직접)

```bash
# 1. venv311 Python 확인
venv311\Scripts\python.exe --version

# 2. 패키지 하나씩 설치 및 확인
venv311\Scripts\python.exe -m pip install fastapi
venv311\Scripts\python.exe -c "import fastapi; print('OK')"

venv311\Scripts\python.exe -m pip install uvicorn
venv311\Scripts\python.exe -c "import uvicorn; print('OK')"

venv311\Scripts\python.exe -m pip install requests
venv311\Scripts\python.exe -c "import requests; print('OK')"
```

**각 단계마다 "OK"가 출력되어야 합니다!**

---

## 📞 에러 발생 시 체크리스트

- [ ] fresh_install.bat을 실행했나요?
- [ ] 설치 중 에러 메시지가 있었나요?
- [ ] test_imports.bat에서 모든 ✓가 나타나나요?
- [ ] 인터넷 연결이 되어 있나요?
- [ ] CMD를 관리자 권한으로 실행했나요?

---

## 🔍 디버깅 명령어

```bash
# 현재 설치된 패키지 확인
venv311\Scripts\python.exe -m pip list | findstr fastapi

# fastapi가 어디에 설치되었는지 확인
venv311\Scripts\python.exe -m pip show fastapi

# Python이 패키지를 찾는 경로 확인
venv311\Scripts\python.exe -c "import sys; print('\n'.join(sys.path))"
```

---

## ⚠️ 최후의 수단: 가상환경 재생성

```bash
# venv311 삭제
rmdir /s /q venv311

# 재생성
py -3.11 -m venv venv311

# 패키지 설치
fresh_install.bat
```




