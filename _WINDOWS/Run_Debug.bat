@echo off
echo Updating to recent github push
git pull
echo Update complete
echo Clearing screen
cls
echo Starting System core
C:/PY/system/System_Core.py
pause