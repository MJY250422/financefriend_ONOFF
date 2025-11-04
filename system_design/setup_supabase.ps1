# Supabase 설정 자동화 스크립트
# PowerShell 스크립트

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Supabase PostgreSQL 설정 스크립트" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# 1. 가상 환경 확인
Write-Host "[1/5] 가상 환경 확인 중..." -ForegroundColor Yellow
if (Test-Path "venv311\Scripts\Activate.ps1") {
    Write-Host "✅ 가상 환경 발견" -ForegroundColor Green
    & ".\venv311\Scripts\Activate.ps1"
} else {
    Write-Host "⚠️  가상 환경을 찾을 수 없습니다" -ForegroundColor Red
    Write-Host "   먼저 가상 환경을 생성하세요: python -m venv venv311" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# 2. psycopg2-binary 설치
Write-Host "[2/5] PostgreSQL 드라이버 설치 중..." -ForegroundColor Yellow
pip install psycopg2-binary --quiet
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ psycopg2-binary 설치 완료" -ForegroundColor Green
} else {
    Write-Host "❌ 설치 실패" -ForegroundColor Red
    exit 1
}

Write-Host ""

# 3. .env 파일 생성
Write-Host "[3/5] .env 파일 확인 중..." -ForegroundColor Yellow
if (Test-Path ".env") {
    Write-Host "⚠️  .env 파일이 이미 존재합니다" -ForegroundColor Yellow
    $response = Read-Host "덮어쓰시겠습니까? (y/N)"
    if ($response -ne "y" -and $response -ne "Y") {
        Write-Host "   .env 파일 유지" -ForegroundColor Cyan
    } else {
        Copy-Item "env_template.txt" ".env" -Force
        Write-Host "✅ .env 파일 생성 완료" -ForegroundColor Green
    }
} else {
    Copy-Item "env_template.txt" ".env"
    Write-Host "✅ .env 파일 생성 완료" -ForegroundColor Green
}

Write-Host ""

# 4. .env 파일 수정 안내
Write-Host "[4/5] .env 파일 수정 필요" -ForegroundColor Yellow
Write-Host ""
Write-Host "다음 단계를 진행하세요:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Supabase 가입 및 프로젝트 생성" -ForegroundColor White
Write-Host "   → https://supabase.com" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Settings → Database → Connection String 복사" -ForegroundColor White
Write-Host ""
Write-Host "3. .env 파일 열기:" -ForegroundColor White
Write-Host "   notepad .env" -ForegroundColor Gray
Write-Host ""
Write-Host "4. DATABASE_URL 수정:" -ForegroundColor White
Write-Host "   DATABASE_URL=postgresql://postgres:[PASSWORD]@db.[PROJECT_REF].supabase.co:5432/postgres" -ForegroundColor Gray
Write-Host ""

$response = Read-Host ".env 파일 수정을 완료하셨나요? (y/N)"
if ($response -ne "y" -and $response -ne "Y") {
    Write-Host ""
    Write-Host "설정을 완료한 후 다시 실행하세요:" -ForegroundColor Yellow
    Write-Host "  .\setup_supabase.ps1" -ForegroundColor Cyan
    exit 0
}

Write-Host ""

# 5. 연결 테스트
Write-Host "[5/5] 데이터베이스 연결 테스트 중..." -ForegroundColor Yellow
Write-Host ""
python test_supabase_connection.py

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "🎉 Supabase 설정 완료!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "다음 명령어로 서버를 시작하세요:" -ForegroundColor Cyan
    Write-Host "  python main.py" -ForegroundColor White
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "❌ 연결 테스트 실패" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "문제 해결 방법은 SUPABASE_SETUP.md를 참고하세요" -ForegroundColor Yellow
    Write-Host ""
    exit 1
}

