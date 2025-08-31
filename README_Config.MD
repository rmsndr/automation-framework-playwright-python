# 🧪 Python Playwright Test Automation with GitHub Actions CI

Welcome! This repo contains a modular, marker-driven Python Playwright test suite with GitHub Actions CI integration. It’s designed for scalability, maintainability, and fast feedback..

---

## 📁 Project Structure

```
your-project/
├── tests/
│   ├── login/
│   │   └── test_login.py
│   ├── inventory/
│   │   └── test_add_to_cart.py
│   ├── checkout/
│   │   └── test_checkout_flow.py
├── utils/
│   └── common_utils.py
├── pytest.ini
├── requirements.txt
└── .github/
    └── workflows/
        └── python-playwright.yml
```

---

## 🧾 Setup Instructions

### 1. Install Dependencies

```bash
pip install pytest playwright pytest-playwright pytest-base-url axe-playwright-python requests
playwright install
```

Generate and clean up `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Recommended contents:

```txt
pytest==8.4.1
playwright==1.54.0
pytest-playwright==0.7.0
pytest-base-url==2.1.0
axe-playwright-python==0.1.5
requests==2.32.4
```

---

### 2. Add Pytest Markers

Use markers to group tests by feature:

```python
import pytest

@pytest.mark.login
def test_valid_login(page):
    ...

@pytest.mark.checkout
@pytest.mark.endtoend
def test_purchase_flow(page):
    ...
```

---

### 3. Configure `pytest.ini`

```ini
[pytest]
addopts = -v
markers =
    login: tests related to login functionality
    inventory: tests for inventory and cart actions
    checkout: tests for checkout flow and validations
    endtoend: full flow tests across multiple pages
```

---

### 4. Update `.gitignore`

```gitignore
__pycache__/
axe_results/
*.txt
!requirements.txt
```

---

### 5. Set Up GitHub Actions CI

Create `.github/workflows/python-playwright.yml`:

```yaml
name: Python Playwright Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        playwright install

    - name: Run Pytest
      run: |
        pytest --maxfail=1 --disable-warnings
```

---

## 🧪 Running Tests

Run by marker:

```bash
pytest -m login
pytest -m "checkout and endtoend"
```

Run all tests:

```bash
pytest
```

---

## ✅ Optional Enhancements

- 📊 Add `pytest-html` for visual reports
- ⚡ Use `pytest-xdist` for parallel execution
- ♿ Integrate accessibility checks with axe-core
- 📁 Upload artifacts in CI for trace/debugging

---

## 🧠 Tips

- Keep `requirements.txt` lean for fast CI runs
- Use markers to isolate smoke, regression, or feature tests
- Document marker usage in `pytest.ini` for team clarity

---

## 🙌 Contributing

Feel free to fork, clone, and contribute! PRs welcome for new test modules, CI improvements, or reporting integrations.

---

Happy testing! 🎯
