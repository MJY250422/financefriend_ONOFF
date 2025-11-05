# 🚀 Render 배포 가이드

**작성일**: 2025.11.05  
**목적**: FastAPI 백엔드를 Render에 무료로 배포하기

---

## 📋 배포 개요

**배포 구성:**
- 백엔드: Render (FastAPI)
- 데이터베이스: Supabase PostgreSQL (기존 유지)
- 프론트엔드: 로컬 실행 (각 팀원 PC)

**예상 시간:** 30분  
**비용:** 무료

---

## ✅ 사전 준비사항

### 1. GitHub 저장소 준비
- ✅ 코드가 GitHub에 업로드되어 있어야 함
- ✅ `feature/connect_streamlit_fastapi` 브랜치 사용

### 2. Supabase 데이터베이스
- ✅ 이미 설정 완료
- ✅ 연결 문자열 확인:
  ```
  postgresql://postgres:[PASSWORD]@aws-0-ap-northeast-2.pooler.supabase.com:6543/postgres
  ```

### 3. 필요한 파일들
- ✅ `system_design/requirements.txt`
- ✅ `system_design/main.py`
- ✅ `system_design/render.yaml` (배포 설정)

---

## 🎯 Step 1: Render 계정 생성

### 1-1. Render 가입

1. **https://render.com** 접속
2. **Get Started for Free** 클릭
3. **Sign up with GitHub** 선택
4. GitHub 계정으로 로그인 및 권한 승인

### 1-2. 저장소 접근 권한 설정

- Render가 GitHub 저장소에 접근할 수 있도록 권한 부여
- `MJY250422/financefriend_ONOFF` 저장소 선택

---

## 🎯 Step 2: Web Service 생성

### 2-1. 새 서비스 만들기

1. **Dashboard** → **New +** 버튼 클릭
2. **Web Service** 선택
3. **Build and deploy from a Git repository** 선택
4. **Next** 클릭

### 2-2. 저장소 연결

1. **Connect a repository** 섹션에서:
   - `financefriend_ONOFF` 저장소 찾기
   - **Connect** 클릭

2. 저장소가 보이지 않으면:
   - **Configure Account** 클릭
   - Render 앱 권한 설정에서 저장소 접근 권한 추가

### 2-3. 기본 설정

**Name:**
```
financefriend-backend
```

**Region:**
```
Singapore (가장 가까운 서버)
```

**Branch:**
```
feature/connect_streamlit_fastapi
```

**Root Directory:**
```
system_design
```
⚠️ **중요**: 반드시 `system_design` 입력! (백엔드 코드가 있는 폴더)

**Runtime:**
```
Python 3
```

### 2-4. Build & Start Commands

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
python main.py
```

### 2-5. Instance Type

**Plan:**
```
Free
- 512 MB RAM
- 0.1 CPU
- 자동 슬립 (15분 미사용 시)
```

---

## 🎯 Step 3: 환경 변수 설정 ⭐ 가장 중요!

**Environment Variables** 섹션에서 다음을 추가:

### 필수 환경 변수

| Key | Value | 설명 |
|-----|-------|------|
| `DATABASE_URL` | `postgresql://postgres:[PASSWORD]@aws-0-ap-northeast-2.pooler.supabase.com:6543/postgres` | Supabase 연결 문자열 |
| `API_HOST` | `0.0.0.0` | 모든 IP에서 접근 허용 |
| `API_PORT` | `8000` | FastAPI 서버 포트 |
| `API_RELOAD` | `False` | 프로덕션 모드 |
| `ALLOWED_ORIGINS` | `*` | CORS 설정 (모든 출처 허용) |
| `LOG_LEVEL` | `INFO` | 로그 레벨 |

### ⚠️ DATABASE_URL 설정 방법

1. Supabase Dashboard 접속
2. **Project Settings** → **Database**
3. **Connection String** 섹션에서 **Connection Pooling** 선택
4. **Mode: Transaction** 선택
5. 연결 문자열 복사:
   ```
   postgresql://postgres.[PROJECT_ID]:[PASSWORD]@aws-0-ap-northeast-2.pooler.supabase.com:6543/postgres
   ```
6. `[PASSWORD]`를 실제 비밀번호로 교체
7. Render의 `DATABASE_URL` 환경 변수에 붙여넣기

---

## 🎯 Step 4: 배포 시작

### 4-1. 서비스 생성

