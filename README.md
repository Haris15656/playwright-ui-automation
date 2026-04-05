markdown# Playwright UI Automation

Automated UI test suite built with Playwright and pytest using the Page Object Model (POM) 
architecture. Tests real websites by automating browser interactions including form submissions,
navigation flows, and UI validation.

## Tech Stack
- Python 3.12
- Playwright
- Pytest
- pytest-html
- Page Object Model (POM)

## Project Structure
playwright-ui-automation/
├── pages/
│   ├── login_page.py
│   └── todo_page.py
├── tests/
│   ├── test_login.py
│   └── test_todo.py
├── reports/
│   └── report.html
└── conftest.py

## Test Cases
| # | Test | Description | Status |
|---|------|-------------|--------|
| 01 | test_valid_login | Valid credentials login successfully | ✅ |
| 02 | test_invalid_password | Wrong password shows error message | ✅ |
| 03 | test_invalid_username | Wrong username shows error message | ✅ |
| 04 | test_empty_credentials | Empty fields show error message | ✅ |
| 05 | test_add_single_todo | Add a single todo item | ✅ |
| 06 | test_add_multiple_todos | Add multiple todo items | ✅ |
| 07 | test_complete_todo | Mark a todo as completed | ✅ |
| 08 | test_clear_completed | Clear completed todos | ✅ |

## Architecture
This project follows the **Page Object Model (POM)** pattern:
- Each website has its own page class describing its elements and actions
- Tests only call methods — they never interact with HTML directly
- Makes tests readable, maintainable, and scalable

## How to Run
```bash
pip install playwright pytest pytest-playwright pytest-html
playwright install chromium

# Run headless (background)
pytest tests/ --browser chromium -v --html=reports/report.html

# Run headed (visible browser)
pytest tests/ --browser chromium -v --html=reports/report.html --headed
``