import pytest
import time
from pages.login_page import LoginPage

@pytest.fixture
def dashboard(driver, config):
    login_page = LoginPage(driver, config)
    login_page.load()
    time.sleep(2)
    dashboard = login_page.login("testqa2026", "Test@123")
    time.sleep(2)
    return dashboard

def test_find_transactions_link(dashboard, driver):
    print("\n📋 Clicking Find Transactions...")
    dashboard.click_by_xpath("//a[text()='Find Transactions']")
    time.sleep(2)
    print(f"📍 URL: {driver.current_url}")
    assert "findtrans" in driver.current_url.lower()
    print("✅ PASSED")

def test_bill_pay_link(dashboard, driver):
    print("\n📋 Clicking Bill Pay...")
    dashboard.click_by_xpath("//a[text()='Bill Pay']")
    time.sleep(2)
    print(f"📍 URL: {driver.current_url}")
    assert "billpay" in driver.current_url.lower()
    print("✅ PASSED")