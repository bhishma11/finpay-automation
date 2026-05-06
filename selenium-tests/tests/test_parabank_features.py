"""
ParaBank Banking Features Tests - Complete Suite
"""

import pytest
import time
from pages.login_page import LoginPage


class TestParaBankFeatures:
    """Test suite for all ParaBank banking features"""
    
    @pytest.fixture
    def dashboard(self, driver, config):
        login_page = LoginPage(driver, config)
        login_page.load()
        time.sleep(2)
        dashboard = login_page.login("testqa2026", "Test@123")
        time.sleep(2)
        print(f"\n✅ Logged in successfully")
        return dashboard
    
    # ============ ACCOUNTS OVERVIEW TESTS ============
    
    @pytest.mark.ui
    def test_account_overview_table_exists(self, dashboard):
        """Verify Accounts Overview table is displayed"""
        print(f"\n📋 Checking Accounts Overview...")
        assert dashboard.is_loaded()
        print(f"✅ Accounts Overview table is visible")
    
    @pytest.mark.ui
    def test_account_balance_displayed(self, dashboard):
        """Verify account balance is visible"""
        balance = dashboard.get_account_balance()
        print(f"\n💰 Account Balance: {balance}")
        assert balance is not None and balance != ""
        print(f"✅ Balance verification passed")
    
    @pytest.mark.ui
    def test_account_id_displayed(self, dashboard):
        """Verify account ID is visible"""
        account_id = dashboard.get_first_account_id()
        print(f"\n🏦 Account ID: {account_id}")
        assert account_id is not None and account_id != ""
        print(f"✅ Account ID verification passed")
    
    # ============ TRANSFER FUNDS TESTS ============
    
    @pytest.mark.ui
    def test_navigate_to_transfer_funds(self, dashboard, driver):
        """Navigate to Transfer Funds page"""
        print(f"\n📋 Navigating to Transfer Funds...")
        transfer_page = dashboard.click_transfer_funds()
        time.sleep(2)
        print(f"📍 Current URL: {driver.current_url}")
        assert "transfer" in driver.current_url.lower()
        print(f"✅ Successfully navigated to Transfer Funds page")
    
    @pytest.mark.ui
    def test_transfer_page_has_from_accounts(self, dashboard):
        """Transfer page should have From Account dropdown"""
        transfer_page = dashboard.click_transfer_funds()
        time.sleep(2)
        from_accounts = transfer_page.get_from_accounts()
        print(f"\n📋 From Account options: {from_accounts}")
        assert len(from_accounts) > 0
        print(f"✅ From Account dropdown has {len(from_accounts)} option(s)")
    
    @pytest.mark.ui
    def test_transfer_page_has_to_accounts(self, dashboard):
        """Transfer page should have To Account dropdown"""
        transfer_page = dashboard.click_transfer_funds()
        time.sleep(2)
        to_accounts = transfer_page.get_to_accounts()
        print(f"\n📋 To Account options: {to_accounts}")
        assert len(to_accounts) > 0
        print(f"✅ To Account dropdown has {len(to_accounts)} option(s)")
    
    @pytest.mark.ui
    def test_amount_field_exists(self, dashboard):
        """Transfer page should have Amount input field"""
        transfer_page = dashboard.click_transfer_funds()
        time.sleep(2)
        assert transfer_page.is_visible("#amount")
        print(f"\n💰 Amount input field is present")
        print(f"✅ Amount field verification passed")
    
    # ============ OPEN NEW ACCOUNT TESTS ============
    
    @pytest.mark.ui
    def test_open_new_account_page(self, dashboard, driver):
        """Navigate to Open New Account page"""
        print(f"\n📋 Navigating to Open New Account...")
        dashboard.click_by_xpath("//a[text()='Open New Account']")
        time.sleep(2)
        print(f"📍 Current URL: {driver.current_url}")
        assert "openaccount" in driver.current_url.lower()
        print(f"✅ Successfully navigated to Open New Account page")
    
    # ============ BILL PAYMENT TESTS ============
    
    @pytest.mark.ui
    def test_bill_pay_page(self, dashboard, driver):
        """Navigate to Bill Pay page"""
        print(f"\n📋 Navigating to Bill Pay...")
        dashboard.click_by_xpath("//a[text()='Bill Pay']")
        time.sleep(2)
        print(f"📍 Current URL: {driver.current_url}")
        assert "billpay" in driver.current_url.lower()
        print(f"✅ Successfully navigated to Bill Pay page")
    
    # ============ FIND TRANSACTIONS TESTS ============
    
    @pytest.mark.ui
    def test_find_transactions_page(self, dashboard, driver):
        """Navigate to Find Transactions page"""
        print(f"\n📋 Navigating to Find Transactions...")
        dashboard.click_by_xpath("//a[text()='Find Transactions']")
        time.sleep(2)
        print(f"📍 Current URL: {driver.current_url}")
        assert "findtrans" in driver.current_url.lower()
        print(f"✅ Successfully navigated to Find Transactions page")
    
    # ============ UPDATE PROFILE TESTS ============
    
    @pytest.mark.ui
    def test_update_profile_page(self, dashboard, driver):
        """Navigate to Update Contact Info page"""
        print(f"\n📋 Navigating to Update Contact Info...")
        dashboard.click_by_xpath("//a[text()='Update Contact Info']")
        time.sleep(2)
        print(f"📍 Current URL: {driver.current_url}")
        assert "updateprofile" in driver.current_url.lower()
        print(f"✅ Successfully navigated to Update Profile page")
    
    # ============ LOAN REQUEST TESTS ============
    
    @pytest.mark.ui
    def test_request_loan_page(self, dashboard, driver):
        """Navigate to Request Loan page"""
        print(f"\n📋 Navigating to Request Loan...")
        dashboard.click_by_xpath("//a[text()='Request Loan']")
        time.sleep(2)
        print(f"📍 Current URL: {driver.current_url}")
        assert "requestloan" in driver.current_url.lower()
        print(f"✅ Successfully navigated to Loan Request page")