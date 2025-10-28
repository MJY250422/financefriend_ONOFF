@echo off
REM 백엔드와 Streamlit 서버를 동시에 실행하는 배치 스크립트

echo ========================================
echo  FinanceFriend 통합 서버 실행
echo ========================================
echo.

REM .env 파일 확인
if not exist .env (
    echo [경고] .env 파일이 없습니다.
    echo .env.example 파일을 .env로 복사하고 설정을 수정하세요.
    echo.
    copy .env.example .env
    echo .env 파일이 생성되었습니다. 필요한 설정을 수정한 후 다시 실행하세요.
    pause
    exit /b
)

echo [1/3] 가상환경 활성화 중...
call venv311\Scripts\activate.bat

echo.
echo [2/3] 백엔드 서버 실행 중... (포트: 8000)
echo      백엔드 로그는 이 창에 표시됩니다.
echo.
start "백엔드 서버 (FastAPI)" cmd /k "call venv311\Scripts\activate.bat && python main.py"

REM 백엔드 서버가 시작될 시간 대기
timeout /t 5 /nobreak > nul

echo.
echo [3/3] Streamlit 앱 실행 중... (포트: 8501)
echo      Streamlit은 자동으로 브라우저에서 열립니다.
echo.
start "Streamlit 앱" cmd /k "call venv311\Scripts\activate.bat && cd ..\streamlit && streamlit run app.py"

echo.
echo ========================================
echo  ✅ 서버 실행 완료!
echo ========================================
echo.
echo  📡 백엔드 API: http://localhost:8000
echo  📚 API 문서: http://localhost:8000/docs
echo  🖥️  Streamlit 앱: http://localhost:8501
echo.
echo  서버를 중지하려면 각 창을 닫으세요.
echo ========================================
echo.
pause

