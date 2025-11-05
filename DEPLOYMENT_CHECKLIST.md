# ✅ Render 배포 체크리스트

**목적**: Render 배포 전 준비사항 및 단계별 확인  
**소요 시간**: 30분

---

## 📋 Phase 1: 배포 준비 (로컬)

### 1. Git 저장소 확인

- [ ] 최신 코드가 GitHub에 푸시되어 있는지 확인
  ```bash
  git status
  git add .
  git commit -m "Prepare for Render deployment"
  git push origin feature/connect_streamlit_fastapi
  ```

- [ ] 브랜치 확인: `feature/connect_streamlit_fastapi`

### 2. 필수 파일 확인

- [ ] `system_design/requirements.txt` 존재
- [ ] `system_design/main.py` 존재
- [ ] `system_design/render.yaml` 존재 (선택사항)
- [ ] 모든 라우터 파일 (`routers/*.py`) 존재

### 3. 환경 변수 준비

Supabase 연결 문자열 확인:

- [ ] Supabase Dashboard 접속
- [ ] Project Settings → Database → Connection String 확인
- [ ] Connection Pooling (포트 6543) 사용
- [ ] 연결 문자열 복사:
  ```
  postgresql://postgres.[PROJECT]:[PASSWORD]@aws-0-ap-northeast-2.pooler.supabase.com:6543/postgres
  ```

---

## 📋 Phase 2: Render 설정

### 1. Render 계정

- [ ] https://render.com 가입 완료
- [ ] GitHub 연동 완료
- [ ] 저장소 접근 권한 부여

### 2. Web Service 생성

Dashboard → New + → Web Service:

- [ ] **Name**: `financefriend-backend`
- [ ] **Region**: Singapore
- [ ] **Branch**: `feature/connect_streamlit_fastapi`
- [ ] **Root Directory**: `system_design`
- [ ] **Runtime**: Python 3
- [ ] **Build Command**: `pip install -r requirements.txt`
- [ ] **Start Command**: `python main.py`
- [ ] **Instance Type**: Free

### 3. 환경 변수 설정 ⭐ 중요!

Environment Variables 섹션에 추가:

- [ ] `DATABASE_URL`: Supabase 연결 문자열
- [ ] `API_HOST`: `0.0.0.0`
- [ ] `API_PORT`: `8000`
- [ ] `API_RELOAD`: `False`
- [ ] `ALLOWED_ORIGINS`: `*`
- [ ] `LOG_LEVEL`: `INFO`

### 4. 배포 시작

- [ ] **Create Web Service** 클릭
- [ ] 배포 로그 확인 (3-5분 대기)
- [ ] "Your service is live 🎉" 메시지 확인

---

## 📋 Phase 3: 배포 확인

### 1. Health Check

브라우저에서 접속:

- [ ] https://financefriend-backend.onrender.com/health
- [ ] 응답 확인:
  ```json
  {
    "status": "healthy",
    "message": "All systems operational",
    "version": "1.0.0"
  }
  ```

### 2. API 문서 확인

- [ ] https://financefriend-backend.onrender.com/docs 접속
- [ ] Swagger UI 정상 표시
- [ ] 모든 엔드포인트 확인 가능

### 3. API 테스트

#### 사용자 목록 조회
```bash
curl https://financefriend-backend.onrender.com/api/v1/users/
```
- [ ] 200 OK 응답
- [ ] 사용자 목록 반환 (배열)

#### 뉴스 목록 조회
```bash
curl https://financefriend-backend.onrender.com/api/v1/news/
```
- [ ] 200 OK 응답
- [ ] 뉴스 목록 반환 (배열)

---

## 📋 Phase 4: 프론트엔드 연결

### 1. API 클라이언트 수정

`streamlit/api_client.py` 파일:

- [ ] 파일 열기
- [ ] `DEFAULT_BACKEND_URL` 확인:
  ```python
  DEFAULT_BACKEND_URL = os.getenv(
      "BACKEND_URL",
      "https://financefriend-backend.onrender.com"
  )
  ```
- [ ] 이미 Render URL로 설정되어 있으면 변경 불필요!

### 2. 로컬에서 프론트엔드 실행

```bash
cd streamlit
conda activate financial_friend_minzero
streamlit run app.py
```

