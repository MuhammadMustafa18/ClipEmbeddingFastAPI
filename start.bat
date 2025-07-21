@echo off
echo Starting FastAPI server...
python -m uvicorn main:app --host 127.0.0.1 --port 8000
pause
