"""
금융 뉴스 도우미 - 메인 애플리케이션 (백엔드 연동 버전)
"""
import streamlit as st
from api_client import get_api_client, check_backend_connection
from datetime import datetime


def main():
    st.set_page_config(
        page_title="금융 뉴스 도우미",
        page_icon="📰",
        layout="wide"
    )
    
    # 사이드바: 백엔드 연결 설정
    with st.sidebar:
        st.header("⚙️ 백엔드 설정")
        
        backend_url = st.text_input(
            "백엔드 URL",
            value="http://localhost:8000",
            help="백엔드 서버 주소"
        )
        
        # API 클라이언트 초기화
        api_client = get_api_client(backend_url)
        
        # 연결 상태 확인
        if st.button("🔌 연결 확인"):
            with st.spinner("백엔드 연결 확인 중..."):
                if check_backend_connection(api_client):
                    st.success("✅ 백엔드 연결 성공!")
                else:
                    st.error("❌ 백엔드에 연결할 수 없습니다.")
                    st.info("💡 백엔드 서버를 먼저 실행하세요: `python main.py`")
        
        st.markdown("---")
        st.markdown("### 📚 도움말")
        st.markdown("""
        **사용 방법:**
        1. 백엔드 서버 실행
        2. 연결 확인 버튼 클릭
        3. 뉴스 조회 및 상호작용
        """)
    
    # 메인 콘텐츠
    st.title("📰 금융 뉴스 도우미")
    st.markdown("백엔드 API와 연동된 금융 뉴스 서비스입니다.")
    st.markdown("---")
    
    # 탭 구성
    tab1, tab2, tab3, tab4 = st.tabs(["📰 뉴스 목록", "🔥 인기 뉴스", "💬 챗봇", "👤 사용자 관리"])
    
    # Tab 1: 뉴스 목록
    with tab1:
        st.header("📰 최신 뉴스")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            search_query = st.text_input("🔍 검색", placeholder="뉴스 제목 검색...")
        
        with col2:
            limit = st.selectbox("표시 개수", [5, 10, 20, 50], index=1)
        
        if st.button("뉴스 조회", type="primary"):
            with st.spinner("뉴스를 불러오는 중..."):
                try:
                    news_list = api_client.get_news_list(
                        limit=limit,
                        search=search_query if search_query else None
                    )
                    
                    if news_list:
                        st.success(f"✅ {len(news_list)}개의 뉴스를 찾았습니다.")
                        
                        for news in news_list:
                            with st.container():
                                col_a, col_b = st.columns([4, 1])
                                
                                with col_a:
                                    st.markdown(f"### 📰 {news.get('title', '제목 없음')}")
                                    published = news.get('published_at')
                                    published_date = published[:10] if published else 'N/A'
                                    st.markdown(f"**출처:** {news.get('source', 'N/A')} | **발행일:** {published_date}")
                                    
                                    if news.get('content'):
                                        with st.expander("📄 본문 보기"):
                                            st.write(news['content'])
                                
                                with col_b:
                                    st.metric("뉴스 ID", news['news_id'])
                                    if st.button("🔗 링크", key=f"link_{news['news_id']}"):
                                        st.write(f"[뉴스 보기]({news['url']})")
                                
                                st.markdown("---")
                    else:
                        st.info("ℹ️ 뉴스가 없습니다. 샘플 데이터를 생성하세요.")
                        st.code("python create_sample_data.py")
                
                except Exception as e:
                    st.error(f"❌ 뉴스 조회 실패: {e}")
                    st.info("💡 백엔드 서버가 실행 중인지 확인하세요.")
    
    # Tab 2: 인기 뉴스
    with tab2:
        st.header("🔥 인기 뉴스")
        st.markdown("최근 24시간 내 가장 많은 상호작용이 있었던 뉴스입니다.")
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            trending_limit = st.slider("표시 개수", 5, 20, 10)
            hours = st.slider("시간 범위", 1, 72, 24)
        
        if st.button("인기 뉴스 조회", type="primary"):
            with st.spinner("인기 뉴스를 불러오는 중..."):
                try:
                    trending_news = api_client.get_trending_news(limit=trending_limit, hours=hours)
                    
                    if trending_news:
                        st.success(f"✅ {len(trending_news)}개의 인기 뉴스를 찾았습니다.")
                        
                        for i, news in enumerate(trending_news, 1):
                            with st.container():
                                col_a, col_b = st.columns([5, 1])
                                
                                with col_a:
                                    st.markdown(f"### {i}. 📰 {news.get('title', '제목 없음')}")
                                    st.markdown(f"**출처:** {news.get('source', 'N/A')}")
                                
                                with col_b:
                                    st.metric("상호작용", f"{news.get('interaction_count', 0)}회")
                                
                                st.markdown("---")
                    else:
                        st.info("ℹ️ 인기 뉴스가 없습니다. 상호작용 데이터가 필요합니다.")
                
                except Exception as e:
                    st.error(f"❌ 인기 뉴스 조회 실패: {e}")
    
    # Tab 3: 챗봇
    with tab3:
        st.header("💬 금융 뉴스 챗봇")
        
        st.info("💡 챗봇 기능은 세션이 필요합니다. 먼저 사용자를 생성하고 세션을 시작하세요.")
        
        # 세션 상태 초기화
        if 'session_id' not in st.session_state:
            st.session_state.session_id = None
        if 'user_id' not in st.session_state:
            st.session_state.user_id = None
        if 'messages' not in st.session_state:
            st.session_state.messages = []
        
        # 세션 시작
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔐 세션 시작")
            user_id_input = st.text_input("사용자 ID", placeholder="User ID를 입력하세요")
            
            if st.button("세션 시작"):
                if user_id_input:
                    try:
                        session = api_client.create_session(
                            user_id=user_id_input,
                            context={"device": "web", "app": "streamlit"}
                        )
                        st.session_state.session_id = session['session_id']
                        st.session_state.user_id = user_id_input
                        st.success(f"✅ 세션이 시작되었습니다! (ID: {session['session_id']})")
                    except Exception as e:
                        st.error(f"❌ 세션 시작 실패: {e}")
                else:
                    st.warning("⚠️ 사용자 ID를 입력하세요.")
        
        with col2:
            if st.session_state.session_id:
                st.subheader("📊 세션 정보")
                st.success(f"**세션 ID:** {st.session_state.session_id}")
                st.info(f"**사용자 ID:** {st.session_state.user_id}")
        
        # 채팅 인터페이스
        if st.session_state.session_id:
            st.markdown("---")
            st.subheader("💬 대화")
            
            # 메시지 표시
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
            
            # 메시지 입력
            if prompt := st.chat_input("메시지를 입력하세요..."):
                # 사용자 메시지 표시
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)
                
                # 백엔드에 대화 저장
                try:
                    api_client.create_dialogue(
                        session_id=st.session_state.session_id,
                        sender_type="user",
                        content=prompt
                    )
                    
                    # 에이전트 응답 (임시)
                    response = f"'{prompt}'에 대한 답변입니다. (실제 AI 에이전트는 구현 예정)"
                    
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    with st.chat_message("assistant"):
                        st.markdown(response)
                    
                    # 에이전트 응답도 저장
                    api_client.create_dialogue(
                        session_id=st.session_state.session_id,
                        sender_type="assistant",
                        content=response
                    )
                
                except Exception as e:
                    st.error(f"❌ 대화 저장 실패: {e}")
    
    # Tab 4: 사용자 관리
    with tab4:
        st.header("👤 사용자 관리")
        
        # 사용자 생성
        st.subheader("✨ 새 사용자 생성")
        
        with st.form("create_user_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                new_email = st.text_input("이메일 *", placeholder="example@email.com")
                new_username = st.text_input("사용자명", placeholder="홍길동")
            
            with col2:
                new_password = st.text_input("비밀번호 *", type="password", placeholder="최소 8자")
                new_password_confirm = st.text_input("비밀번호 확인 *", type="password")
            
            user_type_select = st.selectbox(
                "사용자 타입",
                ["user", "admin", "guest", "premium"],
                help="user: 일반 사용자, admin: 관리자, guest: 게스트, premium: 프리미엄"
            )
            
            submitted = st.form_submit_button("🚀 사용자 생성", type="primary")
            
            if submitted:
                # 유효성 검사
                if not new_email or not new_password:
                    st.error("❌ 이메일과 비밀번호는 필수입니다!")
                elif len(new_password) < 8:
                    st.error("❌ 비밀번호는 최소 8자 이상이어야 합니다!")
                elif new_password != new_password_confirm:
                    st.error("❌ 비밀번호가 일치하지 않습니다!")
                else:
                    try:
                        with st.spinner("사용자 생성 중..."):
                            user = api_client.create_user(
                                email=new_email,
                                password=new_password,
                                username=new_username if new_username else None,
                                user_type=user_type_select
                            )
                            
                            st.success(f"✅ 사용자가 생성되었습니다!")
                            st.balloons()
                            
                            # 생성된 사용자 정보 표시
                            created = user.get('created_at')
                            created_display = created[:19] if created else 'N/A'
                            st.info(f"""
                            **사용자 ID:** {user['user_id']}  
                            **이메일:** {user['email']}  
                            **사용자명:** {user.get('username', 'N/A')}  
                            **타입:** {user['user_type']}  
                            **생성일:** {created_display}
                            """)
                            
                            # 사용자 ID를 클립보드에 복사할 수 있도록 표시
                            st.code(user['user_id'])
                            st.caption("💡 위의 사용자 ID를 복사해서 챗봇 탭에서 사용하세요!")
                    
                    except Exception as e:
                        st.error(f"❌ 사용자 생성 실패: {e}")
                        if "already registered" in str(e).lower():
                            st.warning("⚠️ 이미 등록된 이메일입니다. 다른 이메일을 사용하세요.")
        
        # 사용자 목록 조회
        st.markdown("---")
        st.subheader("📋 사용자 목록")
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            show_users = st.button("사용자 목록 조회", type="secondary")
        
        with col2:
            limit_users = st.slider("표시 개수", 5, 50, 10, key="user_limit")
        
        if show_users:
            try:
                with st.spinner("사용자 목록을 불러오는 중..."):
                    users = api_client.get_users(limit=limit_users)
                    
                    if users:
                        st.success(f"✅ {len(users)}명의 사용자를 찾았습니다.")
                        
                        # 테이블 형식으로 표시
                        import pandas as pd
                        
                        users_data = []
                        for user in users:
                            created = user.get('created_at')
                            created_date = created[:10] if created else 'N/A'
                            users_data.append({
                                "사용자 ID": user['user_id'],
                                "이메일": user['email'],
                                "사용자명": user.get('username', 'N/A'),
                                "타입": user['user_type'],
                                "생성일": created_date
                            })
                        
                        df = pd.DataFrame(users_data)
                        st.dataframe(df, use_container_width=True, hide_index=True)
                        
                        # 개별 사용자 상세 정보
                        with st.expander("🔍 사용자 상세 정보"):
                            for i, user in enumerate(users, 1):
                                created = user.get('created_at')
                                created_display = created[:19] if created else 'N/A'
                                last_active = user.get('last_active_at')
                                last_active_display = last_active[:19] if last_active else 'N/A'
                                st.markdown(f"""
                                **{i}. {user.get('username', user['email'])}**
                                - **ID:** `{user['user_id']}`
                                - **이메일:** {user['email']}
                                - **타입:** {user['user_type']}
                                - **생성일:** {created_display}
                                - **최근 활동:** {last_active_display}
                                """)
                                st.markdown("---")
                    else:
                        st.info("ℹ️ 등록된 사용자가 없습니다.")
            
            except Exception as e:
                st.error(f"❌ 사용자 목록 조회 실패: {e}")
    
    # 하단 정보
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>금융 뉴스 도우미 v1.0 | 백엔드 API 연동</p>
        <p>📚 <a href='http://localhost:8000/docs' target='_blank'>API 문서</a> | 
           🧪 <a href='http://localhost:8501' target='_blank'>테스트 페이지</a></p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()




