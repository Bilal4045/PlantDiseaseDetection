@echo off
setlocal
cd /d "%~dp0"

if not exist "venv\Scripts\python.exe" (
  echo Virtual environment not found. Create it with: py -m venv venv
  exit /b 1
)

venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload