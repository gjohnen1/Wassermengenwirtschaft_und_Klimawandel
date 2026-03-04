cd ..
echo(
@echo Installation of Python virtual environment
python.exe -m venv venvRTC-Tools
@echo Created virtual environment venvRTC-Tools
echo(
@echo Activating virtual environment
call .\venvRTC-Tools\Scripts\activate
@echo Virtual environment activated
pause

echo(
@echo Installing RTC-Tools (Python package)
python -m pip install rtc-tools rtc-tools-channel-flow rtc-tools-interface > install_rtc-tools_log.txt 2>&1
@echo Installed RTC-Tools, please check log file if installation was successful
pause

