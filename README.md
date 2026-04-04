# Playwright UI Automation

Automated UI test suite built with Playwright and pytest using the Page Object Model (POM) architecture.

## Tech Stack
- Python 3.12
- Playwright
- Pytest
- pytest-html

## Project Structure
playwright-ui-automation/
├── pages/
│   └── login_page.py
├── tests/
│   └── test_login.py
├── reports/
│   └── report.html
└── conftest.py

## Test Cases
| Test | Description | Status |
|------|-------------|--------|
| test_valid_login | Valid credentials should login successfully | ✅ |
| test_invalid_password | Wrong password should show error | ✅ |
| test_invalid_username | Wrong username should show error | ✅ |
| test_empty_credentials | Empty fields should show error | ✅ |

## How to Run
```bash
pip install playwright pytest pytest-playwright pytest-html
playwright install chromium
pytest tests/ --browser chromium -v --html=reports/report.html