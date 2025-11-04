# FinanceFriend - 빠른 시작 가이드

## 5분 안에 시작하기 🚀

### 1단계: 백엔드 서버 시작

```powershell
cd system_design
python main.py
```

**예상 결과:**
```
[INFO] Starting News Agent API...
[OK] Database tables created successfully
[SUCCESS] Database initialized
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

### 2단계: Streamlit 앱 시작 (새 터미널)

```powershell
cd C:\Users\USER\Desktop\financefriend_ONOFF
streamlit run streamlit/app.py
```

**예상 결과:**
- 브라우저가 자동으로 `http://localhost:8501` 열림
- 생성된 샘플 데이터 확인 가능

---

### 3단계: 샘플 데이터 생성 (선택사항)

```powershell
cd system_design
python create_sample_data.py
```

**생성되는 데이터:**
- 사용자 3명
- 뉴스 10개
- 세션 3개
- 대화 6개
- 상호작용 11개

---

## 주요 URL 📌

- **백엔드 API 문서**: http://localhost:8000/docs
- **백엔드 헬스체크**: http://localhost:8000/health
- **Streamlit 앱**: http://localhost:8501

---

## 자주 사용하는 명령어 💡

### 데이터베이스 초기화
```powershell
cd system_design
Remove-Item financefriend.db
python main.py  # 자동으로 테이블 생성됨
```

### Python 캐시 삭제
```powershell
Get-ChildItem -Recurse -Include "__pycache__" -Directory | Remove-Item -Recurse -Force
```

### 모든 서버 종료
```powershell
Get-Process -Name python | Stop-Process -Force
```

---

## 문제 해결 🔧

### 포트가 이미 사용 중입니다
```powershell
# 포트 8000 사용 프로세스 찾기
Get-NetTCPConnection -LocalPort 8000 | Select-Object OwningProcess

# 프로세스 종료
Stop-Process -Id <PID>
```

### 가상 환경 활성화 안 됨
```powershell
# 실행 정책 변경 (한 번만 실행)
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# 가상 환경 활성화
.\venv311\Scripts\Activate.ps1
```

---

## 다음 단계 ➡️

자세한 내용은 `PROJECT_SUMMARY.md`를 참고하세요!

- 기술 스택 상세 정보
- 해결된 문제들
- API 엔드포인트 목록
- 데이터베이스 스키마
- 개발 가이드


