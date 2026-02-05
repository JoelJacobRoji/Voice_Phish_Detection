@echo off
echo ========================================
echo   Audio Call Analyzer - Startup
echo ========================================
echo.

cd /d "%~dp0"

echo [1/3] Starting Backend Server...
start "Backend Server" cmd /k ".venv\Scripts\python.exe -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000"
timeout /t 3 /nobreak >nul

echo [2/3] Starting Frontend Server...
start "Frontend Server" cmd /k ".venv\Scripts\python.exe serve_frontend.py"
timeout /t 2 /nobreak >nul

echo [3/3] Opening Browser...
start http://localhost:3000/index.html

echo.
echo ========================================
echo   Servers Started Successfully!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Press any key to stop all servers...
pause >nul

echo.
echo Stopping servers...
taskkill /FI "WINDOWTITLE eq Backend Server*" /T /F >nul 2>&1
taskkill /FI "WINDOWTITLE eq Frontend Server*" /T /F >nul 2>&1
echo Done!
