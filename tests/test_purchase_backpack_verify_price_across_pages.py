from pages import LoginPage,InventoryPage, CartPage, CheckOutStepOnePage, CheckOutStepTwoPage, CheckoutCompletePage
from playwright.sync_api import Page
from tests.test_add_to_cart import test_add_to_cart
from utils.common_utils import get_current_timestamp

def verify_backpack_price(inventory_page_backpack_price, cart_page_backpack_price, checkout_step_two_page_backpack_price):
    assert inventory_page_backpack_price == cart_page_backpack_price, "Backpack price mismatch between inventory and cart pages"
    assert inventory_page_backpack_price == checkout_step_two_page_backpack_price, "Backpack price mismatch between inventory and checkout step two pages"
    assert cart_page_backpack_price == checkout_step_two_page_backpack_price, "Backpack price mismatch between cart and checkout step two pages"
    
def test_purchase_backpack_verify_price_across_pages(page: Page):
    # initialize pages
    login_page = LoginPage.LoginPage(page)
    inventory_page = InventoryPage.InventoryPage(page)
    cart_page = CartPage.CartPage(page)
    checkout_step_one_page = CheckOutStepOnePage.CheckOutStepOnePage(page)
    checkout_step_two_page = CheckOutStepTwoPage.CheckOutStepTwoPage(page)
    checkout_complete_page = CheckoutCompletePage.CheckoutCompletePage(page)
    
    test_add_to_cart(page)  # Ensure backpack is added to cart
    inventory_page_backpack_price = inventory_page.get_backpack_price()  # Get backpack price from inventory page
    inventory_page.navigate_to_cart()  # Navigate to cart page
    cart_page_backpack_price = cart_page.get_backpack_price_on_cart()  # Get backpack price from cart page
    cart_page.click_checkout_button()  # Click checkout button to proceed to checkout step one
    checkout_step_one_page.fill_checkout_information("John", "Doe", "12345")  # Fill checkout information
    checkout_step_one_page.click_continue_button()  # Click continue to proceed to checkout step two
    checkout_step_two_page_backpack_price = checkout_step_two_page.get_backpack_price_on_checkout()  # Get backpack price from checkout step two page
    checkout_step_two_page.click_finish_button()  # Click finish to complete the purchase

    checkout_complete_page.verify_order_confirmation_message()  # Verify purchase success message

    verify_backpack_price(inventory_page_backpack_price, cart_page_backpack_price, checkout_step_two_page_backpack_price)  
    # add time stamp at the end of the log
    # Verify backpack price across pages
    # "a" means append mode, so it won't overwrite existing logs
    with open("logging_tests/backpack_price_verification_log.txt", "a") as log_file:
        log_file.write(f"Backpack price verified across inventory, cart, and checkout step two pages successfully. \t {get_current_timestamp()}\n")

    # Optionally, you can print the prices for debugging

    with open("logging_tests/backpack_prices.txt", "a") as price_log:
        price_log.write(f"Inventory Page Backpack Price: {inventory_page_backpack_price} \t {get_current_timestamp()}\n")
        price_log.write(f"Cart Page Backpack Price: {cart_page_backpack_price} \t {get_current_timestamp()}\n")
        price_log.write(f"Checkout Step Two Page Backpack Price: {checkout_step_two_page_backpack_price} \t {get_current_timestamp()}\n")
