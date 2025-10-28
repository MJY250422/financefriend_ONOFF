@echo off
chcp 65001 >nul
REM 초기 설정 스크립트

REM Stop all Python processes first
taskkill /F /IM python.exe 2>nul
timeout /t 2 /nobreak >nul

echo ========================================
echo  FinanceFriend Setup
echo ========================================
echo.
echo This script will:
echo  1. Check Python version
echo  2. Install pip (if needed)
echo  3. Install all required packages
echo  4. Verify installation
echo.
echo NOTE: Run this as Administrator if you have permission issues.
echo.
pause

echo.
echo [1/5] Checking Python version...
venv311\Scripts\python.exe --version
if %errorlevel% neq 0 (
    echo.
    echo ERROR: venv311 not found or broken!
    echo Please recreate it with: py -3.11 -m venv venv311
    pause
    exit /b 1
)
echo.

echo [2/5] Checking/Installing pip...
venv311\Scripts\python.exe -m pip --version 2>nul
if %errorlevel% neq 0 (
    echo pip not found, installing...
    venv311\Scripts\python.exe -m ensurepip --upgrade
)
echo.

echo [3/5] Upgrading pip...
venv311\Scripts\python.exe -m pip install --upgrade pip
echo.

echo [4/5] Installing packages...
echo This may take a few minutes...
echo.

venv311\Scripts\python.exe -m pip install fastapi uvicorn sqlalchemy requests python-dotenv pydantic email-validator passlib bcrypt python-multipart

if %errorlevel% neq 0 (
    echo.
    echo ERROR during installation!
    echo.
    echo If you see permission errors:
    echo  1. Close this window
    echo  2. Run CMD as Administrator
    echo  3. Run this script again
    echo.
    pause
    exit /b 1
)
echo.

echo [5/5] Verifying installation...
venv311\Scripts\python.exe -c "import fastapi, uvicorn, sqlalchemy, requests; print('✓ All packages installed successfully!')"

if %errorlevel% neq 0 (
    echo.
    echo Verification failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo  Setup Complete!
echo ========================================
echo.
echo You can now:
echo  1. Start backend: start_backend.bat
echo  2. Create sample data: python create_sample_data.py
echo  3. Start Streamlit: start_streamlit.bat
echo  4. Or start both: run_servers.bat
echo.

pause

