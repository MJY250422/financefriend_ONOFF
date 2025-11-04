# Supabase 프로젝트 생성 가이드

> **화면 캡처와 함께 따라하는 상세 가이드**

---

## 🎯 목표

Supabase에서 `financefriend` 프로젝트 생성 및 PROJECT_REF 확인

---

## 📋 Step 1: Supabase 가입

### 1-1. 웹사이트 접속
```
https://supabase.com
```

### 1-2. 계정 생성
- **"Start your project"** 또는 **"Sign Up"** 클릭
- **GitHub 계정으로 로그인** (추천)
  - 또는 이메일로 가입 가능

### 1-3. 로그인 완료
- Dashboard로 자동 이동

---

## 🏗️ Step 2: 새 프로젝트 생성

### 2-1. "New Project" 클릭

Dashboard 화면에서:
```
[+ New Project] 버튼 클릭
```

### 2-2. Organization 선택

처음 사용하는 경우:
```
Personal organization 사용
또는 "New organization" 생성
```

### 2-3. 프로젝트 정보 입력

```
┌─────────────────────────────────────┐
│  Name                               │
│  financefriend                      │ ← 입력
├─────────────────────────────────────┤
│  Database Password                  │
│  K8CZGllYyplDcy0y                   │ ← 이미 있음!
├─────────────────────────────────────┤
│  Region                             │
│  Northeast Asia (Seoul)             │ ← 선택
├─────────────────────────────────────┤
│  Pricing Plan                       │
│  Free                               │ ← 무료 선택
└─────────────────────────────────────┘
```

**중요!**
- Name: `financefriend` (정확히 입력)
- Password: `K8CZGllYyplDcy0y` (이미 정해진 비밀번호)
- Region: `Northeast Asia (Seoul)` (한국 서버)

### 2-4. "Create new project" 클릭

```
⏳ 프로젝트 생성 중... (2-3분 소요)
```

화면에 표시:
```
Setting up your project...
Creating your database...
Initializing...
```

---

## 🔍 Step 3: PROJECT_REF 확인

### 3-1. 프로젝트 생성 완료 대기

완료되면 자동으로 프로젝트 Dashboard로 이동합니다.

### 3-2. Settings 메뉴 이동

왼쪽 사이드바:
```
⚙️ Settings (설정) 클릭
```

### 3-3. Database 섹션

Settings 메뉴에서:
```
Database (데이터베이스) 클릭
```

### 3-4. Connection String 확인

페이지를 아래로 스크롤:
```
Connection String 섹션 찾기
```

**Connection pooling** 토글 확인:
```
○ Session mode (추천)
또는
○ Transaction mode
```

**Connection string** 드롭다운:
```
URI 선택 (기본값)
```

### 3-5. 연결 문자열 복사

표시된 문자열 예시:
```
postgresql://postgres.abcdefghijklmnop:[YOUR-PASSWORD]@aws-0-ap-northeast-2.pooler.supabase.com:6543/postgres
```

또는:
```
postgresql://postgres:[YOUR-PASSWORD]@db.abcdefghijklmnop.supabase.co:5432/postgres
```

**PROJECT_REF 찾기**:
```
db.abcdefghijklmnop.supabase.co
   ^^^^^^^^^^^^^^^^
   이 부분이 PROJECT_REF!
```

예시:
- 전체 HOST: `db.abcdefghijklmnop.supabase.co`
- PROJECT_REF: `abcdefghijklmnop` (16자 문자열)

### 3-6. PROJECT_REF 저장

메모장에 복사:
```
PROJECT_REF: abcdefghijklmnop
```

---

## ✅ 완료 확인

다음 정보를 확인하셨나요?

- [x] Supabase 계정 생성 완료
- [x] `financefriend` 프로젝트 생성 완료
- [x] DATABASE PASSWORD: `K8CZGllYyplDcy0y`
- [x] PROJECT_REF 확인 완료 (16자 문자열)
- [x] Region: Northeast Asia (Seoul)

---

## 📝 다음 단계

PROJECT_REF를 확인했다면 다음으로:

**1. 개발자에게 알려주기**
```
PROJECT_REF: [당신의_PROJECT_REF]
```

**2. .env 파일 생성**
```
DATABASE_URL=postgresql://postgres:K8CZGllYyplDcy0y@db.[PROJECT_REF].supabase.co:5432/postgres
```

**3. 연결 테스트**
```powershell
python test_supabase_connection.py
```

---

## 🎨 Supabase Dashboard 둘러보기

프로젝트가 생성되면 다양한 기능 사용 가능:

### Table Editor
```
왼쪽 메뉴 → Table Editor
→ 데이터베이스 테이블을 엑셀처럼 확인/수정
```

### SQL Editor
```
왼쪽 메뉴 → SQL Editor
→ SQL 쿼리 직접 실행
```

### Database
```
왼쪽 메뉴 → Database
→ 연결 정보, 백업, 설정
```

### Logs
```
왼쪽 메뉴 → Logs
→ 쿼리 로그 및 에러 확인
```

---

## ⚠️ 문제 해결

### 문제 1: "Project name already exists"
```
해결: 다른 이름 사용 (예: financefriend-v2)
```

### 문제 2: "Free tier limit reached"
```
해결: 
1. 기존 프로젝트 삭제 (사용 안 하는 것)
2. 또는 유료 플랜 사용
```

### 문제 3: 비밀번호를 잊어버렸어요
```
해결:
1. Settings → Database
2. "Reset database password" 클릭
3. 새 비밀번호 저장
4. 팀원들에게 새 비밀번호 전달
```

### 문제 4: PROJECT_REF를 찾을 수 없어요
```
해결:
1. Settings → Database
2. Connection String 섹션 확인
3. 또는 프로젝트 URL 확인:
   https://app.supabase.com/project/[PROJECT_REF]
```

---

## 🔐 보안 주의사항

### 비밀번호 관리
```
✅ 이미 설정된 비밀번호: K8CZGllYyplDcy0y
⚠️ 이 비밀번호를 반드시 사용하세요 (팀원과 공유된 비밀번호)
❌ 다른 비밀번호로 변경하지 마세요 (팀원 접속 불가)
```

### PROJECT_REF 공유
```
✅ PROJECT_REF는 공개 가능 (민감하지 않음)
⚠️ 비밀번호는 안전하게 공유
```

---

## 📞 도움 요청

### Supabase 공식 지원
- 문서: https://supabase.com/docs
- Discord: https://discord.supabase.com
- GitHub: https://github.com/supabase/supabase

### 팀 내부 지원
- 프로젝트 관리자에게 문의
- SUPABASE_SETUP.md 참고

---

## ✨ 다음 단계로

PROJECT_REF를 확인했다면:

```powershell
# 개발자에게 알려주기
"PROJECT_REF: abcdefghijklmnop"

# 또는 전체 연결 문자열 제공
"DATABASE_URL=postgresql://postgres:K8CZGllYyplDcy0y@db.abcdefghijklmnop.supabase.co:5432/postgres"
```

---

**작성일**: 2025.11.04  
**상태**: ✅ 프로젝트 생성 가이드

