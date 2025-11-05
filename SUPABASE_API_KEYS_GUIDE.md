# 🔑 Supabase API Keys 가이드

**작성일**: 2025.11.05  
**목적**: Supabase URL 및 API Key 확인 및 사용 방법

---

## ⚠️ 먼저 확인하세요!

### 현재 프로젝트에서는 일반적으로 필요 없습니다!

**현재 구조:**
```
프론트엔드 → FastAPI 백엔드 → PostgreSQL
```

**필요한 것:**
- ✅ 백엔드 API URL: `http://localhost:8000` 또는 `https://financefriend-backend.onrender.com`
- ❌ SUPABASE_URL/KEY: 불필요

**Supabase SDK가 필요한 경우에만 이 가이드를 사용하세요!**

---

## 📍 Supabase API 정보 확인

### Step 1: Dashboard 접속

1. https://supabase.com/dashboard 로그인
2. 프로젝트 선택: `financefriend`

### Step 2: API 설정 확인

**좌측 메뉴 → Settings → API**

---

## 🔑 API Keys 종류

### 1. Project URL (SUPABASE_URL)

**위치:** Configuration → API → Project URL

```
https://[PROJECT_REF].supabase.co
```

**예시:**
```
https://abcdefghijklmnop.supabase.co
```

**용도:**
- Supabase 클라이언트 초기화
- 모든 API 요청의 기본 URL

**공유:** ✅ 안전 (공개 가능)

---

### 2. anon / public key (SUPABASE_KEY)

**위치:** Project API keys → anon public

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6...
```

**특징:**
- ✅ 프론트엔드에서 사용 가능
- ✅ 브라우저에 노출 가능
- ✅ Row Level Security(RLS) 적용됨
- ✅ 안전하게 Git에 커밋 가능

**용도:**
- 클라이언트 측에서 Supabase 접근
- 공개 API 호출
- RLS 정책에 따라 데이터 접근 제한

**공유:** ✅ 안전 (팀원에게 공유 가능)

---

### 3. service_role key ⚠️ 주의!

**위치:** Project API keys → service_role secret

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6...
```

**특징:**
- ⚠️ **절대 공개 금지!**
- ⚠️ 모든 RLS 정책 우회
- ⚠️ 전체 데이터베이스 접근 가능
- ⚠️ Git에 절대 커밋 금지

**용도:**
- 백엔드 서버에서만 사용
- 관리자 작업
- 마이그레이션 스크립트

**공유:** ❌ 절대 공유 금지

---

## 💻 사용 예시

### Python에서 사용

#### 설치
```bash
pip install supabase
```

#### 코드
```python
from supabase import create_client, Client

# 환경 변수에서 로드 (권장)
import os
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")  # anon key

# 클라이언트 생성
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# 데이터 조회
response = supabase.table('news').select('*').execute()
print(response.data)

# 데이터 추가
data = supabase.table('news').insert({
    "title": "새 뉴스",
    "url": "https://example.com"
}).execute()

# 데이터 수정
supabase.table('news').update({
    "summary": "업데이트"
}).eq('news_id', 1).execute()
```

### JavaScript에서 사용

#### 설치
```bash
npm install @supabase/supabase-js
```

#### 코드
```javascript
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = process.env.SUPABASE_URL
const supabaseKey = process.env.SUPABASE_KEY  // anon key

const supabase = createClient(supabaseUrl, supabaseKey)

// 데이터 조회
const { data, error } = await supabase
  .from('news')
  .select('*')

// 데이터 추가
const { data, error } = await supabase
  .from('news')
  .insert([
    { title: '새 뉴스', url: 'https://example.com' }
  ])
```

---

## 🔒 환경 변수 설정

### .env 파일

```env
# Supabase (프론트엔드에서 직접 접근 시)
SUPABASE_URL=https://[PROJECT_REF].supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...  # anon key

# ⚠️ service_role key는 백엔드에만!
# SUPABASE_SERVICE_ROLE_KEY=eyJ...  # 절대 프론트엔드에 노출 금지!
```

### .env.example (Git 커밋용)

```env
# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key-here

# Note: Get these from Supabase Dashboard → Settings → API
```

---

## ⚙️ 현재 프로젝트에 적용

### 만약 프론트엔드에서 Supabase를 직접 사용하려면

#### 1. 의존성 추가

**streamlit/requirements.txt:**
```txt
streamlit==1.51.0
pandas==2.3.3
requests==2.32.5
openai==2.7.1
supabase==2.0.0  # 추가
```

#### 2. 환경 변수 설정

**streamlit/.env:**
```env
SUPABASE_URL=https://[PROJECT_REF].supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

#### 3. 클라이언트 생성

**streamlit/supabase_client.py:**
```python
import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def get_supabase_client() -> Client:
    """Supabase 클라이언트 반환"""
    return create_client(SUPABASE_URL, SUPABASE_KEY)
```

#### 4. 사용

```python
from supabase_client import get_supabase_client

supabase = get_supabase_client()
news = supabase.table('news').select('*').execute()
```

---

## 🎯 권장 사항

### ⭐ 현재 프로젝트에서는 FastAPI 백엔드 사용 권장

**이유:**
1. **보안**: 프론트엔드에서 직접 DB 접근 방지
2. **일관성**: 모든 로직이 백엔드에 집중
3. **검증**: 데이터 검증 및 비즈니스 로직 중앙화
4. **로깅**: 모든 요청 추적 가능

**사용:**
```python
# ✅ 권장: FastAPI 백엔드 사용
from api_client import get_api_client

client = get_api_client()
news = client.get_news_list()
```

**사용 안 함:**
```python
# ❌ 권장하지 않음: 직접 DB 접근
from supabase import create_client

supabase = create_client(URL, KEY)
news = supabase.table('news').select('*').execute()
```

---

## 🔍 특수한 경우: Supabase Realtime

만약 **실시간 데이터 구독**이 필요하다면 Supabase SDK 사용 고려:

```python
# 실시간 뉴스 업데이트 구독
def handle_news_changes(payload):
    print(f"New news: {payload}")

supabase.table('news') \
    .on('INSERT', handle_news_changes) \
    .subscribe()
```

이 경우에만 SUPABASE_URL/KEY가 필요합니다.

---

## 📋 정보 공유 체크리스트

### 팀원에게 공유할 정보

- [ ] SUPABASE_URL (공개 가능)
- [ ] SUPABASE_KEY (anon key, 공개 가능)
- [ ] 사용 예시 코드
- [ ] 환경 변수 설정 방법

### 절대 공유하지 말 것

- [ ] ❌ service_role key
- [ ] ❌ 데이터베이스 비밀번호 (DATABASE_URL에 포함)

---

## 🎉 요약

**언제 필요한가?**
- Supabase Python/JS SDK를 직접 사용할 때
- 실시간 구독(Realtime) 사용 시
- 클라이언트에서 직접 DB 접근 시

**어디서 찾나?**
- Supabase Dashboard → Settings → API
- Project URL + anon public key

**안전한가?**
- ✅ URL: 공개 가능
- ✅ anon key: 공개 가능 (RLS 보호)
- ❌ service_role key: 절대 공개 금지!

**현재 프로젝트에서는?**
- 일반적으로 불필요
- FastAPI 백엔드 사용 권장
- 특별한 경우에만 사용

---

**작성일**: 2025.11.05  
**최종 수정**: 2025.11.05

