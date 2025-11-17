# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a hybrid Playwright automation framework supporting both Python and TypeScript, designed for end-to-end web application testing with modularity and reusability. The framework uses Page Object Model (POM) architecture with protocol-based user flows.

## Architecture

### case_search/ - Main Python Framework
The primary test suite for enterprise web app testing with the following structure:

- **models/**: Page Object Model classes encapsulating UI interactions (e.g., `login_page.py`, `registration_page.py`, `contact_info_page.py`)
- **protocol/**: Reusable user flows that compose page objects into higher-level actions:
  - `register_user.py` - User registration with email generation
  - `login_user.py` - Authentication flow
  - `activate_account.py` - Email-based activation via Mailinator
  - `onboard_user.py` - Post-registration onboarding (terms, contact info)
  - `search_case.py` - Case search flows
- **context/**: `test_context.py` manages browser lifecycle, tenant configs, and session state
  - Loads tenant-specific configs from `configs/`
  - Handles session persistence via `state/session_state.json` and `state/last_user.txt`
  - Supports resuming existing sessions to avoid re-registration
- **configs/**: JSON files per tenant/environment (e.g., `txstage.json`, `castage.json`)
  - Contains `base_url`, `features` flags, `default_password`
- **tests/**: Pytest-based test suites
  - `test_endtoend_register_search.py` - Full registration-to-search flow with session resume
  - Organized by feature area
- **utils/**: Helper functions (screenshots, logging)

### saucedemo/ - Demo Framework
Example implementation demonstrating framework patterns on SauceDemo app:
- Mirrors main framework structure (pages/, tests/, utils/)
- Includes accessibility testing example with `axe-playwright-python`

### Key Framework Patterns

**TestContext Pattern**: Central context object manages:
- Browser and page instances
- Tenant configuration loading
- Feature flags
- Session state persistence
- Generated user credentials

**Protocol Pattern**: User flows are composable and reusable:
```python
register_user(context)      # Creates new user
activate_account(context)   # Activates via email
login_user(context)         # Authenticates
onboard_user(context)       # Handles conditional onboarding
search_case(context)        # Performs search
```

**Session Resume**: Framework can resume from saved sessions:
- Check for `state/session_state.json` and `state/last_user.txt`
- Skip registration/activation if session exists
- To force clean run: delete state files

## Common Commands

### Setup
```bash
pip install -r requirements.txt
python -m playwright install
```

### Running Tests

**Direct pytest execution:**
```bash
# Run specific test file
python -m pytest case_search/tests/test_registration.py --headed

# Run by marker
python -m pytest -m login
python -m pytest -m endtoend
python -m pytest -m "checkout and endtoend"

# Run all tests
pytest
```

**Using runner.py (recommended for parameterized execution):**
```bash
# Basic run
python runner.py --tenant txstage --browser chromium --marker endtoend --user_type new

# Run specific test
python runner.py --tenant txstage --browser chromium --test case_search/tests/test_registration.py

# Run as existing user (resume session)
python runner.py --tenant txstage --browser chromium --marker endtoend --user_type existing
```

**Runner arguments:**
- `--tenant`: Required. Config name from `case_search/configs/` (e.g., txstage, castage)
- `--browser`: chromium (default), firefox, or webkit
- `--marker`: Pytest marker to filter tests
- `--test`: Specific test file or function
- `--user_type`: new (default) or existing (for session resume)
- `--path`: Test path (default: case_search/tests)

### Playwright Codegen
```bash
npx playwright codegen --target python <url> > codegen_registration.py
```

## Development Conventions

### Never Hardcode
- URLs and credentials belong in `case_search/configs/` JSON files
- Use `context.base_url`, `context.default_password`, `context.features`

### Page Object Model Rules
- All Playwright API calls must be in `models/` classes
- Tests and protocols should never directly use `page.locator()` or similar
- Page objects expose locators and action methods

### Protocol Composition
- Protocols orchestrate page objects into user flows
- Tests should primarily call protocols, not page objects directly
- Keep protocols focused on a single flow

### Test Context Management
- Always use `TestContext` for browser/page management
- Context loads tenant config and manages state
- Use `context.launch_page()` to initialize with session resume support

### Naming Conventions
- Test files: `test_*.py`
- Page objects: `*_page.py`
- Protocols: descriptive verb phrases (e.g., `register_user.py`)

### Pytest Markers
Available markers (defined in pytest.ini):
- `login`, `registration`, `inventory`, `checkout`, `purchase`, `cart`
- `endtoend` - Full user flows
- `smoke` - Quick validation
- `regression` - Full suite
- `flag_aware` - Tests depending on feature flags

### Logging and Debugging
- Logs written to `case_search/logs/` (e.g., `registration_log.txt`)
- Screenshots captured on test failure to `screenshots/` directory
- Use `context.page.screenshot()` for manual captures

### Session Management
- Session state persisted to `state/session_state.json`
- Last user email stored in `state/last_user.txt`
- Delete state files to force fresh registration
- Use `--user_type existing` with runner.py to resume sessions

### External Integrations
- Mailinator: Used for email activation flows
  - `mailinator_page.py` and `mailinator_protocol.py` handle email retrieval
- Always verify email generation format: `prefix_randomid@mailinator.com`

## Single Test Execution

To run a single test function:
```bash
python runner.py --tenant txstage --browser chromium --test case_search/tests/test_registration.py::test_user_registration
```

## CI/CD Notes

- Install dependencies and Playwright browsers before test execution
- Use `runner.py` for parameterized runs across tenants/browsers
- Set environment variables `tenant` and `browser` (handled by runner.py)
- Consider using `--user_type new` for clean CI runs
