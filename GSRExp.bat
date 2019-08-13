REM start C:\neulog\neulog.exe
C:
CD C:\Users\RichardHall\python-virtual-env\NeulogProcssEnv\Scripts
call activate.bat
chdir /d D:\Summer Research\Pain Syc\PySensor
echo Press Enter key to start python script
pause 
python ReadSerial.py