- [ ] Streamlit 앱 정상 실행
- [ ] 브라우저 자동 열림 (http://localhost:8501)

### 3. 연결 확인

Streamlit 앱에서:

- [ ] "📰 뉴스 피드" 탭 → 뉴스 목록 표시
- [ ] "👤 사용자 관리" 탭 → 사용자 목록 표시
- [ ] 새 사용자 생성 테스트 → 성공

---

## 📋 Phase 5: 팀원 공유

### 1. URL 공유

팀원들에게 다음 정보 전달:

- [ ] **백엔드 URL**: https://financefriend-backend.onrender.com
- [ ] **API 문서**: https://financefriend-backend.onrender.com/docs
- [ ] **GitHub 저장소**: https://github.com/MJY250422/financefriend_ONOFF
- [ ] **작업 브랜치**: feature/connect_streamlit_fastapi

### 2. 설정 가이드 공유

- [ ] `TEAM_RENDER_SETUP.md` 파일 공유
- [ ] 팀원들에게 설정 방법 안내
- [ ] 필요 시 1:1 지원

### 3. 팀원 테스트

최소 1명의 팀원이:

- [ ] 프로젝트 클론 완료
- [ ] Conda 환경 설정 완료
- [ ] Streamlit 앱 실행 성공
- [ ] Render 백엔드 연결 확인

---

## 📋 Phase 6: 모니터링 및 유지보수

### 1. 초기 모니터링 (첫 24시간)

Render Dashboard:

- [ ] Logs 탭에서 에러 확인
- [ ] Metrics 탭에서 성능 확인
- [ ] 슬립 모드 작동 확인 (15분 후)

### 2. 문서 업데이트

프로젝트 README:

- [ ] 배포 URL 추가
- [ ] 팀원 설정 방법 추가
- [ ] 트러블슈팅 섹션 추가

### 3. Git 태그 생성 (선택)

```bash
git tag -a v1.0.0-deploy -m "First Render deployment"
git push origin v1.0.0-deploy
```

- [ ] 배포 버전 태그 생성
- [ ] GitHub에 푸시

---

## 🔧 트러블슈팅 체크리스트

### 배포 실패 시

- [ ] requirements.txt의 패키지 버전 확인
- [ ] Root Directory가 `system_design`인지 확인
- [ ] Python 버전 호환성 확인
- [ ] Render 로그에서 에러 메시지 확인

### 서버 시작 실패 시

- [ ] DATABASE_URL 환경 변수 확인
- [ ] Supabase 연결 문자열에 비밀번호 포함 확인
- [ ] 환경 변수 철자 확인 (대소문자 구분)
- [ ] Render 서비스 재시작

### CORS 에러 시

- [ ] ALLOWED_ORIGINS가 `*`로 설정되어 있는지 확인
- [ ] 브라우저 콘솔에서 정확한 에러 메시지 확인
- [ ] 환경 변수 저장 후 재배포 확인

### 슬립 모드 문제

- [ ] 첫 요청 시 30초~1분 대기
- [ ] Health check URL로 서버 깨우기
- [ ] 유료 플랜 고려 ($7/월)

---

## 📊 배포 상태 확인

### ✅ 배포 성공 기준

- [ ] Health check 응답 정상
- [ ] API 문서 접근 가능
- [ ] 사용자 목록 API 정상 작동
- [ ] 뉴스 목록 API 정상 작동
- [ ] 로컬 Streamlit에서 연결 성공
- [ ] 팀원 최소 1명 연결 성공

### 📈 성능 벤치마크

초기 벤치마크 기록:

- [ ] Health check 응답 시간: _____ ms
- [ ] 사용자 목록 조회 시간: _____ ms
- [ ] 뉴스 목록 조회 시간: _____ ms
- [ ] 첫 슬립 깨우기 시간: _____ 초

---

## 🎯 배포 후 다음 단계

### 즉시 (이번 주)

- [ ] 팀원들과 협업 시작
- [ ] 개발 워크플로우 확립
- [ ] Git 브랜치 전략 논의

### 단기 (1-2주)

- [ ] 뉴스 크롤러 구현
- [ ] AI 챗봇 고도화
- [ ] 추천 시스템 개발

### 중기 (1-3개월)

- [ ] 프론트엔드 배포 (Streamlit Cloud)
- [ ] 커스텀 도메인 연결
- [ ] CI/CD 파이프라인 구축

### 장기 (프로젝트 완성 후)

- [ ] 네이버 클라우드 전환 검토
- [ ] 성능 최적화
- [ ] 프로덕션 런칭

---

## 📞 도움 받기

### Render 문제

- **공식 문서**: https://render.com/docs
- **Status 페이지**: https://status.render.com
- **Community Forum**: https://community.render.com

### Supabase 문제

- **공식 문서**: https://supabase.com/docs
- **Discord**: https://discord.supabase.com

### 프로젝트 문제

- **GitHub Issues**: 프로젝트 저장소에 이슈 등록
- **팀 채널**: 팀 커뮤니케이션 채널 활용

---

## 🎉 배포 완료!

모든 체크리스트를 완료했다면 축하합니다! 🎊

이제 팀원들과 함께 본격적인 개발을 시작하세요!

**배포 완료 일시**: _______________  
**배포한 사람**: _______________  
**배포 URL**: https://financefriend-backend.onrender.com

---

**작성일**: 2025.11.05  
**버전**: 1.0.0

