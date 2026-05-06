"""
Login functionality tests for ParaBank (Fintech)
"""

import pytest
import time
from pages.login_page import LoginPage


class TestLogin:
    """Test suite for banking login"""
    
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_valid_login(self, driver, config):
        """Valid user should log in successfully"""
        login_page = LoginPage(driver, config)
        login_page.load()
        
        time.sleep(2)
        
        result = login_page.login("testqa2026", "Test@123")
        
        time.sleep(2)
        
        if hasattr(result, 'is_loaded'):
            assert result.is_loaded()
            print(f"\n✅ Login successful! URL: {driver.current_url}")
        else:
            assert False, "Login failed"
    
    @pytest.mark.ui
    def test_invalid_password(self, driver, config):
        """Invalid password should show error"""
        login_page = LoginPage(driver, config)
        login_page.load()
        
        time.sleep(2)
        
        login_page.login("testqa2026", "wrongpassword")
        
        time.sleep(1)
        
        assert login_page.is_error_displayed()
        error = login_page.get_error_message()
        print(f"\n✅ Error displayed: {error}")
    
    @pytest.mark.ui
    def test_empty_credentials(self, driver, config):
        """Empty username and password should show error"""
        login_page = LoginPage(driver, config)
        login_page.load()
        
        time.sleep(2)
        
        login_page.login("", "")
        
        time.sleep(1)
        
        # ParaBank shows error for empty fields
        assert login_page.is_error_displayed()
        print("\n✅ Empty credentials validation works")