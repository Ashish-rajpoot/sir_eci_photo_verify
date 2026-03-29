@echo off
setlocal

REM ====== CONFIG ======
set "REPO_URL=https://github.com/Ashish-rajpoot/sir_eci_photo_verify.git"
set "PROJECT_NAME=sir_eci_photo_verify"

REM folder where this .bat file exists
set "BASE_DIR=%~dp0"
set "BASE_DIR=%BASE_DIR:~0,-1%"

set "PROJECT_PATH=%BASE_DIR%\%PROJECT_NAME%"

REM ====== GO TO BASE DIRECTORY ======
cd /d "%BASE_DIR%"

REM ====== CLONE ONLY IF NOT ALREADY PRESENT ======
if not exist "%PROJECT_PATH%" (
    echo Cloning repository...
    git clone %REPO_URL%
) else (
    echo Project already exists at:
    echo %PROJECT_PATH%
)

REM ====== OPEN VS CODE ======
echo Opening VS Code...
code "%PROJECT_PATH%"

REM ====== SMALL DELAY ======
timeout /t 3 /nobreak >nul
echo Now hit the cmd's given on readme file in step Run 2: Cmd's
endlocal
pause