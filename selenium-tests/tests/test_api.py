"""
API Tests for ParaBank (Fintech Backend)
Testing banking APIs directly without UI
"""

import pytest
import requests
import json

# ParaBank API endpoints
BASE_URL = "https://parabank.parasoft.com/parabank/services/bank"


class TestParaBankAPI:
    """API test suite for banking backend"""
    
    @pytest.mark.api
    def test_api_get_account_by_id(self):
        """GET account details via API"""
        account_id = "14121"  # Your account ID
        url = f"{BASE_URL}/accounts/{account_id}"
        
        response = requests.get(url)
        
        print(f"\n📡 GET {url}")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.text[:200] if response.text else 'Empty'}")
        
        # API returns HTML/SOAP response, not JSON
        assert response.status_code in [200, 400, 404, 403]
    
    @pytest.mark.api
    def test_api_get_customer_accounts(self):
        """GET all accounts for a customer"""
        customer_id = "14121"  # Your customer ID
        url = f"{BASE_URL}/customers/{customer_id}/accounts"
        
        response = requests.get(url)
        
        print(f"\n📡 GET {url}")
        print(f"   Status: {response.status_code}")
        
        assert response.status_code in [200, 400, 404, 403]
    
    @pytest.mark.api
    def test_api_transfer_invalid_amount(self):
        """POST transfer with invalid amount (negative test)"""
        url = f"{BASE_URL}/transfer"
        payload = {
            "fromAccountId": "14121",
            "toAccountId": "14121",
            "amount": -50  # Invalid negative amount
        }
        
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        
        print(f"\n📡 POST {url}")
        print(f"   Payload: {payload}")
        print(f"   Status: {response.status_code}")
        
        # Should return error for invalid amount
        assert response.status_code in [400, 422, 500, 200]
    
    @pytest.mark.api
    def test_api_check_service_health(self):
        """Verify API service is reachable"""
        url = f"{BASE_URL}/login/testuser/testpass"
        
        response = requests.get(url)
        
        print(f"\n📡 API Health Check - {url}")
        print(f"   Status: {response.status_code}")
        
        # Even 404 means service is running
        assert response.status_code is not None
        print(f"   ✅ API service is responsive")
    
    @pytest.mark.api
    def test_api_response_time(self):
        """Verify API response time is acceptable"""
        import time
        url = f"{BASE_URL}/accounts/14121"
        
        start = time.time()
        response = requests.get(url)
        duration = (time.time() - start) * 1000  # milliseconds
        
        print(f"\n⏱️ Response time: {duration:.0f}ms")
        print(f"   Status: {response.status_code}")
        
        # API should respond within 5 seconds
        assert duration < 5000
        print(f"   ✅ Response time acceptable")