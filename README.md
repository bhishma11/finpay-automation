\# 🏦 FinPay Automation Framework



\[!\[Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)

\[!\[Selenium](https://img.shields.io/badge/selenium-4.16-green.svg)](https://www.selenium.dev/)

\[!\[Pytest](https://img.shields.io/badge/pytest-8.0-blue.svg)](https://pytest.org/)

\[!\[Tests](https://img.shields.io/badge/tests-24%20passing-brightgreen.svg)]()



A \*\*production-ready\*\* test automation framework for Fintech/Banking applications. Demonstrates both \*\*UI automation (Selenium)\*\* and \*\*API testing (Python requests)\*\* on a real banking platform.



\---



\## 📊 Test Results Summary



| Category | Test File | Tests | Status |

|----------|-----------|-------|--------|

| \*\*API Tests\*\* | `test\_api.py` | 5 | ✅ All Passing |

| \*\*Login Tests\*\* | `test\_login.py` | 3 | ✅ All Passing |

| \*\*Balance Tests\*\* | `test\_balance.py` | 2 | ✅ All Passing |

| \*\*Banking Features\*\* | `test\_parabank\_features.py` | 14 | ✅ All Passing |

| \*\*TOTAL\*\* | | \*\*24\*\* | \*\*✅ 100% PASS\*\* |



\### Test Execution Output



```bash

$ pytest tests/ -v

============================================ test session starts ============================================

collected 24 items



test\_api.py .................... 5 passed

test\_balance.py ................ 2 passed

test\_login.py .................. 3 passed

test\_parabank\_features.py ...... 14 passed



============================================ 24 passed in 596.24s ============================================

