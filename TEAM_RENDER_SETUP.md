# 👥 팀원용 Render 배포 연결 가이드

**대상**: FinanceFriend 프로젝트 팀원  
**목적**: Render에 배포된 백엔드 서버에 연결하기  
**소요 시간**: 10분

---

## 🎯 개요

백엔드가 Render에 배포되었습니다!  
이제 여러분의 로컬 PC에서 프론트엔드만 실행하면 됩니다.

**배포된 백엔드 URL:**
```
https://financefriend-backend.onrender.com
```

**API 문서:**
```
https://financefriend-backend.onrender.com/docs
```

---

## ✅ Step 1: 프로젝트 클론 (처음 시작하는 경우)

### 이미 클론했다면 이 단계를 건너뛰세요!

```bash
# GitHub에서 프로젝트 클론
git clone https://github.com/MJY250422/financefriend_ONOFF.git

# 프로젝트 폴더로 이동
cd financefriend_ONOFF

# 작업 브랜치로 전환
git checkout feature/connect_streamlit_fastapi
```

---

## ✅ Step 2: Conda 환경 설정

### 2-1. Conda 환경 생성 (처음 한 번만)

```bash
# Python 3.11 환경 생성
conda create -n financial_friend_minzero python=3.11

# 환경 활성화
conda activate financial_friend_minzero
```

### 2-2. 필수 패키지 설치

```bash
# Streamlit 및 의존성 패키지 설치
pip install streamlit pandas requests openai
```

**설치되는 패키지:**
- streamlit (프론트엔드 프레임워크)
- pandas (데이터 처리)
- requests (HTTP 클라이언트)
- openai (AI 챗봇용)

---

## ✅ Step 3: API 서버 주소 변경

### 3-1. 파일 열기

`streamlit/api_client.py` 파일을 열어주세요.

### 3-2. BASE_URL 변경

**파일 위치:** `streamlit/api_client.py`  
**수정 위치:** 파일 상단 (약 10번째 줄)

**변경 전:**
```python
BASE_URL = "http://localhost:8000"
```

**변경 후:**
```python
# 로컬 백엔드 (개발용)
# BASE_URL = "http://localhost:8000"

# Render 배포 서버 (프로덕션)
BASE_URL = "https://financefriend-backend.onrender.com"
```

### 3-3. 저장

파일을 저장하세요 (Ctrl+S 또는 Cmd+S)

---

## ✅ Step 4: 프론트엔드 실행

### 4-1. Streamlit 폴더로 이동

```bash
cd streamlit
```

### 4-2. Streamlit 앱 실행

```bash
streamlit run app.py
```

### 4-3. 브라우저 확인

자동으로 브라우저가 열리면서 앱이 실행됩니다:
```
http://localhost:8501
```

브라우저가 자동으로 열리지 않으면 위 주소를 직접 입력하세요.

---

## ✅ Step 5: 연결 확인

### 5-1. 백엔드 연결 상태 확인

Streamlit 앱 상단에서:
- ✅ "백엔드 연결됨" 메시지 확인
- ❌ "백엔드 연결 실패" 메시지가 뜨면 아래 문제 해결 섹션 참고

### 5-2. 데이터 확인

**"📰 뉴스 피드" 탭:**
- 뉴스 목록이 표시되어야 함
- 샘플 뉴스 10개 확인

**"👤 사용자 관리" 탭:**
- 기존 사용자 목록 확인
- 새 사용자 생성 테스트

### 5-3. 기능 테스트

1. **뉴스 조회**: 뉴스 목록 확인
2. **사용자 생성**: 새 사용자 만들기
3. **챗봇**: AI 챗봇과 대화 (OpenAI API 키 필요 시)

---

## 🔧 문제 해결

### 문제 1: "백엔드 연결 실패" 메시지

**원인:**
- Render 서버가 슬립 모드에 있을 수 있음 (15분 미사용 시)
- 인터넷 연결 문제

**해결:**
1. **30초~1분 대기** 후 새로고침 (F5)
2. 브라우저에서 직접 확인:
   ```
   https://financefriend-backend.onrender.com/health
   ```
3. 위 주소에서 응답이 오면 정상 → Streamlit 앱 새로고침

### 문제 2: "ModuleNotFoundError: No module named 'streamlit'"