1. 모든 설정 확인 후 **Create Web Service** 클릭
2. 자동으로 배포 시작
3. 로그 확인하며 대기 (약 3-5분)

### 4-2. 배포 로그 확인

다음과 같은 로그가 보이면 성공:

```
==> Building...
Collecting fastapi==0.109.0
...
Successfully installed fastapi-0.109.0 ...

==> Starting server...
[INFO] Starting News Agent API...
[SUCCESS] Database initialized
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000

==> Your service is live 🎉
```

### 4-3. 배포 완료

성공 시 다음과 같은 URL이 생성됨:
```
https://financefriend-backend.onrender.com
```

---

## 🎯 Step 5: 배포 확인

### 5-1. Health Check

브라우저에서 접속:
```
https://financefriend-backend.onrender.com/health
```

**예상 응답:**
```json
{
  "status": "healthy",
  "message": "All systems operational",
  "version": "1.0.0"
}
```

### 5-2. API 문서 확인

```
https://financefriend-backend.onrender.com/docs
```

- Swagger UI가 표시되어야 함
- 모든 엔드포인트 확인 가능
- 직접 테스트 가능

### 5-3. API 테스트

**사용자 목록 조회:**
```bash
curl https://financefriend-backend.onrender.com/api/v1/users/
```

**뉴스 목록 조회:**
```bash
curl https://financefriend-backend.onrender.com/api/v1/news/
```

---

## 🎯 Step 6: 프론트엔드 연결

### 6-1. API 클라이언트 수정

**파일:** `streamlit/api_client.py`

**수정 전:**
```python
BASE_URL = "http://localhost:8000"
```

**수정 후:**
```python
# 로컬 개발용
# BASE_URL = "http://localhost:8000"

# Render 배포 서버
BASE_URL = "https://financefriend-backend.onrender.com"
```

### 6-2. 프론트엔드 실행

```bash
cd streamlit
conda activate financial_friend_minzero
streamlit run app.py
```

### 6-3. 연결 확인

1. Streamlit 앱에서 "뉴스 피드" 탭 확인
2. "👤 사용자 관리" 탭에서 사용자 목록 확인
3. 새 사용자 생성 테스트

---

## 📊 배포 후 관리

### 자동 재배포

Git push 시 자동으로 재배포됨:

```bash
git add .
git commit -m "Update backend"
git push origin feature/connect_streamlit_fastapi
```

Render가 자동으로 감지하고 재배포 시작 (약 3-5분 소요)

### 로그 확인

Render Dashboard:
1. **서비스 선택** → **financefriend-backend**
2. **Logs** 탭
3. 실시간 로그 스트리밍

### 환경 변수 수정

1. **Environment** 탭
2. 환경 변수 추가/수정
3. **Save Changes** → 자동 재배포

### 수동 재배포

1. **Manual Deploy** 탭
2. **Deploy latest commit** 클릭

---

## ⚠️ 주의사항 및 제한사항

### Render 무료 플랜 제한

#### 1. 자동 슬립 (Auto-Sleep)
- **문제**: 15분간 요청이 없으면 서버가 슬립 모드로 전환
- **증상**: 첫 요청 시 30초~1분 대기 시간 발생
- **해결**:
  - 인내심을 갖고 첫 로딩 대기
  - 또는 유료 플랜 사용 ($7/월)

#### 2. 월 750시간 제한
- 무료 플랜은 월 750시간까지 실행 가능
- 한 프로젝트만 운영하면 충분함

#### 3. 빌드 시간
- 코드 변경 시마다 3-5분 빌드 시간 필요
- 빈번한 배포는 개발 속도 저하

### 데이터베이스 연결

- Supabase 무료 플랜: 500MB 저장 공간
- Connection Pooling 사용 (6543 포트)
- 동시 연결 수: 15개 (무료 플랜)

---

## 🔧 문제 해결

### 문제 1: 배포 실패 (Build Error)

**증상:**
```
ERROR: Could not find a version that satisfies the requirement...
```

**원인**: requirements.txt의 패키지 버전 문제

**해결:**
1. `system_design/requirements.txt` 확인
2. 패키지 버전 호환성 확인
3. 필요시 버전 제약 완화 (예: `fastapi>=0.109.0`)

### 문제 2: 서버 시작 실패 (Runtime Error)

**증상:**
```
Application startup failed
Database connection error
```

**원인**: 환경 변수 미설정 또는 잘못된 DATABASE_URL

