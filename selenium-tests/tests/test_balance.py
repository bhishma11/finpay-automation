"""
Account balance tests for ParaBank (Fintech)
"""

import pytest
import time
from pages.login_page import LoginPage


class TestAccountBalance:
    """Test suite for account balance"""
    
    @pytest.fixture
    def dashboard(self, driver, config):
        login_page = LoginPage(driver, config)
        login_page.load()
        time.sleep(2)
        return login_page.login("testqa2026", "Test@123")
    
    @pytest.mark.ui
    def test_balance_displays(self, dashboard):
        """Account balance should be visible"""
        balance = dashboard.get_account_balance()
        print(f"\n💰 Account Balance: {balance}")
        assert balance is not None and balance != ""
    
    @pytest.mark.ui
    def test_account_id_exists(self, dashboard):
        """Account ID should be displayed"""
        account_id = dashboard.get_first_account_id()
        print(f"\n🏦 Account ID: {account_id}")
        assert account_id is not None and account_id != ""