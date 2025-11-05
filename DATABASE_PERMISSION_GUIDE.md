# 🔐 데이터베이스 권한 관리 가이드

**작성일**: 2025.11.05  
**목적**: 팀원 데이터베이스 접근 권한 제어 및 안전한 협업

---

## 🎯 권한 관리 전략

### 전략 1: 역할별 차등 권한 (권장) ⭐

```
👑 프로젝트 관리자 (본인)
→ Owner/Admin: 모든 권한

💻 백엔드 개발자
→ Developer: 데이터/스키마 수정 가능

🎨 프론트엔드 개발자
→ Developer 또는 Read-only
   (데이터 확인만 필요하면 Read-only)

🧪 QA/테스터
→ Read-only: 조회만 가능
```

### 전략 2: 환경별 분리 (더 안전) ⭐⭐

```
프로덕션 DB (중요 데이터)
- Supabase 프로젝트: financefriend-prod
- 제한된 인원만 Admin 권한
- Render 배포에 연결

개발용 DB (테스트 데이터)
- Supabase 프로젝트: financefriend-dev
- 모든 팀원 Developer 권한
- 로컬 개발에 사용
- 언제든 초기화 가능
```

---

## ✅ Read-only 권한으로 초대하기

### 언제 사용?

- 프론트엔드 개발자 (API만 사용, DB 직접 수정 불필요)
- QA/테스터 (데이터 확인만 필요)
- 신규 팀원 (초기 온보딩)
- 외부 협력자

### 초대 방법

1. **Supabase Dashboard** 접속
2. 좌측 상단 **Organization 클릭**
3. **Team Settings** → **Members**
4. **Invite** 버튼
5. 이메일 입력
6. **Role 선택**: **Read-only** ⭐
7. **Send Invitation**

### Read-only로 할 수 있는 것

✅ **가능:**
- Table Editor에서 데이터 조회
- SQL Editor에서 SELECT 쿼리
- API 문서 확인
- 로그 확인

❌ **불가능:**
- 데이터 수정/삭제
- INSERT, UPDATE, DELETE 쿼리
- 테이블 생성/수정
- 스키마 변경

---

## 🔄 환경별 데이터베이스 분리

### Step 1: 개발용 Supabase 프로젝트 생성

#### 1-1. 새 프로젝트 생성

1. https://supabase.com/dashboard
2. **New Project** 클릭
3. 설정:
   ```
   Name: financefriend-dev
   Database Password: [새 비밀번호]
   Region: Northeast Asia (Seoul)
   ```
4. **Create new project**

#### 1-2. 스키마 복사

**SQL Editor**에서 실행:

```sql
-- 1. 프로덕션 DB의 스키마 내보내기
-- (프로덕션 프로젝트에서)
-- Settings → Database → Database Settings → Download Schema

-- 2. 개발 DB에 스키마 적용
-- (개발 프로젝트에서)
-- SQL Editor에 붙여넣고 실행
```

또는 마이그레이션 파일 사용:

```bash
# 개발 DB에 스키마 적용
# system_design/supabase_migration.sql 실행
```

#### 1-3. 샘플 데이터 추가

```bash
cd system_design
python create_sample_data.py
```

### Step 2: 팀원 환경 설정

#### 로컬 개발용 .env

팀원들은 **개발 DB**에 연결:

```env
# .env (로컬 개발)
DATABASE_URL=postgresql://postgres:[DEV_PASSWORD]@db.[DEV_PROJECT_REF].supabase.co:5432/postgres
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=True
ALLOWED_ORIGINS=http://localhost:8501
```

#### Render 프로덕션 배포

Render는 **프로덕션 DB**에 연결:

```env
# Render 환경 변수
DATABASE_URL=postgresql://postgres:[PROD_PASSWORD]@aws-0-ap-northeast-2.pooler.supabase.com:6543/postgres
```

### Step 3: 권한 설정

**개발 DB (financefriend-dev):**
- 모든 팀원: **Developer** 권한
- 마음대로 수정/삭제 가능

**프로덕션 DB (financefriend-prod):**
- 프로젝트 관리자: **Admin**
- 백엔드 리드: **Developer**
- 나머지: **Read-only** 또는 접근 불가

---

## 🛡️ 데이터 보호 모범 사례

### 1. 정기 백업

Supabase는 자동 백업 제공하지만 중요한 변경 전:

```sql
-- 수동 백업 (SQL Editor)
-- 특정 테이블 데이터 내보내기
COPY (SELECT * FROM news) TO STDOUT WITH CSV HEADER;
```

또는 Supabase Dashboard:
```
Table Editor → 테이블 선택 → Export to CSV
```

### 2. 위험한 작업 전 확인

**삭제 전 확인:**
```sql
-- 실수로 전체 삭제 방지
-- BAD
DELETE FROM news;  -- 전체 삭제!

-- GOOD
DELETE FROM news WHERE news_id = 123;  -- 특정 레코드만
SELECT COUNT(*) FROM news WHERE news_id = 123;  -- 먼저 확인
```

### 3. 트랜잭션 사용

```sql
-- 여러 작업을 한 번에
BEGIN;
  UPDATE news SET summary = '수정' WHERE news_id = 1;
  DELETE FROM event_logs WHERE session_id = 999;
  -- 문제 있으면 롤백
ROLLBACK;  -- 또는 COMMIT;
```

