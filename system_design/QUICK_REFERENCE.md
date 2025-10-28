# ⚡ 빠른 참조 가이드

> **전체 상세 내용**: `DEVELOPMENT_ISSUES_LOG.md` 참조

---

## 🚀 처음 시작하는 팀원

```bash
# 1. Python 3.11 설치 확인
py -3.11 --version

# 2. 가상환경 생성
py -3.11 -m venv venv311

# 3. 초기 설정 (관리자 권한 CMD)
setup.bat

# 4. 백엔드 실행
start_backend.bat

# 5. 샘플 데이터 (새 터미널)
venv311\Scripts\python.exe create_sample_data.py

# 6. Streamlit (새 터미널)
start_streamlit.bat
```

---

## ⚠️ 주요 주의사항

### ❌ 절대 금지
- Python 3.14 사용 (호환성 문제)
- venv311 활성화 없이 패키지 설치
- 일반 권한으로 setup.bat 실행 (권한 에러 가능)

### ✅ 필수 사항
- **Python 3.11.x** 사용
- 관리자 권한으로 초기 설정
- SQLite 사용 (개발용)

---

## 🐛 문제 해결 치트시트

| 문제 | 해결 |
|------|------|
| `No module named 'fastapi'` | `setup.bat` 실행 |
| 권한 에러 | `taskkill /F /IM python.exe` 후 재시도 |
| venv311 손상 | `rmdir /s /q venv311` → `py -3.11 -m venv venv311` |
| Python 3.14 사용됨 | `venv311\Scripts\python.exe` 직접 사용 |
| 포트 충돌 | `netstat -ano | findstr :8000` → `taskkill /PID [PID] /F` |

---

## 📁 핵심 파일

- `setup.bat` - 초기 설정 ⭐
- `start_backend.bat` - 백엔드 실행
- `start_streamlit.bat` - Streamlit 실행
- `.env.example` - 환경 설정 복사 후 사용

---

## 🔗 접속 URL

- Streamlit: http://localhost:8501
- 백엔드 API: http://localhost:8000
- API 문서: http://localhost:8000/docs

---

## 📚 상세 문서

- **DEVELOPMENT_ISSUES_LOG.md** - 전체 문제 해결 과정
- **README_SIMPLE.md** - 사용 가이드
- **TROUBLESHOOTING.md** - 문제 해결

---

**💡 Tip**: 문제 발생 시 `DEVELOPMENT_ISSUES_LOG.md`의 "5.2 자주 발생하는 문제" 참조!


