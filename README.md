# FinanceFriend - AI 기반 금융 뉴스 에이전트

> 실시간 금융 뉴스 수집 및 AI 기반 개인화 추천 시스템

## 프로젝트 개요

FinanceFriend는 금융 뉴스를 자동으로 수집하고, AI 에이전트를 통해 사용자에게 맞춤형 뉴스를 추천하는 시스템입니다.

### 주요 기능

- 📰 **실시간 뉴스 수집**: 다양한 금융 뉴스 소스에서 데이터 수집
- 🤖 **AI 에이전트**: 사용자 질문에 대한 지능형 응답
- 🎯 **개인화 추천**: 사용자 행동 기반 맞춤 뉴스 제공
- 💬 **대화형 인터페이스**: 자연스러운 대화를 통한 정보 제공
- 📊 **사용자 분석**: 뉴스 상호작용 패턴 분석

---

## 기술 스택

### Backend
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white)
![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white)

- FastAPI - 고성능 REST API 프레임워크
- SQLAlchemy - ORM 및 데이터베이스 관리
- Pydantic - 데이터 검증
- Uvicorn - ASGI 웹 서버

### Frontend
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

- Streamlit - 데이터 시각화 및 웹 인터페이스

### Database
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)

- SQLite (개발)
- PostgreSQL (프로덕션 준비)

---

## ⚠️ 보안 주의사항

**시작하기 전에 반드시 읽어주세요!**

📄 **[SECURITY_NOTICE.md](SECURITY_NOTICE.md)** - 민감한 정보 보호 규칙

---

## 빠른 시작

### 필수 요구사항

- Python 3.11+
- PowerShell (Windows)

### 설치 및 실행

```powershell
# 1. 백엔드 서버 시작
cd system_design
python main.py

# 2. 새 터미널에서 Streamlit 앱 시작
streamlit run streamlit/app.py

# 3. 샘플 데이터 생성 (선택)
python create_sample_data.py
```

**더 자세한 가이드**: [`QUICK_START.md`](QUICK_START.md) 참조

---

## 프로젝트 구조

```
financefriend_ONOFF/
├── system_design/          # 백엔드 (FastAPI)
│   ├── main.py            # 메인 애플리케이션
│   ├── database.py        # DB 연결 관리
│   ├── db_schema_design.py # 데이터 모델
│   ├── routers/           # API 엔드포인트
│   └── venv311/           # 가상 환경
├── streamlit/             # 프론트엔드
│   └── app.py            # Streamlit 앱
├── PROJECT_SUMMARY.md     # 📋 상세 작업 내역
├── QUICK_START.md         # 🚀 빠른 시작 가이드
└── README.md             # 📖 프로젝트 소개 (현재 파일)
```

---

## API 엔드포인트

### 주요 API

- `GET /docs` - Swagger UI API 문서
- `GET /health` - 헬스 체크
- `POST /api/v1/users/` - 사용자 생성
- `GET /api/v1/news/` - 뉴스 목록 조회
- `POST /api/v1/dialogues/` - 대화 생성
- `GET /api/v1/sessions/` - 세션 관리

**전체 API 문서**: http://localhost:8000/docs

---

## 주요 작업 내역 (2025.11.03)

### ✅ 완료된 작업

1. **백엔드-프론트엔드 통합**
   - FastAPI와 Streamlit 연결 완료
   - CORS 설정 및 API 통신 검증

2. **데이터베이스 스키마 구현**
   - 8개 테이블 설계 및 구현
   - SQLAlchemy ORM 모델 정의
   - 샘플 데이터 생성 스크립트 작성

3. **문제 해결**
   - UnicodeEncodeError (이모지 인코딩)
   - Enum 타입 불일치
   - SQLite autoincrement 이슈
   - PowerShell 실행 정책

### 📊 생성된 샘플 데이터

- Users: 3명
- News: 10개
- Sessions: 3개
- Dialogues: 6개
- Interactions: 11개

**자세한 내용**: [`PROJECT_SUMMARY.md`](PROJECT_SUMMARY.md) 참조

---

## 데이터베이스 ERD

```
┌──────────┐     ┌──────────────┐     ┌──────┐
│  Users   │────<│  Sessions    │>────│Dialogues│
└──────────┘     └──────────────┘     └──────┘
      │
      │
      ↓
┌─────────────────────┐
│UserNewsInteractions │
└─────────────────────┘
      │
      ↓
┌──────────┐     ┌────────────────┐
│   News   │────<│NewsEmbeddings  │
└──────────┘     └────────────────┘
```

---

## 다음 단계

### 단기 목표
- [ ] 실제 뉴스 API 연동
- [ ] AI 에이전트 구현 (LangChain/OpenAI)
- [ ] 사용자 인증 시스템

### 중기 목표
- [ ] 뉴스 추천 알고리즘 개선
- [ ] 실시간 데이터 업데이트
- [ ] 성능 최적화

### 장기 목표
- [ ] PostgreSQL 전환
- [ ] 프로덕션 배포 (Docker, AWS)
- [ ] 모바일 앱 개발

---

## 팀원 가이드

### 개발 환경 설정
1. Repository 클론
2. 가상 환경 설정: `python -m venv venv311`
3. 의존성 설치: `pip install -r requirements.txt`
4. 환경 변수 설정: `.env` 파일 생성

### 개발 워크플로우
1. 새 브랜치 생성
2. 기능 개발 및 테스트
3. Pull Request 생성
4. 코드 리뷰 후 병합

### 코드 스타일
- PEP 8 준수
- Type hints 사용 권장
- Docstring 작성

---

## 문제 해결

### 자주 발생하는 문제

**Q: 백엔드가 시작되지 않아요**
```powershell
# Python 캐시 삭제
Get-ChildItem -Recurse __pycache__ | Remove-Item -Recurse -Force
```

**Q: 포트가 이미 사용 중입니다**
```powershell
# 프로세스 종료
Get-Process python | Stop-Process -Force
```

**Q: 가상 환경을 활성화할 수 없어요**
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

더 많은 문제 해결 방법: [`PROJECT_SUMMARY.md`](PROJECT_SUMMARY.md#-문제-발생-시)

---

## 라이선스

This project is licensed under the MIT License.

---

## 연락처

프로젝트 관련 문의사항이 있으시면 이슈를 생성해주세요.

---

**최종 업데이트**: 2025.11.03  
**버전**: 1.0.0  
**상태**: ✅ 개발 환경 구축 완료


