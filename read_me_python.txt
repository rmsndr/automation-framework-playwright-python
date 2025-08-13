python --version
pip --version

pip install playwright

python -m playwright install

pip install pytest

pip install pytest-playwright

pip install allure-pytest pytest-html

Every Time You Start Fresh (like in CI/CD or a new venv)
Here’s your minimum bootstrapping script:

pip install playwright pytest
python -m playwright install

To run tests locally to test: 
python -m pytest .\tests\test_add_to_cart.py --headed 

To run tagged tests:
python -m pytest -m login