# 🔧 개발 과정에서 발생한 문제 및 해결 방법

**작성일**: 2024년 10월 28일  
**작성자**: 시스템 디자인팀  
**목적**: 백엔드-Streamlit 통합 테스트 환경 구축

---

## 📋 목차

1. [환경 설정](#1-환경-설정)
2. [주요 발생 문제](#2-주요-발생-문제)
3. [해결 과정](#3-해결-과정)
4. [최종 해결책](#4-최종-해결책)
5. [팀원을 위한 가이드](#5-팀원을-위한-가이드)

---

## 1. 환경 설정

### 1.1 프로젝트 구조
```
financefriend_ONOFF/
├── system_design/          # 백엔드 (FastAPI)
│   ├── main.py
│   ├── database.py
│   ├── routers/
│   └── venv311/           # Python 3.11 가상환경
└── streamlit/             # 프론트엔드 (Streamlit)
    ├── app.py
    ├── api_client.py
    └── ui/
```

### 1.2 기술 스택
- **백엔드**: FastAPI, SQLAlchemy, Python 3.11
- **프론트엔드**: Streamlit
- **데이터베이스**: SQLite (개발용)

---

## 2. 주요 발생 문제

### ❌ 문제 1: Streamlit 앱 파일 누락
**증상**
```
streamlit_app.py.py 파일이 존재하지 않음
```

**원인**
- 팀원이 만든 Streamlit 앱의 메인 파일명 불일치
- 실행 스크립트가 존재하지 않는 파일을 참조

**영향**
- Streamlit 앱 실행 불가

---

### ❌ 문제 2: PowerShell 한글 깨짐
**증상**
```
실행 스크립트에서 한글이 깨져서 표시됨
```

**원인**
- PowerShell 기본 인코딩이 UTF-8이 아님
- 한글 메시지가 깨져서 출력

**영향**
- 사용자 경험 저하
- 에러 메시지 확인 어려움

---

### ❌ 문제 3: Python 버전 호환성 문제 ⭐ (가장 중요)
**증상**
```bash
ERROR: Failed building wheel for pydantic-core
ERROR: Failed building wheel for psycopg2-binary
Python 3.14.0 사용 중
```

**원인**
- 가상환경(venv311)이 Python 3.14로 생성됨
- Python 3.14는 2024년 10월 릴리스된 개발 버전
- 대부분의 패키지가 Python 3.11~3.12까지만 지원
- pydantic-core, psycopg2-binary 등이 Python 3.14용 빌드 미제공

**영향**
- 모든 패키지 설치 실패
- 백엔드 실행 불가

---

### ❌ 문제 4: 가상환경 활성화 실패
**증상**
```bash
venv311\Scripts\activate.bat 실행
→ 여전히 Python 3.14 사용됨
```

**원인**
- Windows PATH 환경변수에서 Python 3.14가 우선순위가 높음
- activate.bat이 PATH를 변경했지만 시스템 Python이 먼저 인식됨

**영향**
- 가상환경의 Python 3.11을 사용할 수 없음
- 패키지 설치/실행 시 Python 3.14가 계속 사용됨

---

### ❌ 문제 5: pip 모듈 누락 ⭐
**증상**
```bash
venv311\Scripts\python.exe: No module named pip
```

**원인**
- 가상환경 생성 중 네트워크 문제 또는 중단으로 pip 설치 실패
- venv311이 손상된 상태로 생성됨

**영향**
- 패키지 설치 완전 불가
- 모든 pip 명령 실패

---

### ❌ 문제 6: 패키지 설치 실패
**증상**
```bash
ModuleNotFoundError: No module named 'fastapi'
```

**원인**
- pip이 없어서 패키지 설치가 안 됨
- 또는 설치 중 권한 에러로 실패

**영향**
- 백엔드 서버 실행 불가
- import 에러 발생

---

### ❌ 문제 7: 권한 에러 (액세스 거부) ⭐
**증상**
```bash
[WinError 5] 액세스가 거부되었습니다
Could not install packages due to an OSError
```

**원인**
- Python 프로세스가 백그라운드에서 실행 중
- 설치하려는 파일이 사용 중
- venv311이 손상됨

**영향**
- 패키지 설치 중단
- 관리자 권한으로도 설치 실패

---

## 3. 해결 과정

### 3.1 초기 시도 (실패)

#### 시도 1: 직접 패키지 설치
```bash
pip install -r requirements.txt
```
**결과**: ❌ Python 3.14 호환성 문제로 실패

#### 시도 2: 최소 패키지만 설치
```bash
pip install fastapi uvicorn sqlalchemy
```
**결과**: ❌ 여전히 빌드 실패

#### 시도 3: 가상환경 활성화 재시도
```bash
venv311\Scripts\activate.bat
```
**결과**: ❌ PATH 우선순위 문제로 Python 3.14 계속 사용

---

### 3.2 중간 진단

#### 진단 1: Python 버전 확인
```bash
venv311\Scripts\python.exe --version
# 출력: Python 3.11.9 ✅

python --version
# 출력: Python 3.14.0 ❌
```
**발견**: venv311은 3.11이지만 시스템 경로가 3.14를 우선 사용

#### 진단 2: pip 확인
```bash
venv311\Scripts\python.exe -m pip --version
# 출력: No module named pip ❌
```
**발견**: venv311에 pip이 아예 없음!

---

### 3.3 해결 시도

#### 해결 1: pip 복구
```bash
venv311\Scripts\python.exe -m ensurepip --upgrade
```
**결과**: ✅ 성공! pip 24.0 설치됨

#### 해결 2: pip 업그레이드
```bash
venv311\Scripts\python.exe -m pip install --upgrade pip
```
**결과**: ✅ pip 25.3으로 업그레이드

#### 해결 3: 패키지 설치 시도
```bash
venv311\Scripts\python.exe -m pip install fastapi
```
**결과**: ❌ 권한 에러 (액세스 거부)

---

### 3.4 최종 해결

#### 해결 4: Python 프로세스 종료
```bash
taskkill /F /IM python.exe
```
**결과**: 4개의 Python 프로세스 종료됨

#### 해결 5: venv311 완전 재생성
```bash
rmdir /s /q venv311
py -3.11 -m venv venv311
```
**결과**: ✅ 깨끗한 가상환경 생성

#### 해결 6: 패키지 설치 (재생성된 환경)
```bash
venv311\Scripts\python.exe -m pip install --upgrade pip
venv311\Scripts\python.exe -m pip install fastapi uvicorn sqlalchemy requests python-dotenv pydantic email-validator passlib bcrypt python-multipart
```
**결과**: ✅ 모든 패키지 성공적으로 설치!

#### 해결 7: 백엔드 실행
```bash
start_backend.bat
```
**결과**: ✅ 성공!
```
INFO: Uvicorn running on http://0.0.0.0:8000
✅ Database initialized
```

---

## 4. 최종 해결책

### 4.1 핵심 해결 방법

**문제의 근본 원인**
1. venv311이 손상됨 (pip 없음)
2. Python 프로세스가 파일 잠금
3. Python 3.14 호환성 문제

**최종 해결책**
```bash
# 1. 모든 Python 프로세스 종료
taskkill /F /IM python.exe

# 2. 가상환경 완전 삭제
rmdir /s /q venv311

# 3. Python 3.11로 재생성
py -3.11 -m venv venv311

# 4. pip 업그레이드
venv311\Scripts\python.exe -m pip install --upgrade pip

# 5. 패키지 설치
venv311\Scripts\python.exe -m pip install [패키지들]
```

---

### 4.2 생성된 도구

#### 핵심 스크립트
1. **setup.bat** - 초기 설정 (pip + 패키지 설치)
2. **start_backend.bat** - 백엔드 실행
3. **start_streamlit.bat** - Streamlit 실행
4. **create_sample_data.py** - 샘플 데이터 생성

#### 통합 스크립트
- **run_servers.bat/ps1** - 백엔드 + Streamlit 동시 실행

#### API 클라이언트
- **streamlit/api_client.py** - 백엔드 API 호출 라이브러리

---

## 5. 팀원을 위한 가이드

### 5.1 빠른 시작 (처음 설정)

```bash
# 1. Python 3.11 설치 확인
py -3.11 --version

# 2. 가상환경 생성
py -3.11 -m venv venv311

# 3. 초기 설정 (관리자 권한 CMD)
setup.bat

# 4. 백엔드 실행
start_backend.bat

# 5. 샘플 데이터 생성 (새 터미널)
venv311\Scripts\python.exe create_sample_data.py

# 6. Streamlit 실행 (새 터미널)
start_streamlit.bat
```

---

### 5.2 자주 발생하는 문제 & 해결

#### 문제 A: "No module named 'fastapi'"
**해결**:
```bash
# 관리자 권한 CMD에서
setup.bat
```

#### 문제 B: 권한 에러 (액세스 거부)
**해결**:
```bash
# 1. Python 프로세스 종료
taskkill /F /IM python.exe

# 2. 관리자 권한으로 재시도
setup.bat
```

#### 문제 C: venv311이 손상됨
**해결**:
```bash
# 완전 재생성
rmdir /s /q venv311
py -3.11 -m venv venv311
setup.bat
```

#### 문제 D: Python 3.14 사용됨
**해결**:
- venv311의 Python을 직접 사용
```bash
venv311\Scripts\python.exe main.py
```

#### 문제 E: 포트 충돌 (8000, 8501)
**해결**:
```bash
# 포트 사용 프로세스 확인
netstat -ano | findstr :8000

# 프로세스 종료
taskkill /PID [PID번호] /F
```

---

### 5.3 권장 개발 환경

#### Python 버전
- ✅ **Python 3.11.x** (강력 권장)
- ✅ Python 3.12.x (가능)
- ⚠️ Python 3.10.x (최소)
- ❌ Python 3.14.x (절대 사용 금지 - 호환성 문제)

#### 데이터베이스
- ✅ **SQLite** (개발/테스트용, 기본 설정)
- PostgreSQL (프로덕션용, 선택사항)

#### 운영체제
- ✅ Windows 10/11
- ⚠️ 관리자 권한 필요할 수 있음

---

### 5.4 디렉토리 구조

```
system_design/
├── main.py                 # FastAPI 메인
├── database.py             # DB 설정
├── schemas.py              # Pydantic 스키마
├── enums.py               # Enum 정의
├── db_schema_design.py    # SQLAlchemy 모델
├── routers/               # API 라우터
│   ├── users.py
│   ├── sessions.py
│   ├── news.py
│   ├── dialogues.py
│   └── agent_tasks.py
├── venv311/               # 가상환경 ⭐
├── .env.example           # 환경 설정 예시
├── requirements_minimal.txt  # 필수 패키지
├── setup.bat              # 초기 설정 스크립트 ⭐
├── start_backend.bat      # 백엔드 실행 ⭐
├── create_sample_data.py  # 샘플 데이터
└── test_integration.py    # API 테스트

streamlit/
├── app.py                 # 메인 Streamlit 앱 ⭐
├── api_client.py          # 백엔드 API 클라이언트 ⭐
├── test_backend.py        # API 테스트 UI
├── core/                  # 핵심 로직
├── ui/                    # UI 컴포넌트
└── data/                  # 데이터 모듈
```

---

### 5.5 환경 변수 설정 (.env)

```env
# 기본 설정 (개발용)
DATABASE_URL=sqlite:///./financefriend.db
ALLOWED_ORIGINS=http://localhost:8501,http://127.0.0.1:8501
API_HOST=0.0.0.0
API_PORT=8000
```

---

## 6. 교훈 및 권장사항

### 6.1 교훈

1. **Python 버전 호환성 중요**
   - 안정 버전(3.11) 사용 필수
   - 최신 개발 버전(3.14) 사용 금지

2. **가상환경 관리 중요**
   - pip 포함 여부 확인
   - 손상 시 즉시 재생성

3. **프로세스 관리 필요**
   - 설치 전 Python 프로세스 종료
   - 파일 잠금 문제 방지

4. **권한 문제 대비**
   - 관리자 권한으로 초기 설정
   - 권한 에러 시 프로세스 종료 후 재시도

---

### 6.2 팀 권장사항

#### 개발 환경 표준화
- 모든 팀원 Python 3.11 사용
- venv311 가상환경 통일
- setup.bat으로 표준 설정

#### 문서화
- 문제 발생 시 이 문서 참조
- 새로운 문제 발견 시 추가

#### 코드 리뷰
- 가상환경 경로 하드코딩 금지
- 환경 변수 사용 권장

#### 배포 준비
- Docker 컨테이너화 고려
- 환경별 설정 분리 (.env.dev, .env.prod)

---

## 7. 참고 자료

### 7.1 문서
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Streamlit 공식 문서](https://docs.streamlit.io/)
- [SQLAlchemy 문서](https://docs.sqlalchemy.org/)

### 7.2 프로젝트 문서
- `README_SIMPLE.md` - 간단한 시작 가이드
- `START_HERE.md` - 상세 시작 가이드
- `TEST_GUIDE.md` - 테스트 가이드
- `TROUBLESHOOTING.md` - 문제 해결 가이드

### 7.3 API 문서
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 8. 변경 이력

| 날짜 | 작성자 | 변경 내용 |
|------|--------|-----------|
| 2024-10-28 | 시스템 디자인팀 | 초기 작성 - 백엔드-Streamlit 통합 과정 정리 |

---

## 9. 연락처 및 지원

문제 발생 시:
1. 이 문서의 "5.2 자주 발생하는 문제" 섹션 확인
2. `TROUBLESHOOTING.md` 참조
3. 팀 채널에 문의

---

**📌 이 문서는 실제 개발 과정에서 발생한 모든 문제와 해결 방법을 기록했습니다.**  
**새로운 팀원이나 비슷한 문제를 겪는 분들께 도움이 되기를 바랍니다!** 🚀


