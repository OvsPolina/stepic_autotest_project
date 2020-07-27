import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")
#    parser.addoption('--browser_name', action='store', default=None,
#                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
#    browser_name = request.config.getoption("browser_name")
#    browser = None
#    if browser_name == "chrome":
 #       browser = webdriver.Chrome()
#    elif browser_name == "firefox":
#        browser = webdriver.Firefox()
#    else:
#        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser=webdriver.Chrome()
    yield browser
    browser.quit()