**해결:**
1. Render Dashboard → Environment 탭
2. `DATABASE_URL` 확인
3. Supabase에서 연결 문자열 재확인
4. 비밀번호 포함 여부 확인

### 문제 3: CORS 에러

**증상:**
```
Access to XMLHttpRequest has been blocked by CORS policy
```

**원인**: ALLOWED_ORIGINS 설정 문제

**해결:**
1. 환경 변수 `ALLOWED_ORIGINS` 확인
2. 값을 `*`로 설정 (모든 출처 허용)
3. 또는 특정 도메인만 허용: `http://localhost:8501,https://yourdomain.com`

### 문제 4: 슬립 모드에서 깨어나지 않음

**증상**: 계속 로딩 중

**해결:**
1. Render Dashboard → Logs 확인
2. **Restart Service** 버튼 클릭
3. 1-2분 대기 후 재시도

---

## 📞 팀원 협업 가이드

### 팀원들에게 공유할 정보

**백엔드 API URL:**
```
https://financefriend-backend.onrender.com
```

**API 문서:**
```
https://financefriend-backend.onrender.com/docs
```

### 팀원 설정 방법

#### 1. 프로젝트 클론 (처음 시작하는 경우)

```bash
git clone https://github.com/MJY250422/financefriend_ONOFF.git
cd financefriend_ONOFF
git checkout feature/connect_streamlit_fastapi
```

#### 2. Conda 환경 설정

```bash
conda create -n financial_friend_minzero python=3.11
conda activate financial_friend_minzero
pip install streamlit pandas requests openai
```

#### 3. API 클라이언트 수정

`streamlit/api_client.py` 파일을 열고:

```python
BASE_URL = "https://financefriend-backend.onrender.com"
```

#### 4. 프론트엔드 실행

```bash
cd streamlit
streamlit run app.py
```

#### 5. 연결 확인

- 브라우저에서 `http://localhost:8501` 열림
- 뉴스 목록이 표시되면 성공!

---

## 💡 개발 워크플로우

### 로컬 개발

```python
# streamlit/api_client.py
BASE_URL = "http://localhost:8000"  # 로컬 개발
```

```bash
# Terminal 1: 백엔드
cd system_design
python main.py

# Terminal 2: 프론트엔드
cd streamlit
streamlit run app.py
```

### 프로덕션 (Render)

```python
# streamlit/api_client.py
BASE_URL = "https://financefriend-backend.onrender.com"  # 프로덕션
```

```bash
# 프론트엔드만 로컬 실행
cd streamlit
streamlit run app.py
```

### 배포

```bash
git add .
git commit -m "Feature: 새 기능 추가"
git push origin feature/connect_streamlit_fastapi
```

Render가 자동으로 재배포 시작!

---

## 📈 성능 모니터링

### Render Dashboard

1. **Metrics** 탭:
   - CPU 사용률
   - 메모리 사용량
   - 응답 시간

2. **Logs** 탭:
   - 실시간 서버 로그
   - 에러 추적

3. **Events** 탭:
   - 배포 이력
   - 서비스 상태 변경

---

## 🎯 다음 단계

### 즉시 가능한 작업

1. ✅ 팀원들과 협업 시작
2. ✅ 뉴스 API 연동
3. ✅ AI 챗봇 구현
4. ✅ 추천 시스템 개발

### 장기 계획

1. 프론트엔드도 배포 (Streamlit Cloud)
2. 커스텀 도메인 연결
3. HTTPS 인증서 (Render 자동 제공)
4. 프로덕션 DB로 업그레이드

---

## 🎉 배포 완료!

축하합니다! 이제 팀원들과 함께 개발할 수 있습니다!

**다음 문서:**
- `팀원_협업_가이드.md` - 팀원 온보딩
- `API_CONNECTION_GUIDE.md` - API 사용법
- `FRONTEND_BACKEND_CONNECTION_GUIDE.md` - 연결 가이드

---

**작성일**: 2025.11.05  
**최종 수정**: 2025.11.05  
**문의**: 프로젝트 담당자

---

## 📚 추가 자료

### Render 공식 문서
- https://render.com/docs/web-services
- https://render.com/docs/deploy-fastapi

### Supabase 문서
- https://supabase.com/docs/guides/database

### FastAPI 문서
- https://fastapi.tiangolo.com/deployment/manual/

---

**Happy Deploying! 🚀**

