import pytest
from pages import CartPage
from pages import CheckOutStepOnePage
from playwright.sync_api import Page
from tests.test_add_to_cart import test_add_to_cart
from utils.common_utils import get_current_timestamp

def test_checkout_error_verification(page: Page):
    test_add_to_cart(page)
    cart_page = CartPage.CartPage(page)
    cart_page.click_checkout_button()

    checkout_page = CheckOutStepOnePage.CheckOutStepOnePage(page)
    checkout_page.fill_checkout_information("Jon")
    checkout_page.click_continue_button()
    assert checkout_page.error_message() == "Error: Last Name is required"

    with open("logging_tests/error_log.txt", "a") as log_file:
        log_file.write(f"Checkout error verification completed successfully. \nError message displayed: {checkout_page.error_message()} \t {get_current_timestamp()}\n")