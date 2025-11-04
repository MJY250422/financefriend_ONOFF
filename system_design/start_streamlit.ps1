# Streamlit 앱만 실행하는 PowerShell 스크립트
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Streamlit App Launcher" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$venvPath = Join-Path $PSScriptRoot "venv311\Scripts\Activate.ps1"
$streamlitPath = Join-Path $PSScriptRoot "..\streamlit"

# Check backend connection
Write-Host "[1/2] Checking backend connection..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:8000/health" -Method Get -TimeoutSec 3 -ErrorAction Stop
    Write-Host "[OK] Backend is running!" -ForegroundColor Green
} catch {
    Write-Host "[WARNING] Backend server is not running!" -ForegroundColor Red
    Write-Host "Please start backend first: python main.py" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit
}

Write-Host ""
Write-Host "[2/2] Starting Streamlit app..." -ForegroundColor Green
Write-Host "      Opening browser at http://localhost:8501" -ForegroundColor Gray
Write-Host ""

# Activate virtual environment and run Streamlit
Set-Location $streamlitPath
& $venvPath
streamlit run app.py

Read-Host "Press Enter to exit"




