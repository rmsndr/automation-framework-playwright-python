import uuid
import json
from playwright.sync_api import Page
import pytest
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from tests import test_login
from utils.accessibility_utils import accessibility_utils

@pytest.mark.inventory
def test_inventory_accessibility(page: Page):
    inventory = InventoryPage(page)
    # do not assert, save results to a file
    test_login.test_valid_login(page)
    inventory.page.goto("https://www.saucedemo.com/inventory.html")
    result = accessibility_utils.run_axe_scan(inventory.page)
    # use the name of the test function in the file name
    # goto the results folder and save the results there
    result.save_to_file(f"axe_results/{test_inventory_accessibility.__name__}_accessibility_results_{uuid.uuid4()}.json")
    print("Accessibility scan completed and results saved.")
    # Optionally, you can print the violations count
    print(f"Violations found: {result.violations_count}")

@pytest.mark.login
def test_login_accessibility(page: Page):
    login_page = LoginPage(page)
    login_page.page.goto("https://www.saucedemo.com")
    result = accessibility_utils.run_axe_scan(login_page.page)
    print(type(result))
    print(dir(result))

    # AxeResults is a custom class (<class 'axe_playwright_python.base.AxeResults'>)
    # with attributes such as 
    #['_AxeResults__violation_report', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'generate_report', 'generate_snapshot', 'response', 'save_to_file', 'violations_count']
    # do not assert, save results to a file
    # use the name of the test function in the file name
    result.save_to_file(f"axe_results/{test_login_accessibility.__name__}_accessibility_results_{uuid.uuid4()}.json")
    print("Accessibility scan completed and results saved.")
    # Optionally, you can print the violations count
    print(f"Violations found: {result.violations_count}")
