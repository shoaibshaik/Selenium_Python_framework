@echo off

:: Create virtual env if needed
if not exist ".venv\" (
    python -m venv .venv
)

:: Activate the environment
call .venv\Scripts\activate.bat

:: Install required packages
pip install --upgrade pip
pip install -r requirements.txt

:: Run tests
pytest -v -s -m "sanity" --html=Reports/report.html testCases/ --alluredir=allure-results

pause
