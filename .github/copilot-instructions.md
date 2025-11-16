
# Copilot Instructions for automation-framework-playwright-python

## Project Overview
This repository is a hybrid Playwright automation framework for both Python and TypeScript/JavaScript. It is designed for end-to-end, integration, and UI testing of web applications, with a focus on modularity, reusability, and cross-language support.

## Architecture & Key Components
- **case_search/**: Main Python framework for enterprise web app testing.
  - `models/`: Page Object Model (POM) classes (e.g., `login_page.py`, `registration_page.py`).
  - `protocol/`: Encapsulated user flows (e.g., `register_user.py`, `login_user.py`, `search_case.py`).
  - `context/`: Test context and browser/session management (`test_context.py`).
  - `configs/`: Tenant/environment configs (e.g., `txstage.json`).
  - `tests/`: Pytest-based test suites for registration, search, and end-to-end flows.
  - `utils/`: Utilities (e.g., screenshot, logging).
- **saucedemo/**: Example Playwright suite for SauceDemo app, with Python POMs and tests. Demonstrates best practices and cross-app patterns.
- **playwright.config.ts**: TypeScript Playwright config for JS/TS tests (not used by Python runner).
- **codegen_registration.py**: Example Playwright codegen output for Python.

## Developer Workflows
- **Environment Setup:**
  - `pip install -r requirements.txt`
  - `python -m playwright install`
- **Running Tests:**
  - Python: `python -m pytest case_search/tests/test_registration.py --headed`
  - Tag-based: `python -m pytest -m login`
  - End-to-end: `python runner.py --tenant txstage --browser chromium --marker endtoend --user_type new`
  - TypeScript: `npx playwright test` (for JS/TS tests)
- **Codegen:**
  - `npx playwright codegen --target python <url> > codegen_registration.py`
- **Reports:**
  - Allure and pytest-html supported for reporting.
- **Logs:**
  - Written to `logs/` directories per suite (e.g., `registration_log.txt`, `error_log.txt`).

## Project Conventions & Patterns
- **Page Object Model:** All UI interactions are encapsulated in `models/` classes. Tests and protocols should not directly use Playwright APIs.
- **Protocols:** User flows are implemented in `protocol/` and should be reused in tests (e.g., registration, login, onboarding, search).
- **Test Context:** Shared context and fixtures are in `context/test_context.py` and `conftest.py`. Context manages browser, page, config, and user state.
- **Config Management:** Use `case_search/configs/` for environment/tenant settings. Never hardcode URLs or credentials.
- **Naming:**
  - Test files: `test_*.py`
  - Page objects: `*_page.py`
  - Protocols: describe user flows (e.g., `register_user.py`)
- **Cross-app Patterns:**
  - `saucedemo/` mirrors the main framework structure for demo purposes.
  - Accessibility testing via `axe-playwright-python` in `saucedemo/utils/accessibility_utils.py`.

## Integration Points
- **External Services:**
  - Mailinator flows for email-based activation (`mailinator_page.py`, `mailinator_protocol.py`).
- **CI/CD:**
  - Always install dependencies and Playwright browsers before running tests.
  - Use the provided runner (`runner.py`) for parameterized test execution.

## Examples & Recipes
- Add a new page: create a POM in `models/` and a protocol in `protocol/`.
- Add a new test: place it in `case_search/tests/` and use context/protocols.
- For SauceDemo: see `saucedemo/tests/` for login, cart, and accessibility test patterns.

---
For more details, see `read_me.txt` and `read_me_python.txt` in the project root.
