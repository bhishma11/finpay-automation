"""
Transfer Funds Page Object for ParaBank
"""

from pages.base_page import BasePage
import time
import logging

logger = logging.getLogger(__name__)


class TransferPage(BasePage):
    """Page Object for fund transfers"""
    
    def __init__(self, driver, config):
        super().__init__(driver, config)
    
    def get_from_accounts(self):
        """Get list of available from accounts"""
        try:
            from_options = "#fromAccountId option"
            return self.get_all_texts(from_options)
        except:
            return []
    
    def get_to_accounts(self):
        """Get list of available to accounts"""
        try:
            to_options = "#toAccountId option"
            return self.get_all_texts(to_options)
        except:
            return []
    
    def select_from_account(self, account_number: str):
        """Select source account"""
        try:
            from_account = f"#fromAccountId option[value='{account_number}']"
            if self.is_visible(from_account, timeout=3):
                self.click(from_account)
        except:
            # Try selecting by index 0
            self.click("#fromAccountId")
        time.sleep(1)
        return self
    
    def select_to_account(self, account_number: str):
        """Select destination account"""
        try:
            to_account = f"#toAccountId option[value='{account_number}']"
            if self.is_visible(to_account, timeout=3):
                self.click(to_account)
        except:
            self.click("#toAccountId")
        time.sleep(1)
        return self
    
    def enter_amount(self, amount: float):
        """Enter transfer amount"""
        self.input_text("#amount", str(amount))
        return self
    
    def submit_transfer(self):
        """Submit transfer form"""
        self.click("input[value='Transfer']")
        time.sleep(3)
        return self
    
    def transfer(self, from_account: str, to_account: str, amount: float):
        """Complete transfer flow"""
        self.select_from_account(from_account)
        self.select_to_account(to_account)
        self.enter_amount(amount)
        self.submit_transfer()
        
        if self.is_visible(".title", timeout=5):
            success_text = self.get_text(".title")
            if "Transfer Complete" in success_text:
                logger.info(f"✅ Transfer complete: ${amount}")
                return True
        return False
    
    def get_success_message(self) -> str:
        if self.is_visible(".title"):
            return self.get_text(".title")
        return ""