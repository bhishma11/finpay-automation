"""
Pytest configuration with command line arguments and fixtures
"""

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def pytest_addoption(parser):
    """Add command line arguments for user configuration"""
    
    parser.addoption("--url", action="store", default="https://parabank.parasoft.com/parabank/index.htm")
    parser.addoption("--username-field", action="store", default="input[name='username']")
    parser.addoption("--password-field", action="store", default="input[name='password']")
    parser.addoption("--login-button", action="store", default="input[value='Log In']")
    parser.addoption("--dashboard-indicator", action="store", default="#accountTable")
    parser.addoption("--error-message", action="store", default=".error")
    parser.addoption("--headless", action="store_true", default=False)
    
    
@pytest.fixture(scope="session")
def config(request):
    """Provide user configuration to all tests"""
    return {
        "url": request.config.getoption("--url"),
        "selectors": {
            "username": request.config.getoption("--username-field"),
            "password": request.config.getoption("--password-field"),
            "login_button": request.config.getoption("--login-button"),
            "dashboard_indicator": request.config.getoption("--dashboard-indicator"),
            "error_message": request.config.getoption("--error-message"),
        },
        "headless": request.config.getoption("--headless"),
    }


@pytest.fixture(scope="function")
def driver(config):
    """WebDriver fixture using Selenium Manager (automatic driver download)"""
    
    options = Options()
    
    if config["headless"]:
        options.add_argument("--headless=new")
    
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    
    driver.implicitly_wait(10)
    
    yield driver
    
    # Keep browser open for 30 seconds so you can see the result
    print("\n📸 Browser closing in 15 seconds...")
    time.sleep(15)
    
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None)
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshots/failure_{item.name}_{timestamp}.png"
            driver.save_screenshot(filename)
            print(f"\n📸 Screenshot saved: {filename}")


def pytest_configure(config):
    """Register custom markers to avoid warnings"""
    config.addinivalue_line("markers", "ui: UI tests - marks tests as UI automation")
    config.addinivalue_line("markers", "api: API tests - marks tests as API testing")
    config.addinivalue_line("markers", "smoke: Smoke tests - fast validation tests")
    config.addinivalue_line("markers", "regression: Regression tests - full test suite")
    config.addinivalue_line("markers", "slow: Slow running tests - takes more time")