**원인:** Conda 환경이 활성화되지 않았거나 패키지 미설치

**해결:**
```bash
# 환경 활성화 확인
conda activate financial_friend_minzero

# 패키지 재설치
pip install streamlit pandas requests openai
```

### 문제 3: 데이터가 표시되지 않음

**원인:** 
- API URL이 잘못 설정됨
- 데이터베이스가 비어있음

**해결:**
1. `streamlit/api_client.py`의 `BASE_URL` 다시 확인
2. API 문서에서 직접 확인:
   ```
   https://financefriend-backend.onrender.com/docs
   ```
3. `/api/v1/news/` 엔드포인트 테스트

### 문제 4: CORS 에러

**브라우저 콘솔 에러:**
```
Access to XMLHttpRequest has been blocked by CORS policy
```

**해결:**
- 백엔드 관리자에게 문의
- ALLOWED_ORIGINS 환경 변수에 추가 필요

---

## 📝 일상 개발 워크플로우

### 매일 시작할 때

```bash
# 1. 프로젝트 폴더로 이동
cd financefriend_ONOFF

# 2. 최신 코드 가져오기
git pull origin feature/connect_streamlit_fastapi

# 3. Conda 환경 활성화
conda activate financial_friend_minzero

# 4. Streamlit 실행
cd streamlit
streamlit run app.py
```

### 코드 수정 후

```bash
# 1. 변경사항 추가
git add .

# 2. 커밋 메시지 작성
git commit -m "Feature: 새로운 기능 추가"

# 3. GitHub에 푸시
git push origin feature/connect_streamlit_fastapi
```

---

## 💡 개발 팁

### 로컬 백엔드 vs Render 백엔드

**로컬 백엔드 사용 (빠른 개발):**
```python
# streamlit/api_client.py
BASE_URL = "http://localhost:8000"
```

백엔드도 로컬에서 실행:
```bash
cd system_design
python main.py
```

**Render 백엔드 사용 (팀 협업):**
```python
# streamlit/api_client.py
BASE_URL = "https://financefriend-backend.onrender.com"
```

### 환경 변수로 전환 (고급)

`streamlit/api_client.py`를 다음과 같이 수정하면 자동 전환 가능:

```python
import os

# 환경 변수로 자동 전환
BASE_URL = os.getenv(
    "BACKEND_URL",
    "https://financefriend-backend.onrender.com"  # 기본값
)
```

그 다음 로컬 백엔드 사용 시:
```bash
export BACKEND_URL="http://localhost:8000"  # Mac/Linux
# 또는
set BACKEND_URL=http://localhost:8000  # Windows CMD
# 또는
$env:BACKEND_URL="http://localhost:8000"  # Windows PowerShell
```

---

## 📞 도움이 필要하면

### 1. API 문서 확인
```
https://financefriend-backend.onrender.com/docs
```
모든 엔드포인트와 사용법이 자동으로 문서화되어 있습니다.

### 2. 로그 확인

**브라우저 개발자 도구:**
- F12 키 또는 마우스 우클릭 → 검사
- Console 탭에서 에러 메시지 확인

**Streamlit 터미널:**
- Streamlit 실행 중인 터미널에서 로그 확인

### 3. 팀원 또는 프로젝트 담당자에게 문의

---

## ✅ 체크리스트

설정 완료 확인:

- [ ] 프로젝트 클론 완료
- [ ] Conda 환경 생성 및 활성화
- [ ] 필수 패키지 설치 완료
- [ ] `BASE_URL` 변경 완료
- [ ] Streamlit 앱 실행 성공
- [ ] 백엔드 연결 확인
- [ ] 뉴스 목록 표시 확인
- [ ] 사용자 생성 테스트 성공

모두 체크되면 개발 준비 완료! 🎉

---

## 🎯 다음 단계

이제 본격적으로 개발을 시작하세요!

**개발 가능한 기능:**
1. 🤖 AI 챗봇 고도화
2. 📊 데이터 시각화 대시보드
3. 🔍 뉴스 검색 및 필터링
4. 💬 사용자 피드백 시스템
5. 📈 개인화 추천 알고리즘

---

**행운을 빕니다! Happy Coding! 🚀**

---

**작성일**: 2025.11.05  
**최종 수정**: 2025.11.05

