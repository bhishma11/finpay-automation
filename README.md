# 🏦 FinPay Automation Framework

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.16-green.svg)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-8.0-blue.svg)](https://pytest.org/)
[![Requests](https://img.shields.io/badge/Requests-2.31-orange.svg)](https://requests.readthedocs.io/)
![Tests](https://img.shields.io/badge/Tests-24%20Passing-brightgreen.svg)
![UI Tests](https://img.shields.io/badge/UI-19%20Passing-green.svg)
![API Tests](https://img.shields.io/badge/API-5%20Passing-blue.svg)

**🚀 24/24 Tests Passing | 100% Success Rate**

---

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Test Results](#test-results)
- [Quick Start](#quick-start)
- [Banking Features Tested](#banking-features-tested)
- [Project Structure](#project-structure)
- [Technology Stack](#technology-stack)
- [Skills Demonstrated](#skills-demonstrated)
- [Configuration](#configuration)
- [CI/CD Integration](#cicd-integration)
- [Test Execution Time](#test-execution-time)
- [Author](#author)
- [License](#license)

---

## 📖 Project Overview
A **production-ready** test automation framework for **Fintech/Banking applications**.  
It covers both **UI automation (Selenium)** and **API testing (Python requests)** on the ParaBank demo banking platform.

### Features Tested
- Account Management (balances, IDs, overview)
- Fund Transfers
- Bill Payment
- Transaction History
- Loan Requests
- Profile Management

---

## 📊 Test Results

| Metric | Value |
|--------|-------|
| **Total Tests** | 24 |
| **Passed** | 24 ✅ |
| **Failed** | 0 ❌ |
| **Pass Rate** | 100% |
| **Execution Time** | 603s (~10 min) |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Chrome browser
- Git

### Installation
```bash
git clone https://github.com/bhishma11/finpay-automation
cd finpay-automation/selenium-tests
pip install -r requirements.txt
Got it — your README is overloaded with repeated sections and some broken badge links. Let me clean it up into a **professional, concise, and visually clear version** that renders properly on GitHub. I’ll fix the badge links, remove duplication, and organize the sections so it flows smoothly.


### Run Tests
```bash
pytest tests/ -v                         # Run all tests
pytest tests/test_api.py -v              # Run only API tests
pytest tests/test_parabank_features.py -v # Run only UI tests
```

---

## 🏦 Banking Features Tested

| Feature            | UI Test | API Test | Status |
|--------------------|---------|----------|--------|
| Account Overview   | ✅      | ✅       | ✅ |
| Account Balance    | ✅      | ✅       | ✅ |
| Account ID         | ✅      | ✅       | ✅ |
| Transfer Funds     | ✅      | ✅       | ✅ |
| Bill Payment       | ✅      | ❌       | ✅ |
| Find Transactions  | ✅      | ❌       | ✅ |
| Open New Account   | ✅      | ❌       | ✅ |
| Update Profile     | ✅      | ❌       | ✅ |
| Request Loan       | ✅      | ❌       | ✅ |
| Login Validation   | ✅      | ❌       | ✅ |

---

## 📊 Test Results

### Executive Summary

| Metric | Value |
|--------|-------|
| **Total Tests** | 24 |
| **Passed** | 24 ✅ |
| **Failed** | 0 ❌ |
| **Pass Rate** | 100% |
| **Total Time** | 603 seconds (10 minutes) |

---

### Test Execution Output

```
collected 24 items

⚡ API TESTS (5 tests)
test_api.py::test_api_get_account_by_id ............. PASSED ✅
test_api.py::test_api_get_customer_accounts ......... PASSED ✅
test_api.py::test_api_transfer_invalid_amount ....... PASSED ✅
test_api.py::test_api_check_service_health .......... PASSED ✅
test_api.py::test_api_response_time ................ PASSED ✅

💰 BALANCE TESTS (2 tests)
test_balance.py::test_balance_displays .............. PASSED ✅
test_balance.py::test_account_id_exists ............. PASSED ✅

🔗 NAVIGATION TESTS (2 tests)
test_failing.py::test_find_transactions_link ........ PASSED ✅
test_failing.py::test_bill_pay_link ................. PASSED ✅

🔐 LOGIN TESTS (3 tests)
test_login.py::test_valid_login ..................... PASSED ✅
test_login.py::test_invalid_password ................ PASSED ✅
test_login.py::test_empty_credentials ............... PASSED ✅

🏦 BANKING FEATURES TESTS (12 tests)
test_parabank_features.py::test_account_overview_table_exists  PASSED ✅
test_parabank_features.py::test_account_balance_displayed     PASSED ✅
test_parabank_features.py::test_account_id_displayed          PASSED ✅
test_parabank_features.py::test_navigate_to_transfer_funds    PASSED ✅
test_parabank_features.py::test_transfer_page_has_from_accounts PASSED ✅
test_parabank_features.py::test_transfer_page_has_to_accounts   PASSED ✅
test_parabank_features.py::test_amount_field_exists          PASSED ✅
test_parabank_features.py::test_open_new_account_page        PASSED ✅
test_parabank_features.py::test_bill_pay_page                PASSED ✅
test_parabank_features.py::test_find_transactions_page       PASSED ✅
test_parabank_features.py::test_update_profile_page          PASSED ✅
test_parabank_features.py::test_request_loan_page            PASSED ✅

============================================ 24 passed in 603.31s ============================================
```

---

### API Test Details

| Test Case | Endpoint | Expected | Actual | Status |
|-----------|----------|----------|--------|--------|
| Get Account by ID | `GET /accounts/14121` | 200 OK | 200 OK | ✅ |
| Get Customer Accounts | `GET /customers/14121/accounts` | 200/400 | 400 | ✅ |
| Transfer Invalid Amount | `POST /transfer` (amount=-50) | 400 Error | 400 Error | ✅ |
| Service Health Check | `GET /login/test` | Any response | 400 | ✅ |
| Response Time | `GET /accounts/14121` | < 5s | 202ms | ✅ |

---

### Test Breakdown by Category

| Category | Test File | Tests | Status |
|----------|-----------|-------|--------|
| API Tests | `test_api.py` | 5 | ✅ PASSED |
| Balance Tests | `test_balance.py` | 2 | ✅ PASSED |
| Navigation Tests | `test_failing.py` | 2 | ✅ PASSED |
| Login Tests | `test_login.py` | 3 | ✅ PASSED |
| Banking Features | `test_parabank_features.py` | 12 | ✅ PASSED |
| **TOTAL** | | **24** | **✅ 100% PASS** |
```

## 📁 Project Structure
```
finpay-automation/
│
├── selenium-tests/
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── dashboard_page.py
│   │   └── transfer_page.py
│   ├── tests/
│   │   ├── test_api.py               (5 tests)
│   │   ├── test_login.py             (3 tests)
│   │   ├── test_balance.py           (2 tests)
│   │   ├── test_failing.py           (2 tests)
│   │   └── test_parabank_features.py (12 tests)
│   ├── conftest.py
│   ├── requirements.txt
│   └── screenshots/
└── README.md
```

---

## 🛠️ Technology Stack

| Tool              | Version | Purpose             |
|-------------------|---------|---------------------|
| Python            | 3.11+   | Core language       |
| Selenium          | 4.16    | Browser automation  |
| Pytest            | 8.0     | Test framework      |
| Requests          | 2.31    | API testing         |
| WebDriver Manager | 4.0     | Driver management   |

---

## 💡 Skills Demonstrated
- **Selenium WebDriver**: 19 UI tests with Page Object Model  
- **API Testing**: 5 API tests using Python requests  
- **Fintech Domain**: Banking operations (transfers, loans, bill pay)  
- **Framework Design**: Fixtures, configuration, screenshots on failure  
- **Wait Strategies**: Explicit waits (no `time.sleep()`)  
- **CI/CD Ready**: GitHub Actions integration  

---

## 🔧 Configuration

Example command-line arguments:
```bash
pytest tests/ \
  --url="https://your-bank.com/login" \
  --username-field="#username" \
  --password-field="#password" \
  --login-button="button[type='submit']" \
  --headless
```

---

## 🔄 CI/CD Integration

```yaml
name: Run Tests

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 8 * * *'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r selenium-tests/requirements.txt
      - run: pytest selenium-tests/tests/ -v --headless
```

---

## 📈 Test Execution Time

| Category   | Time   |
|------------|--------|
| API Tests  | ~2s    |
| UI Tests   | ~601s  |
| **Total**  | ~603s  |

---

## 👨‍💻 Author
**Bhishma Khettri**  
GitHub: [@bhishma11](https://github.com/bhishma11)

---

## 📄 License
MIT License  

⭐ If you find this project useful, please give it a star!

---

