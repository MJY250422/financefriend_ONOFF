# 🚀 빠른 시작 가이드

백엔드와 Streamlit을 연동하여 테스트하는 가장 빠른 방법입니다.

## 📝 3단계로 시작하기

### 1️⃣ 환경 설정 (최초 1회)

```bash
# system_design 디렉토리에서 실행
copy .env.example .env
```

`.env` 파일을 열고 필요한 설정만 확인:
```env
# 개발용으로는 기본 설정 그대로 사용 가능
DATABASE_URL=sqlite:///./financefriend.db
ALLOWED_ORIGINS=http://localhost:8501,http://127.0.0.1:8501
```

### 2️⃣ 서버 실행

**Windows 배치 파일** (가장 간단):
```bash
run_servers.bat
```

**또는 PowerShell**:
```powershell
.\run_servers.ps1
```

이 명령은 자동으로:
- ✅ 백엔드 서버를 시작합니다 (http://localhost:8000)
- ✅ Streamlit 앱을 시작합니다 (http://localhost:8501)
- ✅ 브라우저를 자동으로 엽니다

### 3️⃣ 테스트

#### 옵션 A: 샘플 데이터로 테스트 (권장)

```bash
# 새 터미널 열기
cd system_design
venv311\Scripts\activate
python create_sample_data.py
```

이제 Streamlit 앱에서 샘플 뉴스와 사용자 데이터를 확인할 수 있습니다!

#### 옵션 B: API 직접 테스트

브라우저에서 접속:
- 📚 **Swagger UI**: http://localhost:8000/docs
- 🧪 **테스트 페이지**: `streamlit run test_backend.py` 실행

---

## 🎯 주요 URL

| 서비스 | URL | 설명 |
|--------|-----|------|
| 백엔드 API | http://localhost:8000 | FastAPI 서버 |
| API 문서 (Swagger) | http://localhost:8000/docs | 인터랙티브 API 문서 |
| API 문서 (ReDoc) | http://localhost:8000/redoc | 보기 좋은 API 문서 |
| Streamlit 앱 | http://localhost:8501 | 메인 웹 애플리케이션 |

---

## 💡 유용한 명령어

### 통합 테스트 실행
```bash
python test_integration.py
```

### 샘플 데이터 생성
```bash
python create_sample_data.py
```

### 백엔드 테스트 페이지
```bash
cd ..\streamlit
streamlit run test_backend.py
```

---

## ❓ 문제 해결

### 서버가 시작되지 않으면?

1. **가상환경 확인**
   ```bash
   venv311\Scripts\activate
   ```

2. **패키지 설치**
   ```bash
   pip install -r requirements.txt
   ```

3. **.env 파일 확인**
   ```bash
   dir .env
   # 없으면: copy .env.example .env
   ```

### 포트가 이미 사용 중이면?

```powershell
# 포트 8000 확인
netstat -ano | findstr :8000

# 프로세스 종료 (PID 확인 후)
taskkill /PID <PID> /F
```

---

## 📊 테스트 시나리오 예시

### 1. 기본 연동 확인
```bash
# 1. 서버 실행
run_servers.bat

# 2. 헬스 체크
curl http://localhost:8000/health

# 3. Streamlit 앱 확인
# 브라우저에서 http://localhost:8501 접속
```

### 2. 전체 워크플로우
```bash
# 1. 서버 실행
run_servers.bat

# 2. 샘플 데이터 생성 (새 터미널)
python create_sample_data.py

# 3. 통합 테스트
python test_integration.py

# 4. Streamlit에서 데이터 확인
# 브라우저에서 뉴스 목록, 사용자 목록 확인
```

---

## 🎉 다음 단계

테스트가 성공하면:

1. **백엔드 API 탐색**
   - http://localhost:8000/docs 에서 모든 API 확인

2. **Streamlit 커스터마이징**
   - `streamlit/` 폴더의 컴포넌트 수정
   - `api_client.py`를 활용하여 새 기능 추가

3. **데이터 추가**
   - `create_sample_data.py`를 수정하여 더 많은 데이터 추가
   - 또는 Swagger UI에서 직접 데이터 생성

---

**🎊 준비 완료! 즐거운 개발 되세요!**




