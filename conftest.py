import pytest


# Get browser name from arguments, use parser as it is
# this allows to access Python parser to add a new optional parameter
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome ")


# conftest is used to have the fixtures in one place, so this portion was in login_test.py
# this fixture or function will run before, in this case, the module, as that is the scope
@pytest.fixture(scope="module")
def driver(request):
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager

    browser = request.config.getoption("--browser")
    if browser == "chrome":
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        # only this command is needed to download or look the chromedriver, no need for .exe
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    elif browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()
    print("Test completed.")
