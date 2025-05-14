@echo off

:: Activate the virtual environment
call C:\Users\shaik\PycharmProjects\Selenium_Python_Demo\.venv\Scripts\activate.bat

:: Run pytest with the desired options
pytest -v -s -m "sanity" --html=Reports/report.html testCases/ --browser chrome

:: Pause to keep the console window open
pause

rem pytest -v -s -m 'regression' --html=Reports/report.html testCases/
rem pytest -v -s -m 'sanity and regression' --html=Reports/report.html testCases/
rem pytest -v -s -m 'sanity or regression' --html=Reports/report.html testCases/