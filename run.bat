@echo off

:: Activate the virtual environment
call venv\Scripts\activate.bat

:: Optional: print Python location
where python

:: Run the tests
pytest -v -s -m "sanity" --html=Reports/report.html testCases/ --browser chrome

pause
