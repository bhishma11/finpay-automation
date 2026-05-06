"""
Dashboard Page Object for ParaBank (Fintech)
"""

from pages.base_page import BasePage
import time


class DashboardPage(BasePage):
    """Page Object for banking dashboard"""
    
    def __init__(self, driver, config):
        super().__init__(driver, config)
        self.dashboard_indicator = config["selectors"]["dashboard_indicator"]
    
    def is_loaded(self) -> bool:
        """Check if dashboard loaded"""
        return self.is_visible(self.dashboard_indicator)
    
    def get_account_balance(self, account_index=0) -> str:
        """Get balance from account table"""
        balance_selector = "#accountTable tbody tr td:nth-child(2)"
        try:
            balances = self.get_all_texts(balance_selector)
            if balances and len(balances) > account_index:
                return balances[account_index]
        except:
            pass
        return ""
    
    def get_first_account_id(self) -> str:
        """Get the first account ID from the table"""
        try:
            account_selector = "#accountTable tbody tr td:nth-child(1) a"
            if self.is_visible(account_selector, timeout=5):
                return self.get_text(account_selector)
        except:
            pass
        return ""
    
    def click_transfer_funds(self):
        """Navigate to Transfer Funds page using XPath"""
        transfer_link = "//a[text()='Transfer Funds']"
        self.click_by_xpath(transfer_link)
        time.sleep(2)
        from pages.transfer_page import TransferPage
        return TransferPage(self.driver, self.config)
    
    def click_open_new_account(self):
        """Navigate to Open New Account page"""
        open_account_link = "//a[text()='Open New Account']"
        self.click_by_xpath(open_account_link)
        time.sleep(2)
        return self
    
    def click_account_activity(self):
        """Navigate to Account Activity page"""
        activity_link = "//a[text()='Account Activity']"
        self.click_by_xpath(activity_link)
        time.sleep(2)
        return self
    
    def click_logout(self):
        """Log out of banking portal"""
        logout_link = "//a[text()='Log Out']"
        self.click_by_xpath(logout_link)
        time.sleep(2)
        from pages.login_page import LoginPage
        return LoginPage(self.driver, self.config)