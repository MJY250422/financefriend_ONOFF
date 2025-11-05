# 팀원용 서버 접속 정보 (FinanceFriend)

> **즉시 사용 가능한 접속 정보**

---

## 🌐 당신의 서버 정보

### 서버 IP 주소
```
192.168.80.78
```

### 네트워크 정보
- **서브넷**: 255.255.255.0
- **게이트웨이**: 192.168.80.1
- **네트워크**: 같은 WiFi/LAN (192.168.80.x)에 연결 필요

---

## 📡 팀원 접속 URL

### Base URL
```
http://192.168.80.78:8000
```

### API 문서 (Swagger UI)
```
http://192.168.80.78:8000/docs
```

### Health Check
```
http://192.168.80.78:8000/health
```

### ReDoc UI
```
http://192.168.80.78:8000/redoc
```

---

## 🔗 주요 API 엔드포인트

### 뉴스 API
```
GET  http://192.168.80.78:8000/api/v1/news/
POST http://192.168.80.78:8000/api/v1/news/
GET  http://192.168.80.78:8000/api/v1/news/{news_id}
```

### 사용자 API
```
GET  http://192.168.80.78:8000/api/v1/users/
POST http://192.168.80.78:8000/api/v1/users/
GET  http://192.168.80.78:8000/api/v1/users/{user_id}
```

### 세션 API
```
GET  http://192.168.80.78:8000/api/v1/sessions/
POST http://192.168.80.78:8000/api/v1/sessions/
```

### 대화 API
```
GET  http://192.168.80.78:8000/api/v1/dialogues/
POST http://192.168.80.78:8000/api/v1/dialogues/
```

---

## 🧪 즉시 테스트하기

### 브라우저에서
1. 브라우저 열기
2. 주소창에 입력:
   ```
   http://192.168.80.78:8000/docs
   ```
3. Swagger UI가 보이면 성공! ✅

### PowerShell에서
```powershell
# Health Check
Invoke-WebRequest -Uri "http://192.168.80.78:8000/health"

# 뉴스 목록
Invoke-WebRequest -Uri "http://192.168.80.78:8000/api/v1/news/"
```

### Python에서
```python
import requests

# Health Check
response = requests.get("http://192.168.80.78:8000/health")
print(response.json())

# 뉴스 목록
response = requests.get("http://192.168.80.78:8000/api/v1/news/")
print(response.json())
```

---

## ⚠️ 팀원 필수 조건

### 1. 같은 네트워크 연결
```
팀원도 같은 WiFi에 연결되어야 합니다.
네트워크: 192.168.80.x (게이트웨이: 192.168.80.1)
```

### 2. 서버 실행 중
```
당신의 컴퓨터에서 서버가 실행되어 있어야 합니다.
python main.py
```

### 3. 방화벽 설정 (필요 시)
```powershell
# 8000번 포트 허용 (관리자 권한)
netsh advfirewall firewall add rule name="FastAPI Server" dir=in action=allow protocol=TCP localport=8000
```

---

## 🎨 Streamlit 앱 (프론트엔드)

### 접속 URL
```
http://192.168.80.78:8501
```

### 설정 필요
Streamlit 앱의 API 클라이언트 설정:
```python
# streamlit/api_client.py 또는 config.py
API_BASE_URL = "http://192.168.80.78:8000"
```

---

## 📤 팀원에게 보낼 메시지

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FinanceFriend 백엔드 서버 접속 정보
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌐 Base URL:
   http://192.168.80.78:8000

📚 API 문서 (Swagger):
   http://192.168.80.78:8000/docs

❤️ Health Check:
   http://192.168.80.78:8000/health

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ 중요:
1. 같은 WiFi에 연결되어야 함
2. 내 컴퓨터에서 서버 실행 중
3. 포트: 8000

🧪 테스트:
브라우저에서 접속 → Swagger UI 확인

❓ 문제 발생 시:
- WiFi 연결 확인
- 서버 실행 확인 (나에게 연락)
- TEAM_SERVER_INFO.md 참고

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🔧 설정 완료 체크리스트

### 서버 관리자 (당신)
- [x] IP 주소 확인 완료 (192.168.80.78)
- [ ] 서버 실행 중 (`python main.py`)
- [ ] Health Check 테스트 완료
- [ ] 방화벽 8000번 포트 허용
- [ ] 팀원에게 접속 정보 전달

### 팀원
- [ ] 같은 WiFi 연결 (192.168.80.x)
- [ ] 브라우저에서 http://192.168.80.78:8000/docs 접속 테스트
- [ ] API 호출 테스트
- [ ] 문제 발생 시 서버 관리자에게 연락

---

## 🚀 지금 바로 실행

### 1. 방화벽 설정 (관리자 권한 PowerShell)
```powershell
netsh advfirewall firewall add rule name="FastAPI Server" dir=in action=allow protocol=TCP localport=8000
```

### 2. 서버 시작
```powershell
cd system_design
.\venv311\Scripts\Activate.ps1
python main.py
```

### 3. 자체 테스트
```powershell
# 브라우저 열기
start http://192.168.80.78:8000/docs
```

### 4. 팀원에게 전달
위 "팀원에게 보낼 메시지" 복사해서 전송!

---

## 📊 빠른 참조 카드

```
┌─────────────────────────────────────────┐
│  FinanceFriend Backend Server           │
├─────────────────────────────────────────┤
│  IP:        192.168.80.78               │
│  Port:      8000                        │
│  Protocol:  HTTP                        │
├─────────────────────────────────────────┤
│  Swagger:   /docs                       │
│  ReDoc:     /redoc                      │
│  Health:    /health                     │
├─────────────────────────────────────────┤
│  Network:   192.168.80.0/24             │
│  Gateway:   192.168.80.1                │
└─────────────────────────────────────────┘
```

---

**최종 업데이트**: 2025.11.04  
**서버 IP**: 192.168.80.78  
**포트**: 8000  
**상태**: ✅ 준비 완료