### 4. Row Level Security (RLS) 설정

Supabase의 강력한 보안 기능:

```sql
-- 사용자별 데이터 접근 제어
ALTER TABLE news ENABLE ROW LEVEL SECURITY;

-- 정책 생성 (예: 자신이 생성한 뉴스만 삭제 가능)
CREATE POLICY "Users can delete own news"
ON news FOR DELETE
USING (auth.uid() = created_by);
```

---

## 📋 권한 변경하기

### 팀원 권한 상향 (Read-only → Developer)

1. **Team Settings** → **Members**
2. 팀원 찾기
3. 점 3개 **(...)** 클릭
4. **Change Role**
5. **Developer** 선택
6. **Update**

### 팀원 권한 하향 (Developer → Read-only)

신규 팀원이 숙련되기 전:

1. 처음: **Read-only**로 초대
2. 1-2주 후: **Developer**로 승급

### 팀원 제거

1. **Team Settings** → **Members**
2. 팀원 찾기
3. 점 3개 **(...)** 클릭
4. **Remove member**

---

## 🎯 시나리오별 권장 설정

### 시나리오 1: 소규모 팀 (2-3명)

**모두 신뢰하는 팀원:**
```
모든 팀원: Developer 권한
환경: 프로덕션 DB 하나만 사용
백업: 주 1회 수동 백업
```

### 시나리오 2: 중규모 팀 (4-7명)

**역할이 구분된 팀:**
```
프로젝트 관리자: Admin
백엔드 개발자 2명: Developer
프론트엔드 개발자 2명: Read-only
QA 1명: Read-only

환경: 프로덕션 + 개발 DB 분리
백업: 자동 백업 + 중요 변경 전 수동
```

### 시나리오 3: 대규모/외부 협력 (8명+)

**보안이 중요한 경우:**
```
프로젝트 관리자: Owner
백엔드 리드: Admin
백엔드 개발자: Developer (개발 DB만)
프론트엔드: Read-only
QA/외부 협력자: Read-only
인턴: 접근 권한 없음 (로컬만)

환경:
- 프로덕션 DB (제한된 접근)
- 스테이징 DB (백엔드 Developer)
- 개발 DB (모두 Developer)
```

---

## 🚨 문제 발생 시 대응

### 실수로 데이터 삭제

**Supabase 자동 백업 복구:**

1. **Settings** → **Database**
2. **Backups** 섹션
3. 이전 시점 선택
4. **Restore**

⚠️ **주의**: 무료 플랜은 백업 보관 기간 제한

### 권한 오용 발견

1. **즉시 팀원 권한 하향** 또는 제거
2. **데이터베이스 비밀번호 변경**
   ```
   Settings → Database → Reset password
   ```
3. **팀원들에게 새 비밀번호 공유**
4. **Render 환경 변수 업데이트**

### 보안 침해 의심

1. **즉시 비밀번호 변경**
2. **의심스러운 팀원 제거**
3. **최근 로그 확인**
   ```
   Logs → Database Logs
   ```
4. **필요시 프로젝트 재생성**

---

## ✅ 권한 설정 체크리스트

### 프로젝트 시작 시

- [ ] Organization 생성
- [ ] 개발/프로덕션 DB 분리 결정
- [ ] 팀원 역할 정의
- [ ] 적절한 권한으로 팀원 초대
- [ ] DATABASE_URL 안전하게 공유
- [ ] 백업 정책 수립

### 팀원 추가 시

- [ ] 역할 확인 (백엔드/프론트엔드/QA)
- [ ] 적절한 권한 선택
- [ ] Supabase 초대 발송
- [ ] 가이드 문서 공유
- [ ] 설정 확인 및 테스트

### 정기 점검 (월 1회)

- [ ] 팀원 권한 리뷰
- [ ] 퇴사자 권한 제거
- [ ] 데이터 백업 확인
- [ ] 의심스러운 활동 로그 확인

---

## 💡 추가 팁

### 1. Git 브랜치 전략과 연동

```
main 브랜치 → 프로덕션 DB
develop 브랜치 → 개발 DB
feature/* 브랜치 → 로컬 SQLite 또는 개발 DB
```

### 2. 환경 변수 관리

```python
# config.py
import os

ENV = os.getenv("ENV", "development")

if ENV == "production":
    DATABASE_URL = os.getenv("PROD_DATABASE_URL")
elif ENV == "staging":
    DATABASE_URL = os.getenv("STAGING_DATABASE_URL")
else:
    DATABASE_URL = os.getenv("DEV_DATABASE_URL")
```

### 3. 코드 리뷰에 스키마 변경 포함

**Pull Request에 포함:**
- 테이블 추가/수정 사항
- 마이그레이션 SQL
- 영향받는 API 엔드포인트

---

## 📚 관련 문서

- **`SUPABASE_TEAM_ACCESS_GUIDE.md`** - 팀원 초대 방법
- **`SCHEMA_UPDATE_GUIDE.md`** - 스키마 변경 절차
- **`팀원_협업_가이드.md`** - 전체 협업 프로세스

---

**안전한 협업을 위해 적절한 권한 관리는 필수입니다!** 🔒

---

**작성일**: 2025.11.05  
**최종 수정**: 2025.11.05

