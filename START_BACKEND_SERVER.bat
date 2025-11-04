@echo off
echo ========================================
echo 백엔드 서버 시작
echo ========================================
echo.

cd system_design

echo 가상환경 활성화 중...
call venv311\Scripts\activate.bat

echo.
echo 백엔드 서버 실행 중...
echo.
echo 서버 주소: http://localhost:8000
echo API 문서: http://localhost:8000/docs
echo.
echo 서버를 중지하려면 Ctrl+C를 누르세요.
echo.

python main.py

pause

