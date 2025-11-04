@echo off
REM 백엔드 서버만 실행하는 스크립트

echo ========================================
echo  Backend Server 실행
echo ========================================
echo.

REM .env 파일 확인
if not exist .env (
    echo [WARNING] .env file not found!
    echo Copying .env.example to .env...
    echo.
    copy .env.example .env
    echo [OK] .env file created!
    echo Please check the settings and run again if needed.
    echo.
)

REM 가상환경 활성화
call venv311\Scripts\activate.bat

echo [INFO] Starting backend server on http://localhost:8000
echo [INFO] API docs available at http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

REM 백엔드 서버 실행
python main.py

pause




