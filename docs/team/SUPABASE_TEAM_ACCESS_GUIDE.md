# 👥 Supabase 팀원 협업 가이드

**작성일**: 2025.11.05  
**목적**: 팀원들이 Supabase 데이터베이스에 접근하는 방법

---

## 🎯 협업 방법 2가지

### 방법 1: Supabase 프로젝트에 팀원 초대 (권장) ⭐
- 팀원이 Supabase Dashboard에 직접 접속 가능
- 데이터베이스 관리, 테이블 확인, SQL 실행 가능
- 무료 플랜에서도 사용 가능

### 방법 2: 연결 정보만 공유
- DATABASE_URL만 공유
- 팀원은 애플리케이션 코드로만 접근
- Dashboard 접근 불가

**추천: 방법 1 (팀원 초대)**

---

## ✅ 방법 1: Supabase 프로젝트에 팀원 초대

### Step 1: Organization 확인/생성

#### 1-1. Supabase Dashboard 접속
1. https://supabase.com/dashboard 로그인
2. 좌측 상단 조직(Organization) 이름 클릭

#### 1-2. Organization 설정
- **개인 계정**: 기본으로 생성됨
- **팀 Organization**: 새로 만들거나 기존 것 사용

**Organization 생성 (필요 시):**
1. 좌측 상단 Organization 이름 클릭
2. **New Organization** 선택
3. 이름 입력: 예) `FinanceFriend Team`
4. **Create Organization**

### Step 2: 프로젝트를 Organization으로 이동 (필요 시)

프로젝트가 개인 계정에 있다면 Organization으로 이동:

1. **프로젝트 선택**
2. **Settings** → **General**
3. **Transfer project** 섹션
4. Organization 선택 후 이동

### Step 3: 팀원 초대 ⭐ 핵심

#### 3-1. Organization 설정 열기
1. 좌측 상단 Organization 이름 클릭
2. **Team Settings** 선택

#### 3-2. 팀원 초대
1. **Members** 탭 클릭
2. **Invite** 버튼 클릭
3. 팀원 이메일 입력: `teammate@example.com`
4. 권한 선택:
   - **Owner**: 모든 권한 (프로젝트 삭제 가능) ⚠️
   - **Admin**: 대부분의 관리 권한
   - **Developer**: 개발 권한 (권장) ⭐
   - **Read-only**: 읽기 전용
5. **Send Invitation** 클릭

#### 3-3. 팀원 수락 과정

**팀원이 받을 이메일:**
```
[Your Name] invited you to join [Organization] on Supabase
```

**팀원이 할 일:**
1. 이메일에서 **Accept Invitation** 클릭
2. Supabase 계정 없으면 회원가입
3. 계정 있으면 로그인
4. 초대 수락

### Step 4: 팀원 접근 확인

**팀원이 확인할 것:**
1. https://supabase.com/dashboard 로그인
2. 좌측 상단에서 Organization 선택
3. 프로젝트 목록에 `financefriend` 프로젝트 표시
4. 프로젝트 클릭하여 Dashboard 접근

---

## 🔑 팀원이 접근할 수 있는 것들

### Developer 권한으로 할 수 있는 것:

✅ **Database**:
- Table Editor에서 데이터 조회/수정
- SQL Editor에서 쿼리 실행
- 테이블 스키마 확인

✅ **API**:
- API 문서 확인
- API 키 확인
- 엔드포인트 테스트

✅ **Logs**:
- 데이터베이스 로그 확인
- API 로그 확인

✅ **Settings**:
- 연결 정보 확인
- 환경 변수 확인

❌ **할 수 없는 것**:
- 프로젝트 삭제
- 결제 정보 변경
- 조직 설정 변경

---

## 📋 방법 2: 연결 정보만 공유 (대안)

Dashboard 접근이 필요 없다면 연결 정보만 공유:

### 공유할 정보

**1. DATABASE_URL (Connection Pooling)**
```
postgresql://postgres.[PROJECT]:[PASSWORD]@aws-0-ap-northeast-2.pooler.supabase.com:6543/postgres
```

**2. 프로젝트 정보**
```
Project ID: [PROJECT_ID]
Region: Northeast Asia (Seoul)
```

### 팀원이 할 일

**로컬 개발 환경 설정:**

1. **프로젝트 클론**:
```bash
git clone https://github.com/MJY250422/financefriend_ONOFF.git
cd financefriend_ONOFF
git checkout feature/connect_streamlit_fastapi
```

2. **백엔드 환경 변수 설정**:
```bash
cd system_design
cp .env.example .env
nano .env  # 또는 메모장으로 열기
```

