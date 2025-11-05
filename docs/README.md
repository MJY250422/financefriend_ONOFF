# 📚 FinanceFriend 문서 센터

프로젝트의 모든 문서가 카테고리별로 정리되어 있습니다.

---

## 📁 문서 구조

### 🚀 [deployment/](./deployment/) - 배포 가이드
서버 배포 및 배포 관련 모든 문서
- `RENDER_DEPLOYMENT_GUIDE.md` - Render 배포 상세 가이드
- `DEPLOYMENT_WITH_SCHEMA_UPDATE.md` - 스키마 업데이트와 함께 배포
- `DEPLOYMENT_STATUS.md` - 배포 현황 추적
- `DEPLOYMENT_CHECKLIST.md` - 배포 체크리스트
- `START_DEPLOYMENT.md` - 배포 시작 가이드
- `배포_작업_완료_요약.md` - 배포 작업 요약
- `네이버클라우드_배포_가이드.md` - 네이버 클라우드 배포 옵션

### ⚙️ [setup/](./setup/) - 초기 설정
프로젝트 시작 및 환경 설정
- `QUICK_START.md` - 빠른 시작 가이드
- `START.md` - 프로젝트 시작 방법
- `TEAM_SETUP_GUIDE.md` - 팀원 환경 설정
- `TEAM_RENDER_SETUP.md` - Render 서버 연결 설정
- `SUPABASE_QUICKSTART.md` - Supabase 빠른 시작

### 🗄️ [database/](./database/) - 데이터베이스
데이터베이스 설정 및 관리
- `SUPABASE_SETUP.md` - Supabase 상세 설정
- `SUPABASE_PROJECT_SETUP.md` - Supabase 프로젝트 생성
- `SUPABASE_API_KEYS_GUIDE.md` - API 키 사용 가이드
- `DATABASE_PERMISSION_GUIDE.md` - 데이터베이스 권한 관리
- `SCHEMA_UPDATE_GUIDE.md` - 스키마 업데이트 방법

### 👥 [team/](./team/) - 팀 협업
팀원 초대 및 협업 방법
- `SUPABASE_TEAM_ACCESS_GUIDE.md` - Supabase 팀 접근 권한
- `TEAM_ACCESS_INFO.md` - 팀 접근 정보
- `TEAM_SERVER_INFO.md` - 서버 정보 공유
- `팀원_협업_가이드.md` - 협업 가이드
- `네트워크_협업_가이드.md` - 네트워크 환경 협업

### 🔌 [api/](./api/) - API 연결
프론트엔드-백엔드 API 연결
- `API_CONNECTION_GUIDE.md` - API 연결 가이드
- `FRONTEND_BACKEND_CONNECTION_GUIDE.md` - 프론트엔드-백엔드 연결
- `연결_테스트_가이드.md` - 연결 테스트 방법

### 📊 [reports/](./reports/) - 작업 보고서
작업 진행 상황 및 요약
- `오늘_작업_완료_보고서.md` - 서버 배포 완료 보고서
- `오늘_오후_작업_요약.md` - 오후 작업 요약
- `다음_작업_계획.md` - 향후 작업 계획
- `MIGRATION_COMPLETE_SUMMARY.md` - 마이그레이션 완료 요약

### 📋 [project/](./project/) - 프로젝트 정보
프로젝트 개요 및 보안
- `PROJECT_SUMMARY.md` - 프로젝트 전체 요약
- `SECURITY_NOTICE.md` - 보안 주의사항

---

## 🎯 빠른 링크

### 새로 시작하는 팀원이라면:
1. [빠른 시작 가이드](./setup/QUICK_START.md)
2. [팀원 환경 설정](./setup/TEAM_SETUP_GUIDE.md)
3. [Supabase 팀 접근](./team/SUPABASE_TEAM_ACCESS_GUIDE.md)

### 배포를 진행한다면:
1. [Render 배포 가이드](./deployment/RENDER_DEPLOYMENT_GUIDE.md)
2. [배포 체크리스트](./deployment/DEPLOYMENT_CHECKLIST.md)
3. [스키마 업데이트 포함 배포](./deployment/DEPLOYMENT_WITH_SCHEMA_UPDATE.md)

### 데이터베이스 작업을 한다면:
1. [Supabase 설정](./database/SUPABASE_SETUP.md)
2. [데이터베이스 권한 관리](./database/DATABASE_PERMISSION_GUIDE.md)
3. [스키마 업데이트 가이드](./database/SCHEMA_UPDATE_GUIDE.md)

### API 연결 작업을 한다면:
1. [API 연결 가이드](./api/API_CONNECTION_GUIDE.md)
2. [프론트엔드-백엔드 연결](./api/FRONTEND_BACKEND_CONNECTION_GUIDE.md)
3. [연결 테스트](./api/연결_테스트_가이드.md)

---

## 📝 문서 작성 규칙

새로운 문서를 추가할 때는 적절한 카테고리 폴더에 배치해주세요:
- **배포 관련** → `deployment/`
- **초기 설정** → `setup/`
- **데이터베이스** → `database/`
- **팀 협업** → `team/`
- **API 연결** → `api/`
- **작업 보고서** → `reports/`
- **프로젝트 정보** → `project/`

---

## 🔍 문서 검색

모든 문서는 마크다운 형식으로 작성되어 있어 IDE나 GitHub에서 쉽게 검색할 수 있습니다.

- **GitHub**: Repository 내 검색 기능 활용
- **VS Code**: `Ctrl+Shift+F` (전체 검색)
- **명령줄**: `grep -r "검색어" docs/`

---

## 📅 최근 업데이트

- **2025-11-05**: 문서 체계 재정리, 카테고리별 폴더 구조화
- **2025-11-05**: 서버 배포 완료 및 관련 문서 추가

---

**📍 루트 README**: [../README.md](../README.md)

