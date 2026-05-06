"""
Base Page Object with common methods
All page objects inherit from this class
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import time


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.wait = WebDriverWait(driver, 20)
        self.short_wait = WebDriverWait(driver, 5)
    
    def click(self, selector: str, retry: bool = True):
        """Click element using CSS selector"""
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
            element.click()
        except Exception as e:
            if retry:
                self.click(selector, retry=False)
            else:
                raise
    
    def click_by_xpath(self, xpath: str, retry: bool = True):
        """Click element using XPath"""
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
        except Exception as e:
            if retry:
                self.click_by_xpath(xpath, retry=False)
            else:
                raise
    
    def input_text(self, selector: str, text: str, clear_first: bool = True):
        """Type text into input field"""
        element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        if clear_first:
            element.clear()
        element.send_keys(text)
    
    def get_text(self, selector: str) -> str:
        """Get text content of element"""
        element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        return element.text
    
    def get_all_texts(self, selector: str) -> list:
        """Get text from all matching elements"""
        elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
        return [el.text for el in elements if el.text]
    
    def is_visible(self, selector: str, timeout: int = 5) -> bool:
        """Check if element is visible"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
            )
            return True
        except TimeoutException:
            return False
    
    def take_screenshot(self, name: str = "screenshot") -> str:
        """Take screenshot for debugging"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        return filename
    
    def wait_for_page_load(self):
        """Wait for page to fully load"""
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )