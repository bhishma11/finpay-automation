"""
Login Page Object
"""

from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage


class LoginPage(BasePage):
    """Page Object for login page"""
    
    def __init__(self, driver, config):
        super().__init__(driver, config)
        self.url = config["url"]
        self.username_field = config["selectors"]["username"]
        self.password_field = config["selectors"]["password"]
        self.login_button = config["selectors"]["login_button"]
        self.error_selector = config["selectors"]["error_message"]
    
    def load(self):
        """Navigate to login page"""
        self.driver.get(self.url)
        self.wait_for_page_load()
        return self
    
    def enter_username(self, username: str):
        self.input_text(self.username_field, username)
        return self
    
    def enter_password(self, password: str):
        self.input_text(self.password_field, password)
        return self
    
    def click_login(self):
        self.click(self.login_button)
        self.wait_for_page_load()
        return self
    
    def login(self, username: str, password: str):
        """Complete login flow"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
        dashboard_selector = self.config["selectors"]["dashboard_indicator"]
        if self.is_visible(dashboard_selector, timeout=5):
            return DashboardPage(self.driver, self.config)
        return self
    
    def get_error_message(self) -> str:
        if self.is_visible(self.error_selector):
            return self.get_text(self.error_selector)
        return ""
    
    def is_error_displayed(self) -> bool:
        return self.is_visible(self.error_selector)