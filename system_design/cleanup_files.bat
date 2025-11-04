@echo off
chcp 65001 >nul
REM 불필요한 파일 정리

echo ========================================
echo  Cleaning Up Unnecessary Files
echo ========================================
echo.

echo This will delete temporary/debug scripts.
echo Core files will be kept.
echo.
set /p confirm="Continue? (Y/N): "
if /i not "%confirm%"=="Y" (
    echo Cancelled.
    pause
    exit /b
)

echo.
echo Deleting debug and test files...

del /q check_environment.bat 2>nul
del /q check_python_path.bat 2>nul
del /q create_sample_data_direct.bat 2>nul
del /q debug_install.bat 2>nul
del /q diagnose_venv.bat 2>nul
del /q fix_installation.bat 2>nul
del /q fix_pip.bat 2>nul
del /q force_use_venv.bat 2>nul
del /q fresh_install.bat 2>nul
del /q install_missing_packages.bat 2>nul
del /q install_packages.bat 2>nul
del /q install_simple.bat 2>nul
del /q install_with_retry.bat 2>nul
del /q kill_python_processes.bat 2>nul
del /q ONE_COMMAND.bat 2>nul
del /q quick_test.bat 2>nul
del /q recreate_venv.bat 2>nul
del /q recreate_venv_simple.bat 2>nul
del /q run_backend_direct.bat 2>nul
del /q test_imports.bat 2>nul

echo.
echo ========================================
echo  Cleanup Complete!
echo ========================================
echo.
echo Deleted temporary files.
echo.
echo Remaining essential files:
echo  - setup.bat (NEW - setup everything)
echo  - start_backend.bat
echo  - start_streamlit.bat / start_streamlit.ps1
echo  - run_servers.bat / run_servers.ps1
echo  - create_sample_data.py
echo  - test_integration.py
echo.

pause




