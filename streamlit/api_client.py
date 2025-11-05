"""
백엔드 API 클라이언트 모듈
Streamlit 앱에서 백엔드 API를 호출하기 위한 클래스
"""
import requests
import os
from typing import Optional, List, Dict, Any
from datetime import datetime
import streamlit as st


# ========== 백엔드 URL 설정 ==========
# 환경 변수로 자동 전환 가능
# 로컬 개발: export BACKEND_URL=http://localhost:8000
# Render 배포: export BACKEND_URL=https://financefriend-backend.onrender.com

DEFAULT_BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "https://financefriend-onoff-backend.onrender.com"  # 기본값: Render 배포 서버
)

# 로컬 개발 시에는 아래 주석을 해제하고 위를 주석 처리하세요:
# DEFAULT_BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")


class BackendAPIClient:
    """백엔드 API 클라이언트"""
    
    def __init__(self, base_url: str = DEFAULT_BACKEND_URL):
        """
        Args:
            base_url: 백엔드 API 기본 URL (기본값: 환경 변수 또는 Render 서버)
        """
        self.base_url = base_url
        self.api_v1 = f"{base_url}/api/v1"
        
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """
        API 응답 처리
        
        Args:
            response: requests 응답 객체
            
        Returns:
            JSON 응답 데이터
            
        Raises:
            Exception: API 에러 발생 시
        """
        if response.status_code >= 400:
            try:
                error_detail = response.json()
                raise Exception(f"API Error {response.status_code}: {error_detail.get('detail', 'Unknown error')}")
            except:
                raise Exception(f"API Error {response.status_code}: {response.text}")
        
        return response.json()
    
    # ========== 헬스 체크 ==========
    
    def health_check(self) -> Dict[str, Any]:
        """서버 헬스 체크"""
        try:
            response = requests.get(f"{self.base_url}/health", timeout=5)
            return self._handle_response(response)
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    # ========== 사용자 관리 ==========
    
    def create_user(self, email: str, password: str, username: Optional[str] = None, 
                   user_type: str = "user") -> Dict[str, Any]:
        """
        새 사용자 생성
        
        Args:
            email: 이메일
            password: 비밀번호
            username: 사용자명 (선택)
            user_type: 사용자 타입 (기본: user) - 가능한 값: "user", "admin", "guest", "premium"
            
        Returns:
            생성된 사용자 정보
        """
        response = requests.post(
            f"{self.api_v1}/users/",
            json={
                "email": email,
                "password": password,
                "username": username,
                "user_type": user_type
            }
        )
        return self._handle_response(response)
    
    def get_user(self, user_id: str) -> Dict[str, Any]:
        """
        사용자 정보 조회
        
        Args:
            user_id: 사용자 ID
            
        Returns:
            사용자 정보
        """
        response = requests.get(f"{self.api_v1}/users/{user_id}")
        return self._handle_response(response)
    
    def get_users(self, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
        """
        사용자 목록 조회
        
        Args:
            skip: 건너뛸 레코드 수
            limit: 최대 반환 레코드 수
            
        Returns:
            사용자 목록
        """
        response = requests.get(
            f"{self.api_v1}/users/",
            params={"skip": skip, "limit": limit}
        )
        return self._handle_response(response)
    
    def activate_user(self, user_id: str) -> Dict[str, Any]:
        """
        사용자 활성화 (마지막 활동 시간 업데이트)
        
        Args:
            user_id: 사용자 ID
            
        Returns:
            업데이트된 사용자 정보
        """
        response = requests.post(f"{self.api_v1}/users/{user_id}/activate")
        return self._handle_response(response)
    
    # ========== 세션 관리 ==========
    
    def create_session(self, user_id: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        """
        새 세션 생성
        
        Args:
            user_id: 사용자 ID
            context: 세션 컨텍스트 (선택)
            
        Returns:
            생성된 세션 정보
        """
        response = requests.post(
            f"{self.api_v1}/sessions/",
            json={"user_id": user_id, "context": context}
        )
        return self._handle_response(response)
    
    def get_session(self, session_id: int) -> Dict[str, Any]:
        """
        세션 정보 조회
        
        Args:
            session_id: 세션 ID
            
        Returns:
            세션 정보
        """
        response = requests.get(f"{self.api_v1}/sessions/{session_id}")
        return self._handle_response(response)
    
    def get_user_sessions(self, user_id: str, active_only: bool = True) -> List[Dict[str, Any]]:
        """
        사용자의 세션 목록 조회
        
        Args:
            user_id: 사용자 ID
            active_only: 활성 세션만 조회 (기본: True)
            
        Returns:
            세션 목록
        """
        response = requests.get(
            f"{self.api_v1}/sessions/user/{user_id}",
            params={"active_only": active_only}
        )
        return self._handle_response(response)
    
    # ========== 뉴스 관리 ==========
    
    def create_news(self, title: str, url: str, content: Optional[str] = None,
                   source: Optional[str] = None, published_at: Optional[datetime] = None) -> Dict[str, Any]:
        """
        새 뉴스 생성
        
        Args:
            title: 뉴스 제목
            url: 뉴스 URL
            content: 뉴스 본문 (선택)
            source: 뉴스 출처 (선택)
            published_at: 발행 시간 (선택)
            
        Returns:
            생성된 뉴스 정보
        """
        data = {
            "title": title,
            "url": url,
            "content": content,
            "source": source
        }
        if published_at:
            data["published_at"] = published_at.isoformat()
            
        response = requests.post(f"{self.api_v1}/news/", json=data)
        return self._handle_response(response)
    
    def get_news_list(self, skip: int = 0, limit: int = 20, 
                     source: Optional[str] = None, search: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        뉴스 목록 조회
        
        Args:
            skip: 건너뛸 레코드 수
            limit: 최대 반환 레코드 수
            source: 출처 필터 (선택)
            search: 제목 검색 (선택)
            
        Returns:
            뉴스 목록
        """
        params = {"skip": skip, "limit": limit}
        if source:
            params["source"] = source
        if search:
            params["search"] = search
            
        response = requests.get(f"{self.api_v1}/news/", params=params)
        return self._handle_response(response)
    
    def get_news(self, news_id: int) -> Dict[str, Any]:
        """
        뉴스 상세 조회
        
        Args:
            news_id: 뉴스 ID
            
        Returns:
            뉴스 정보
        """
        response = requests.get(f"{self.api_v1}/news/{news_id}")
        return self._handle_response(response)
    
    def get_news_with_interactions(self, news_id: int, user_id: Optional[str] = None) -> Dict[str, Any]:
        """
        상호작용 정보를 포함한 뉴스 조회
        
        Args:
            news_id: 뉴스 ID
            user_id: 사용자 ID (선택)
            
        Returns:
            뉴스 정보 (상호작용 포함)
        """
        params = {}
        if user_id:
            params["user_id"] = user_id
            
        response = requests.get(f"{self.api_v1}/news/{news_id}/with-interactions", params=params)
        return self._handle_response(response)
    
    def get_trending_news(self, limit: int = 10, hours: int = 24) -> List[Dict[str, Any]]:
        """
        인기 뉴스 조회
        
        Args:
            limit: 최대 반환 레코드 수
            hours: 시간 범위
            
        Returns:
            인기 뉴스 목록
        """
        response = requests.get(
            f"{self.api_v1}/news/trending/",
            params={"limit": limit, "hours": hours}
        )
        return self._handle_response(response)
    
    def create_interaction(self, news_id: int, user_id: str, interaction_type: str) -> Dict[str, Any]:
        """
        뉴스 상호작용 생성
        
        Args:
            news_id: 뉴스 ID
            user_id: 사용자 ID
            interaction_type: 상호작용 타입 - 가능한 값: "click", "view", "share", "like", "bookmark", "comment"
            
        Returns:
            생성된 상호작용 정보
        """
        response = requests.post(
            f"{self.api_v1}/news/{news_id}/interactions",
            json={"news_id": news_id, "interaction_type": interaction_type},
            params={"user_id": user_id}
        )
        return self._handle_response(response)
    
    def get_user_interactions(self, user_id: str, interaction_type: Optional[str] = None,
                             skip: int = 0, limit: int = 50) -> List[Dict[str, Any]]:
        """
        사용자의 뉴스 상호작용 이력 조회
        
        Args:
            user_id: 사용자 ID
            interaction_type: 상호작용 타입 필터 (선택)
            skip: 건너뛸 레코드 수
            limit: 최대 반환 레코드 수
            
        Returns:
            상호작용 목록
        """
        params = {"skip": skip, "limit": limit}
        if interaction_type:
            params["interaction_type"] = interaction_type
            
        response = requests.get(f"{self.api_v1}/news/user/{user_id}/interactions", params=params)
        return self._handle_response(response)
    
    # ========== 대화 관리 ==========
    
    def create_dialogue(self, session_id: int, sender_type: str, content: str,
                       intent: Optional[str] = None) -> Dict[str, Any]:
        """
        대화 생성
        
        Args:
            session_id: 세션 ID
            sender_type: 발신자 타입 - 가능한 값: "user", "assistant", "system"
            content: 대화 내용
            intent: 의도 (선택)
            
        Returns:
            생성된 대화 정보
        """
        response = requests.post(
            f"{self.api_v1}/dialogues/",
            json={
                "session_id": session_id,
                "sender_type": sender_type,
                "content": content,
                "intent": intent
            }
        )
        return self._handle_response(response)
    
    def get_session_dialogues(self, session_id: int, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
        """
        세션의 대화 목록 조회
        
        Args:
            session_id: 세션 ID
            skip: 건너뛸 레코드 수
            limit: 최대 반환 레코드 수
            
        Returns:
            대화 목록
        """
        response = requests.get(
            f"{self.api_v1}/dialogues/session/{session_id}",
            params={"skip": skip, "limit": limit}
        )
        return self._handle_response(response)


# ========== Streamlit 통합 헬퍼 ==========

@st.cache_resource
def get_api_client(base_url: str = DEFAULT_BACKEND_URL) -> BackendAPIClient:
    """
    API 클라이언트 싱글톤 (Streamlit 캐시 사용)
    
    Args:
        base_url: 백엔드 API 기본 URL (기본값: 환경 변수 또는 Render 서버)
        
    Returns:
        BackendAPIClient 인스턴스
    """
    return BackendAPIClient(base_url)


def check_backend_connection(client: BackendAPIClient) -> bool:
    """
    백엔드 연결 확인
    
    Args:
        client: API 클라이언트
        
    Returns:
        연결 성공 여부
    """
    try:
        health = client.health_check()
        return health.get("status") == "healthy"
    except:
        return False




