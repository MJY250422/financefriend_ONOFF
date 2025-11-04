# 📦 패키지 설치 가이드

## 🚀 빠른 설치

### 방법 1: 자동 설치 스크립트 (권장)

```bash
cd system_design
install_packages.bat
```

이 스크립트는 `requirements.txt`의 모든 패키지를 자동으로 설치합니다.

---

### 방법 2: 수동 설치

#### Step 1: 가상환경 활성화

```bash
cd system_design
venv311\Scripts\activate
```

✅ 가상환경이 활성화되면 프롬프트 앞에 `(venv311)`이 표시됩니다.

#### Step 2: 패키지 설치

```bash
pip install -r requirements.txt
```

---

## 📋 설치되는 패키지 목록

### 백엔드 서버
- `fastapi` - 웹 프레임워크
- `uvicorn` - ASGI 서버
- `pydantic` - 데이터 검증
- `python-dotenv` - 환경변수 관리

### 데이터베이스
- `sqlalchemy` - ORM
- `psycopg2-binary` - PostgreSQL 드라이버

### 보안
- `passlib` - 비밀번호 해싱
- `python-multipart` - 파일 업로드

### 테스트 도구
- `requests` - HTTP 클라이언트 ⭐ (새로 추가)

---

## 🐛 문제 해결

### ModuleNotFoundError: No module named 'requests'

**원인:** `requests` 모듈이 설치되지 않음

**해결:**
```bash
venv311\Scripts\activate
pip install requests
```

### ModuleNotFoundError: No module named 'fastapi'

**원인:** 가상환경이 활성화되지 않았거나 패키지 미설치

**해결:**
```bash
venv311\Scripts\activate
pip install -r requirements.txt
```

### pip install이 너무 느림

**해결:** 국내 미러 서버 사용
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### "Permission denied" 에러

**해결:** 관리자 권한으로 실행
```powershell
# PowerShell을 관리자 권한으로 실행 후
cd system_design
venv311\Scripts\activate
pip install -r requirements.txt
```

---

## ✅ 설치 확인

### 1. Python 버전 확인
```bash
python --version
# Python 3.11.x 출력 확인
```

### 2. 패키지 설치 확인
```bash
pip list
```

다음 패키지들이 보여야 합니다:
- fastapi
- uvicorn
- sqlalchemy
- requests
- pydantic
- passlib

### 3. 임포트 테스트
```bash
python -c "import fastapi, requests, sqlalchemy; print('All packages OK!')"
```

✅ "All packages OK!" 메시지가 나오면 성공!

---

## 🔄 패키지 업데이트

```bash
venv311\Scripts\activate
pip install --upgrade -r requirements.txt
```

---

## 🎯 다음 단계

패키지 설치가 완료되면:

1. **백엔드 실행**
   ```bash
   python main.py
   ```

2. **샘플 데이터 생성**
   ```bash
   python create_sample_data.py
   ```

3. **테스트 실행**
   ```bash
   python test_integration.py
   ```

---

## 📞 추가 도움말

문제가 계속되면:
1. 가상환경 재생성
2. Python 버전 확인 (3.11 이상)
3. pip 업그레이드: `python -m pip install --upgrade pip`

---

**✨ 설치가 완료되었습니다!**




