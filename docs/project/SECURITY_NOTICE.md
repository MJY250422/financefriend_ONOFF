# 🔒 보안 주의사항

> **FinanceFriend 프로젝트의 중요한 보안 규칙**

---

## ⚠️ 절대 Git에 커밋하면 안 되는 파일들

다음 파일들에는 **민감한 정보**가 포함되어 있습니다:

### 1. 환경 변수 파일
```
.env
*.env
system_design/.env
streamlit/.streamlit/secrets.toml
```

### 2. 인증 정보 문서
```
system_design/CREDENTIALS_SETUP.md
```

### 3. 로컬 설정 파일
```
config_local.py
secrets.json
```

---

## ✅ 이미 보호된 파일들

`.gitignore` 파일에 다음이 포함되어 있습니다:

```gitignore
# API keys, credentials, local env
.env
*.env
config_local.py
secrets.json
.streamlit/secrets.toml
system_design/CREDENTIALS_SETUP.md

# 파이썬 캐시파일
__pycache__/
*.pyc
```

---

## 🔍 Git 커밋 전 체크리스트

매번 커밋하기 전에 확인:

```powershell
# Git 상태 확인
git status

# 다음 파일들이 보이면 안 됨:
# - .env
# - CREDENTIALS_SETUP.md
# - secrets.toml
```

---

## 🚨 비밀번호/토큰 유출 시 대응

### 1. 즉시 비밀번호 변경
- Supabase 대시보드 → Settings → Database → "Reset database password"
- OpenAI API 키 등 다른 서비스도 재발급

### 2. Git 히스토리에서 제거 (심각한 경우)
```powershell
# 전문가에게 문의 또는 GitHub 문서 참조
# https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
```

### 3. 팀원에게 알림
- 새 비밀번호 안전하게 공유
- 모두 `.env` 파일 업데이트

---

## 💡 안전하게 비밀번호 공유하는 방법

### 권장 방법 ✅
1. **Slack/Discord DM** (일대일 메시지)
2. **암호화된 이메일**
3. **비밀번호 관리 도구**
   - 1Password
   - LastPass
   - Bitwarden
4. **파일 직접 전달** (USB, AirDrop 등)

### 절대 금지 ❌
1. ~~Public GitHub Repository~~
2. ~~Slack/Discord 단체 채팅방~~
3. ~~GitHub Issues~~
4. ~~공개 문서 (Notion, Google Docs 등)~~
5. ~~일반 이메일 (제목에 비밀번호)~~

---

## 📋 민감한 정보 종류

프로젝트에서 보호해야 하는 정보:

### 데이터베이스
- Supabase 비밀번호
- PostgreSQL 연결 문자열
- 데이터베이스 사용자명

### API 키
- OpenAI API Key
- News API Key
- 기타 외부 서비스 키

### 보안 토큰
- JWT Secret Key
- Session Secret
- CSRF Token

---

## 🎓 팀원 교육

새로운 팀원이 합류하면:

1. 이 문서(`SECURITY_NOTICE.md`) 읽기 필수
2. `.gitignore` 규칙 이해
3. `git status` 확인 습관화
4. 의심스러우면 팀 리더에게 문의

---

## 🔧 보안 검증 스크립트

커밋 전 자동 체크:

```powershell
# 민감한 파일이 staging 영역에 있는지 확인
git diff --cached --name-only | Select-String -Pattern "\.env|CREDENTIALS|secrets\.toml"
```

결과가 없으면 안전, 결과가 있으면 위험!

---

## 📞 보안 문제 발견 시

보안 문제를 발견했다면:

1. **즉시 팀 리더에게 알림**
2. **공개 채널에 게시하지 않음**
3. **빠른 대응 조치**

---

## 📚 추가 참고 자료

- [GitHub: Removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [OWASP: Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Best Practices for API Keys](https://cloud.google.com/docs/authentication/api-keys)

---

## ✅ 보안 서약

모든 팀원은 다음을 준수합니다:

- [ ] `.env` 파일을 Git에 커밋하지 않습니다
- [ ] 비밀번호를 공개 채널에 올리지 않습니다
- [ ] 커밋 전 `git status`로 확인합니다
- [ ] 의심스러운 상황은 즉시 보고합니다
- [ ] 이 보안 규칙을 다른 팀원에게도 알립니다

---

**마지막 업데이트**: 2025.11.04  
**책임자**: 프로젝트 관리자  

**🔐 보안은 모두의 책임입니다!**

