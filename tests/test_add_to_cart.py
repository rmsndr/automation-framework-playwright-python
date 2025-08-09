import pytest
from pages import InventoryPage,CartPage
from playwright.sync_api import Page
from tests.test_login import test_valid_login
from utils.common_utils import get_current_timestamp

def test_add_to_cart(page: Page):
    test_valid_login(page)  # Ensure user is logged in before adding items to cart
    inventory_page = InventoryPage.InventoryPage(page)
    cart_page = CartPage.CartPage(page)
    inventory_page.page.goto("https://www.saucedemo.com/inventory.html")
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    navigate_to_cart(page)
    #save print to a file
    with open("logging_tests/cart_addition_log.txt", "a") as log_file:
        log_file.write(f"Items added to cart successfully. Current cart count: {cart_page.get_cart_count()} items.\t {get_current_timestamp()}\n")

def navigate_to_cart(page: Page):
    inventory_page = InventoryPage.InventoryPage(page)
    inventory_page.navigate_to_cart()