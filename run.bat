@echo off



:: Install required packages
pip install --upgrade pip
pip install -r requirements.txt

:: Run tests
pytest -v -s -m "sanity" --html=Reports/report.html testCases/ --alluredir=allure-results

pause
