from selenium import webdriver
import pytest
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser == "edge":
        driver=webdriver.Edge()
    else:
        driver = webdriver.Chrome() #default browser
    return driver

def pytest_addoption(parser):
    parser.addoption('--browser')
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

### hooks for html report

# conftest.py

def pytest_metadata(metadata):
    metadata['Project Name'] = 'Test Demo'
    metadata['Module Name'] = 'Login'
    metadata['Tester'] = 'Shaik'
    return metadata


