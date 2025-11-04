@echo off
echo ========================================
echo 프론트엔드 (Streamlit) 앱 시작
echo ========================================
echo.

echo Conda 환경 활성화 중...
call conda activate financial_friend_minzero

cd streamlit

echo.
echo Streamlit 앱 실행 중...
echo.
echo 앱 주소: http://localhost:8501
echo.
echo 앱을 중지하려면 Ctrl+C를 누르세요.
echo.

streamlit run app.py

pause

