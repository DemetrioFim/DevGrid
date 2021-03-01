@echo off

cd /D "%~dp0"

python -m virtualenv venv
call venv\Scripts\activate
pip install -r requirements.txt -U
call python test_app.py
call venv\Scripts\deactivate
