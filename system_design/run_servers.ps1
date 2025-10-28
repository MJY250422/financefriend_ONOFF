# PowerShell 스크립트: 백엔드와 Streamlit 서버를 동시에 실행
# UTF-8 인코딩 설정
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " FinanceFriend Integration Server" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# .env file check
if (-Not (Test-Path ".env")) {
    Write-Host "[WARNING] .env file not found." -ForegroundColor Yellow
    Write-Host "Copying .env.example to .env..." -ForegroundColor Yellow
    Write-Host ""
    Copy-Item ".env.example" ".env"
    Write-Host ".env file created successfully!" -ForegroundColor Green
    Write-Host "Please modify settings if needed and run again." -ForegroundColor Green
    Write-Host ""
    Read-Host "Press Enter to continue"
    exit
}

Write-Host "[1/3] Setting up virtual environment..." -ForegroundColor Green
$venvPath = Join-Path $PSScriptRoot "venv311\Scripts\Activate.ps1"
$streamlitPath = Join-Path $PSScriptRoot "..\streamlit"

Write-Host ""
Write-Host "[2/3] Starting backend server... (Port: 8000)" -ForegroundColor Green
Write-Host "      Backend logs will be shown in a new window." -ForegroundColor Gray
Write-Host ""

# Start backend server
Start-Process powershell -ArgumentList @"
    -NoExit
    -Command & {
        [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
        Set-Location '$PSScriptRoot'
        & '$venvPath'
        Write-Host 'Starting Backend Server...' -ForegroundColor Cyan
        python main.py
    }
"@

# Wait for backend to initialize
Write-Host "Waiting for backend to initialize..." -ForegroundColor Gray
Start-Sleep -Seconds 5

Write-Host ""
Write-Host "[3/3] Starting Streamlit app... (Port: 8501)" -ForegroundColor Green
Write-Host "      Streamlit will open in your browser automatically." -ForegroundColor Gray
Write-Host ""

# Start Streamlit app
Start-Process powershell -ArgumentList @"
    -NoExit
    -Command & {
        [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
        Set-Location '$streamlitPath'
        & '$venvPath'
        Write-Host 'Starting Streamlit App...' -ForegroundColor Cyan
        streamlit run app.py
    }
"@

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Servers Started Successfully!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host " Backend API: http://localhost:8000" -ForegroundColor White
Write-Host " API Docs: http://localhost:8000/docs" -ForegroundColor White
Write-Host " Streamlit App: http://localhost:8501" -ForegroundColor White
Write-Host ""
Write-Host " To stop servers, close each PowerShell window." -ForegroundColor Gray
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Read-Host "Press Enter to continue"

