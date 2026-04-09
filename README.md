# Playwright UI Automation

Automated browser test suite built with Playwright and pytest using the Page Object Model (POM) architecture. Tests my own live portfolio website and a Todo app by automating real Chrome browser interactions.

## Tech Stack
- Python 3.12
- Playwright
- Pytest
- pytest-html
- Page Object Model (POM)

## Project Structure
playwright-ui-automation/
├── pages/
│   ├── portfolio_page.py
│   └── todo_page.py
├── tests/
│   ├── test_portfolio.py
│   └── test_todo.py
├── reports/
│   └── report.html
└── conftest.py

## Test Cases (11)

### Portfolio Tests — haris-noonari.vercel.app
| # | Test | Description | Status |
|---|------|-------------|--------|
| 01 | test_portfolio_loads | Portfolio loads and hero name is visible | ✅ |
| 02 | test_about_section_visible | About section exists in DOM | ✅ |
| 03 | test_projects_section_visible | Projects section exists in DOM | ✅ |
| 04 | test_experience_section_visible | Experience section exists in DOM | ✅ |
| 05 | test_contact_section_visible | Contact section exists in DOM | ✅ |
| 06 | test_language_switch_to_german | DE/EN language switcher works | ✅ |
| 07 | test_page_title | Browser tab title is not empty | ✅ |

### Todo App Tests — demo.playwright.dev/todomvc
| # | Test | Description | Status |
|---|------|-------------|--------|
| 08 | test_add_single_todo | Single todo item added correctly | ✅ |
| 09 | test_add_multiple_todos | Multiple todos added and counted | ✅ |
| 10 | test_complete_todo | Todo marked as completed | ✅ |
| 11 | test_clear_completed | Completed todos cleared correctly | ✅ |

## Architecture
Uses **Page Object Model (POM)** — each website has its own page class. Tests call methods, never interact with HTML directly. Makes tests readable, maintainable, and scalable.

## How to Run
```bash
pip install playwright pytest pytest-playwright pytest-html
playwright install chromium
pytest tests/ --browser chromium -v --html=reports/report.html
pytest tests/ --browser chromium -v --headed  # visible browser
```