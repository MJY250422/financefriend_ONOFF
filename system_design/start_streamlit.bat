@echo off
REM Streamlit 앱만 실행하는 간단한 스크립트

echo ========================================
echo  Streamlit App 실행
echo ========================================
echo.

REM 가상환경 활성화
call venv311\Scripts\activate.bat

REM Streamlit 디렉토리로 이동
cd ..\streamlit

echo [1/2] Checking backend connection...
curl -s http://localhost:8000/health >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Backend server is not running!
    echo Please start backend first: python main.py
    echo.
    pause
    exit /b
)

echo [OK] Backend is running!
echo.

echo [2/2] Starting Streamlit app...
echo      Opening browser at http://localhost:8501
echo.

REM Streamlit 앱 실행
streamlit run app.py

pause




