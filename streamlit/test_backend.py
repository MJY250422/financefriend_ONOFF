"""
백엔드 API 연동 테스트 페이지
Streamlit 앱에서 백엔드 API를 호출하여 연결을 테스트합니다.
"""
import streamlit as st
from api_client import get_api_client, check_backend_connection
from datetime import datetime


def main():
    st.set_page_config(
        page_title="백엔드 API 테스트",
        page_icon="🧪",
        layout="wide"
    )
    
    st.title("🧪 백엔드 API 연동 테스트")
    st.markdown("---")
    
    # API 클라이언트 초기화
    api_client = get_api_client()
    
    # 사이드바: 연결 상태 확인
    with st.sidebar:
        st.header("⚙️ 설정")
        
        # 백엔드 URL 설정
        backend_url = st.text_input(
            "백엔드 URL",
            value="http://localhost:8000",
            help="백엔드 서버의 URL을 입력하세요"
        )
        
        # 연결 확인 버튼
        if st.button("🔌 연결 확인", type="primary"):
            with st.spinner("백엔드 서버 연결 확인 중..."):
                api_client = get_api_client(backend_url)
                if check_backend_connection(api_client):
                    st.success("✅ 백엔드 서버 연결 성공!")
                else:
                    st.error("❌ 백엔드 서버에 연결할 수 없습니다.")
                    st.info("💡 백엔드 서버가 실행 중인지 확인하세요: `python main.py`")
        
        st.markdown("---")
        st.markdown("### 📚 API 문서")
        st.markdown(f"[Swagger UI]({backend_url}/docs)")
        st.markdown(f"[ReDoc]({backend_url}/redoc)")
    
    # 메인 콘텐츠
    tab1, tab2, tab3, tab4 = st.tabs(["🏥 헬스 체크", "👥 사용자 관리", "📰 뉴스 관리", "💬 대화 관리"])
    
    # Tab 1: 헬스 체크
    with tab1:
        st.header("🏥 헬스 체크")
        
        if st.button("헬스 체크 실행"):
            with st.spinner("헬스 체크 중..."):
                result = api_client.health_check()
                
                if result.get("status") == "healthy":
                    st.success("✅ 서버가 정상적으로 작동 중입니다!")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("상태", result.get("status", "N/A"))
                    with col2:
                        st.metric("버전", result.get("version", "N/A"))
                    with col3:
                        st.metric("메시지", result.get("message", "N/A"))
                else:
                    st.error("❌ 서버 상태 이상")
                
                with st.expander("📋 응답 상세"):
                    st.json(result)
    
    # Tab 2: 사용자 관리
    with tab2:
        st.header("👥 사용자 관리")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📝 사용자 생성")
            with st.form("create_user_form"):
                email = st.text_input("이메일", placeholder="user@example.com")
                password = st.text_input("비밀번호", type="password", placeholder="최소 8자")
                username = st.text_input("사용자명", placeholder="홍길동")
                user_type = st.selectbox("사용자 타입", ["USER", "ADMIN"])
                
                if st.form_submit_button("사용자 생성", type="primary"):
                    if email and password:
                        try:
                            result = api_client.create_user(
                                email=email,
                                password=password,
                                username=username if username else None,
                                user_type=user_type
                            )
                            st.success(f"✅ 사용자 생성 성공! User ID: {result['user_id']}")
                            st.json(result)
                        except Exception as e:
                            st.error(f"❌ 사용자 생성 실패: {e}")
                    else:
                        st.warning("⚠️ 이메일과 비밀번호를 입력해주세요.")
        
        with col2:
            st.subheader("🔍 사용자 조회")
            user_id = st.text_input("사용자 ID", key="user_id_lookup")
            
            if st.button("사용자 조회"):
                if user_id:
                    try:
                        result = api_client.get_user(user_id)
                        st.success("✅ 사용자 조회 성공!")
                        
                        # 사용자 정보 표시
                        st.markdown(f"**이메일:** {result.get('email')}")
                        st.markdown(f"**사용자명:** {result.get('username', 'N/A')}")
                        st.markdown(f"**사용자 타입:** {result.get('user_type')}")
                        st.markdown(f"**생성일:** {result.get('created_at')}")
                        
                        with st.expander("📋 전체 정보"):
                            st.json(result)
                    except Exception as e:
                        st.error(f"❌ 사용자 조회 실패: {e}")
                else:
                    st.warning("⚠️ 사용자 ID를 입력해주세요.")
        
        st.markdown("---")
        st.subheader("📋 사용자 목록")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("사용자 목록 조회", type="primary"):
                try:
                    users = api_client.get_users(limit=10)
                    st.session_state['users'] = users
                except Exception as e:
                    st.error(f"❌ 사용자 목록 조회 실패: {e}")
        
        if 'users' in st.session_state and st.session_state['users']:
            st.success(f"✅ {len(st.session_state['users'])}명의 사용자를 찾았습니다.")
            for user in st.session_state['users']:
                with st.expander(f"👤 {user.get('username', user.get('email'))}"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.markdown(f"**ID:** {user['user_id'][:8]}...")
                        st.markdown(f"**이메일:** {user['email']}")
                    with col2:
                        st.markdown(f"**타입:** {user['user_type']}")
                        st.markdown(f"**생성일:** {user['created_at'][:10]}")
                    with col3:
                        if st.button("활성화", key=f"activate_{user['user_id']}"):
                            try:
                                api_client.activate_user(user['user_id'])
                                st.success("✅ 사용자 활성화 성공!")
                            except Exception as e:
                                st.error(f"❌ 활성화 실패: {e}")
    
    # Tab 3: 뉴스 관리
    with tab3:
        st.header("📰 뉴스 관리")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("📝 뉴스 생성")
            with st.form("create_news_form"):
                title = st.text_input("제목", placeholder="뉴스 제목을 입력하세요")
                url = st.text_input("URL", placeholder="https://example.com/news/1")
                content = st.text_area("본문", placeholder="뉴스 본문을 입력하세요")
                source = st.text_input("출처", placeholder="연합뉴스")
                
                if st.form_submit_button("뉴스 생성", type="primary"):
                    if title and url:
                        try:
                            result = api_client.create_news(
                                title=title,
                                url=url,
                                content=content if content else None,
                                source=source if source else None,
                                published_at=datetime.now()
                            )
                            st.success(f"✅ 뉴스 생성 성공! News ID: {result['news_id']}")
                            st.json(result)
                        except Exception as e:
                            st.error(f"❌ 뉴스 생성 실패: {e}")
                    else:
                        st.warning("⚠️ 제목과 URL을 입력해주세요.")
        
        with col2:
            st.subheader("📋 뉴스 목록")
            
            # 필터 옵션
            col_a, col_b = st.columns(2)
            with col_a:
                limit = st.slider("표시 개수", 5, 50, 10)
            with col_b:
                search_term = st.text_input("검색어", placeholder="제목 검색")
            
            if st.button("뉴스 목록 조회", type="primary"):
                try:
                    news_list = api_client.get_news_list(
                        limit=limit,
                        search=search_term if search_term else None
                    )
                    st.session_state['news_list'] = news_list
                except Exception as e:
                    st.error(f"❌ 뉴스 목록 조회 실패: {e}")
            
            if 'news_list' in st.session_state and st.session_state['news_list']:
                st.success(f"✅ {len(st.session_state['news_list'])}개의 뉴스를 찾았습니다.")
                
                for news in st.session_state['news_list']:
                    with st.expander(f"📰 [{news['news_id']}] {news['title']}"):
                        st.markdown(f"**출처:** {news.get('source', 'N/A')}")
                        st.markdown(f"**URL:** {news['url']}")
                        st.markdown(f"**발행일:** {news.get('published_at', 'N/A')}")
                        
                        if news.get('content'):
                            st.markdown("**본문:**")
                            st.text(news['content'][:200] + "..." if len(news['content']) > 200 else news['content'])
        
        st.markdown("---")
        st.subheader("🔥 인기 뉴스")
        
        if st.button("인기 뉴스 조회"):
            try:
                trending = api_client.get_trending_news(limit=5)
                if trending:
                    st.success(f"✅ {len(trending)}개의 인기 뉴스를 찾았습니다.")
                    for i, news in enumerate(trending, 1):
                        st.markdown(f"{i}. **{news['title']}** (상호작용: {news.get('interaction_count', 0)}회)")
                else:
                    st.info("ℹ️ 인기 뉴스가 없습니다. (상호작용 데이터 필요)")
            except Exception as e:
                st.error(f"❌ 인기 뉴스 조회 실패: {e}")
    
    # Tab 4: 대화 관리
    with tab4:
        st.header("💬 대화 관리")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔐 세션 생성")
            with st.form("create_session_form"):
                session_user_id = st.text_input("사용자 ID", placeholder="User ID를 입력하세요")
                
                if st.form_submit_button("세션 생성", type="primary"):
                    if session_user_id:
                        try:
                            result = api_client.create_session(
                                user_id=session_user_id,
                                context={"device": "web", "browser": "streamlit-test"}
                            )
                            st.success(f"✅ 세션 생성 성공! Session ID: {result['session_id']}")
                            st.session_state['current_session'] = result
                            st.json(result)
                        except Exception as e:
                            st.error(f"❌ 세션 생성 실패: {e}")
                    else:
                        st.warning("⚠️ 사용자 ID를 입력해주세요.")
        
        with col2:
            st.subheader("💭 대화 생성")
            
            if 'current_session' in st.session_state:
                session_id = st.session_state['current_session']['session_id']
                st.info(f"현재 세션: {session_id}")
                
                with st.form("create_dialogue_form"):
                    sender = st.selectbox("발신자", ["USER", "AGENT"])
                    content = st.text_area("내용", placeholder="메시지를 입력하세요")
                    intent = st.text_input("의도", placeholder="greeting, question, response 등")
                    
                    if st.form_submit_button("대화 전송", type="primary"):
                        if content:
                            try:
                                result = api_client.create_dialogue(
                                    session_id=session_id,
                                    sender_type=sender,
                                    content=content,
                                    intent=intent if intent else None
                                )
                                st.success("✅ 대화 생성 성공!")
                                
                                # 세션의 대화 목록 갱신
                                dialogues = api_client.get_session_dialogues(session_id)
                                st.session_state['dialogues'] = dialogues
                            except Exception as e:
                                st.error(f"❌ 대화 생성 실패: {e}")
                        else:
                            st.warning("⚠️ 메시지를 입력해주세요.")
            else:
                st.info("ℹ️ 먼저 세션을 생성해주세요.")
        
        # 대화 목록 표시
        if 'dialogues' in st.session_state and st.session_state['dialogues']:
            st.markdown("---")
            st.subheader("💬 대화 기록")
            
            for dialogue in st.session_state['dialogues']:
                sender = dialogue['sender_type']
                icon = "👤" if sender == "USER" else "🤖"
                
                with st.chat_message(sender.lower()):
                    st.markdown(f"{icon} **{sender}**")
                    st.markdown(dialogue['content'])
                    st.caption(f"{dialogue.get('intent', 'N/A')} | {dialogue['created_at']}")


if __name__ == "__main__":
    main()




