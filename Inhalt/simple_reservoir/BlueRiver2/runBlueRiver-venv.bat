@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
pushd "%SCRIPT_DIR%src"

set "VENV_ACT=%SCRIPT_DIR%..\..\..\venvRTC-Tools\Scripts\activate.bat"
if not exist "%VENV_ACT%" (
    set "VENV_ACT=%SCRIPT_DIR%..\..\venvRTC-Tools\Scripts\activate.bat"
)

if not exist "%VENV_ACT%" (
    echo Could not find venv activation script.
    echo Checked:
    echo   %SCRIPT_DIR%..\..\..\venvRTC-Tools\Scripts\activate.bat
    echo   %SCRIPT_DIR%..\..\venvRTC-Tools\Scripts\activate.bat
    popd
    pause
    exit /b 1
)

call "%VENV_ACT%"
python ".\BlueRiver.py" > "..\venv-log.txt" 2>&1

popd
pause
exit /b