`.env` 파일 내용:
```env
DATABASE_URL=postgresql://postgres.[PROJECT]:[PASSWORD]@...
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=True
ALLOWED_ORIGINS=http://localhost:8501
```

3. **백엔드 실행**:
```bash
python main.py
```

---

## 🔐 보안 주의사항

### ⚠️ DATABASE_URL 공유 시 주의

**절대 공개하지 말 것:**
- [ ] GitHub에 커밋하지 않기 (.gitignore에 .env 포함됨)
- [ ] 공개 문서에 작성하지 않기
- [ ] 스크린샷 공유 시 비밀번호 가리기

**안전하게 공유하는 방법:**
1. **비공개 채팅**으로 전달 (카카오톡, 슬랙 DM 등)
2. **비밀번호 관리 도구** 사용 (1Password, LastPass 등)
3. **일회성 링크** 사용 (PrivateBin, OneTimeSecret 등)

### 🔒 비밀번호 변경 (필요 시)

침해 의심 시 즉시 변경:

1. Supabase Dashboard → Settings → Database
2. **Database Password** 섹션
3. **Reset Database Password**
4. 새 비밀번호 생성
5. 모든 팀원에게 새 DATABASE_URL 공유
6. 모든 배포 환경(Render 등) 환경 변수 업데이트

---

## 📊 권한 레벨 비교

| 작업 | Owner | Admin | Developer | Read-only |
|------|-------|-------|-----------|-----------|
| 데이터 조회 | ✅ | ✅ | ✅ | ✅ |
| 데이터 수정 | ✅ | ✅ | ✅ | ❌ |
| SQL 실행 | ✅ | ✅ | ✅ | ❌ |
| 테이블 생성 | ✅ | ✅ | ✅ | ❌ |
| API 키 확인 | ✅ | ✅ | ✅ | ✅ |
| 환경 설정 변경 | ✅ | ✅ | ⚠️ 제한적 | ❌ |
| 팀원 초대 | ✅ | ✅ | ❌ | ❌ |
| 결제 관리 | ✅ | ⚠️ 제한적 | ❌ | ❌ |
| 프로젝트 삭제 | ✅ | ❌ | ❌ | ❌ |

**권장 역할:**
- 프로젝트 관리자: **Admin**
- 개발자: **Developer** ⭐
- QA/테스터: **Read-only**

---

## 🎯 실전 시나리오

### 시나리오 1: 3명 팀 프로젝트

**역할 분담:**
- 팀장 (당신): **Owner**
- 백엔드 개발자: **Developer**
- 프론트엔드 개발자: **Developer**

**설정 방법:**
1. Organization 생성: `FinanceFriend Team`
2. 프로젝트를 Organization으로 이동
3. 2명의 팀원을 Developer로 초대
4. 모두 Supabase Dashboard 접근 가능
5. DATABASE_URL 공유 (로컬 개발용)

### 시나리오 2: 5명 이상 대규모 팀

**역할 분담:**
- 프로젝트 관리자 1명: **Admin**
- 백엔드 개발자 2명: **Developer**
- 프론트엔드 개발자 2명: **Developer**
- QA 1명: **Read-only**

**추가 고려사항:**
- Supabase 무료 플랜: 동시 연결 15개
- 필요 시 Pro 플랜 고려 ($25/월)

---

## 📝 팀원에게 보낼 초대 메시지 템플릿

### 이메일 또는 메시지 템플릿

```
안녕하세요 [팀원 이름]님,

FinanceFriend 프로젝트의 Supabase 데이터베이스에 접근 권한을 드립니다.

📧 초대 이메일
[팀원 이메일]로 Supabase 초대 메일을 보냈습니다.
이메일에서 "Accept Invitation"을 클릭해주세요.

🔗 접속 방법
1. https://supabase.com/dashboard 로그인
2. 좌측 상단에서 "FinanceFriend Team" 선택
3. "financefriend" 프로젝트 클릭

📚 추가 문서
- 팀원 설정 가이드: SUPABASE_TEAM_ACCESS_GUIDE.md
- 로컬 개발 가이드: TEAM_RENDER_SETUP.md
- 전체 협업 가이드: 팀원_협업_가이드.md

❓ 문제 발생 시
초대 이메일이 오지 않으면:
1. 스팸 메일함 확인
2. [당신의 연락처]로 연락 주세요

감사합니다!
```

---

## 🔧 문제 해결

### 문제 1: 초대 이메일이 안 옴

