# 🚀 빠른 배포 시작 가이드

**소요 시간**: 30분  
**난이도**: 쉬움 ⭐⭐☆☆☆

---

## 🎯 목표

백엔드를 Render에 배포하여 팀원들과 협업 가능한 환경 구축

---

## 📋 3단계로 끝내기

### Step 1: Render 계정 생성 (5분)

1. https://render.com 접속
2. **Sign up with GitHub** 클릭
3. GitHub 계정으로 로그인
4. `financefriend_ONOFF` 저장소 접근 권한 부여

### Step 2: Web Service 생성 (15분)

1. **Dashboard** → **New +** → **Web Service**

2. **기본 설정**:
   ```
   Name: financefriend-backend
   Region: Singapore
   Branch: feature/connect_streamlit_fastapi
   Root Directory: system_design
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: python main.py
   Instance Type: Free
   ```

3. **환경 변수 추가** (Environment Variables):
   
   먼저 Supabase에서 연결 문자열 복사:
   - Supabase Dashboard → Project Settings → Database
   - Connection String (Transaction mode, Port 6543)
   
   그 다음 Render에 추가:
   ```
   DATABASE_URL=postgresql://postgres.[PROJECT]:[PASSWORD]@aws-0-ap-northeast-2.pooler.supabase.com:6543/postgres
   API_HOST=0.0.0.0
   API_PORT=8000
   API_RELOAD=False
   ALLOWED_ORIGINS=*
   LOG_LEVEL=INFO
   ```

4. **Create Web Service** 클릭

5. 배포 로그 확인 (3-5분 대기)

### Step 3: 배포 확인 (10분)

1. **Health Check**:
   ```
   https://financefriend-backend.onrender.com/health
   ```
   응답이 오면 성공! ✅

2. **API 문서 확인**:
   ```
   https://financefriend-backend.onrender.com/docs
   ```

3. **로컬에서 프론트엔드 실행**:
   ```bash
   cd streamlit
   conda activate financial_friend_minzero
   streamlit run app.py
   ```

4. Streamlit 앱에서 뉴스 목록 확인 → 성공! 🎉

---

## ✅ 완료!

이제 팀원들에게 공유하세요:

**백엔드 URL**: https://financefriend-backend.onrender.com  
**팀원 설정 가이드**: `TEAM_RENDER_SETUP.md` 파일 공유

---

## 📚 상세 가이드

더 자세한 내용은 다음 문서를 참고하세요:

- **전체 가이드**: `RENDER_DEPLOYMENT_GUIDE.md`
- **체크리스트**: `DEPLOYMENT_CHECKLIST.md`
- **팀원 가이드**: `TEAM_RENDER_SETUP.md`
- **배포 상태**: `DEPLOYMENT_STATUS.md`

---

## 🔧 문제 발생 시

### 배포 실패
→ `RENDER_DEPLOYMENT_GUIDE.md`의 "문제 해결" 섹션

### 연결 안 됨
→ 환경 변수 `DATABASE_URL` 다시 확인

### 슬립 모드
→ 30초~1분 대기 후 새로고침

---

**이제 시작하세요! 화이팅! 💪**

