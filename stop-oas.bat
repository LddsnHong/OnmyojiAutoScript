@echo off
color F0
title OAS Backend Stopper
echo Finding OAS backend listening on port 22288 ...

set "found=0"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":22288" ^| findstr /i "LISTENING"') do (
    echo Killing process tree, PID %%a ...
    taskkill /F /T /PID %%a && set "found=1"
)

if "%found%"=="0" (
    echo No OAS backend found on port 22288. Nothing to stop.
) else (
    echo OAS backend stopped.
)
pause