**해결:**
1. 스팸 메일함 확인
2. Supabase에서 다시 초대 보내기:
   - Team Settings → Members
   - 해당 이메일 찾기
   - **Resend Invitation** 클릭

### 문제 2: "No organizations found"

**원인:** 프로젝트가 개인 계정에 있음

**해결:**
1. Organization 생성
2. 프로젝트를 Organization으로 이동
3. 팀원 재초대

### 문제 3: 팀원이 데이터베이스에 연결 안 됨

**확인사항:**
1. DATABASE_URL이 올바른지 확인
2. 비밀번호 포함 여부 확인
3. Connection Pooling URL 사용 확인 (포트 6543)
4. 방화벽 확인

### 문제 4: 권한 부족 에러

**해결:**
1. Team Settings → Members
2. 해당 팀원의 Role 확인
3. 필요 시 권한 상향:
   - 점 3개 (...) 클릭
   - **Change Role**
   - **Developer** 선택

---

## 📊 Supabase 무료 플랜 제약사항

### 팀 협업 관련 제약

✅ **무료로 가능:**
- Organization 생성
- 무제한 팀원 초대
- 프로젝트 2개까지
- 500MB 데이터베이스

⚠️ **제약사항:**
- 동시 연결: 15개
- 데이터 전송: 월 2GB
- 스토리지: 1GB

### 팀 규모별 권장

| 팀 규모 | 플랜 | 이유 |
|---------|------|------|
| 1-3명 | Free | 충분함 |
| 4-10명 | Free | 가능 (주의 필요) |
| 10명+ | Pro ($25/월) | 동시 연결 제한 |

---

## ✅ 팀원 초대 체크리스트

### 프로젝트 관리자 (당신)

- [ ] Organization 생성 또는 확인
- [ ] 프로젝트를 Organization으로 이동
- [ ] 팀원 이메일 목록 준비
- [ ] Team Settings에서 팀원 초대
- [ ] 권한 레벨 설정 (Developer 권장)
- [ ] 팀원에게 안내 메시지 전송
- [ ] DATABASE_URL 안전하게 공유
- [ ] 관련 문서 링크 공유

### 팀원

- [ ] Supabase 초대 이메일 확인
- [ ] 초대 수락
- [ ] Supabase 계정 생성/로그인
- [ ] Organization 및 프로젝트 접근 확인
- [ ] 로컬 환경 설정 (`.env` 파일)
- [ ] 백엔드 서버 실행 테스트
- [ ] 데이터베이스 연결 확인

---

## 🎉 초대 완료 후 할 일

### 1. 팀 온보딩 미팅

**논의 항목:**
- 프로젝트 구조 설명
- 데이터베이스 스키마 소개
- 개발 워크플로우
- Git 브랜치 전략

### 2. 권한 테스트

**각 팀원이 확인:**
- [ ] Supabase Dashboard 접속
- [ ] Table Editor에서 데이터 조회
- [ ] SQL Editor에서 쿼리 실행
- [ ] 로컬 백엔드 연결 테스트

### 3. 협업 규칙 수립

**합의 필요:**
- 데이터베이스 스키마 변경 시 누구에게 알릴 것인가?
- SQL 직접 실행 전 리뷰 필요한가?
- 프로덕션 데이터 백업 주기는?

---

## 📚 추가 참고 문서

프로젝트 내 문서:
- **`팀원_협업_가이드.md`** - 전체 협업 프로세스
- **`TEAM_RENDER_SETUP.md`** - 팀원 로컬 환경 설정
- **`SCHEMA_UPDATE_GUIDE.md`** - 데이터베이스 스키마 변경
- **`FRONTEND_BACKEND_CONNECTION_GUIDE.md`** - API 연결 가이드

Supabase 공식:
- https://supabase.com/docs/guides/platform/access-control
- https://supabase.com/docs/guides/platform/organization-based-billing

---

## 💡 팁

### 효율적인 팀 협업

1. **Supabase Dashboard 활용**:
   - SQL Editor로 빠른 데이터 확인
   - Logs 탭으로 실시간 디버깅
   - API 탭으로 엔드포인트 테스트

2. **개발 환경 분리**:
   - 로컬: SQLite 또는 개발용 Supabase 프로젝트
   - 프로덕션: 메인 Supabase 프로젝트

3. **정기 백업**:
   - Supabase는 자동 백업 제공
   - 중요 변경 전 수동 백업 고려

---

**팀원 초대 완료! 이제 함께 개발하세요!** 🚀

---

**작성일**: 2025.11.05  
**최종 수정**: 2025.11.05

