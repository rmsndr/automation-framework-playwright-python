import pytest
from pages import LoginPage, InventoryPage, CartPage, CheckOutStepOnePage, CheckOutStepTwoPage, CheckoutCompletePage
from playwright.sync_api import Page
from tests.test_login import test_valid_login
from utils.common_utils import get_current_timestamp

def verify_backpack_price(inventory_page_backpack_price, cart_page_backpack_price, checkout_step_two_page_backpack_price):
    """Verify that backpack price is consistent across all pages."""
    assert inventory_page_backpack_price == cart_page_backpack_price, \
        f"Backpack price mismatch between inventory ({inventory_page_backpack_price}) and cart ({cart_page_backpack_price}) pages"
    assert inventory_page_backpack_price == checkout_step_two_page_backpack_price, \
        f"Backpack price mismatch between inventory ({inventory_page_backpack_price}) and checkout step two ({checkout_step_two_page_backpack_price}) pages"
    assert cart_page_backpack_price == checkout_step_two_page_backpack_price, \
        f"Backpack price mismatch between cart ({cart_page_backpack_price}) and checkout step two ({checkout_step_two_page_backpack_price}) pages"

@pytest.mark.endtoend
@pytest.mark.purchase
@pytest.mark.checkout
@pytest.mark.regression
def test_purchase_backpack_verify_price_across_pages(page_with_video: Page):
    """
    End-to-end test that purchases a backpack and verifies the price remains consistent
    across inventory, cart, and checkout pages.
    """
    # Initialize page objects
    login_page = LoginPage.LoginPage(page_with_video)
    inventory_page = InventoryPage.InventoryPage(page_with_video)
    cart_page = CartPage.CartPage(page_with_video)
    checkout_step_one_page = CheckOutStepOnePage.CheckOutStepOnePage(page_with_video)
    checkout_step_two_page = CheckOutStepTwoPage.CheckOutStepTwoPage(page_with_video)
    checkout_complete_page = CheckoutCompletePage.CheckoutCompletePage(page_with_video)
    
    # Step 1: Login and navigate to inventory page
    test_valid_login(page_with_video)  # Ensure user is logged in
    page_with_video.goto("https://www.saucedemo.com/inventory.html")
    
    # Step 2: Add backpack to cart and get price from inventory page
    inventory_page.add_backpack_to_cart()
    inventory_page_backpack_price = inventory_page.get_backpack_price()
    assert inventory_page_backpack_price, "Failed to retrieve backpack price from inventory page"
    page_with_video.screenshot(path="saucedemo/screenshots/inventory_page_backpack_price.png", full_page=True)
    
    # Step 3: Navigate to cart page and verify price
    inventory_page.navigate_to_cart()
    cart_page_backpack_price = cart_page.get_backpack_price_on_cart()
    assert cart_page_backpack_price, "Failed to retrieve backpack price from cart page"
    page_with_video.screenshot(path="saucedemo/screenshots/cart_page_backpack_price.png", full_page=True)
    
    # Step 4: Proceed to checkout step one
    cart_page.click_checkout_button()
    checkout_step_one_page.fill_checkout_information("John", "Doe", "12345")
    checkout_step_one_page.click_continue_button()
    
    # Step 5: Verify price on checkout step two page
    checkout_step_two_page_backpack_price = checkout_step_two_page.get_backpack_price_on_checkout()
    assert checkout_step_two_page_backpack_price, "Failed to retrieve backpack price from checkout step two page"
    page_with_video.screenshot(path="saucedemo/screenshots/checkout_step_two_page.png", full_page=True)
    
    # Step 6: Complete the purchase
    checkout_step_two_page.click_finish_button()
    confirmation_message = checkout_complete_page.verify_order_confirmation_message()
    assert confirmation_message, "Order confirmation message not found"
    page_with_video.screenshot(path="saucedemo/screenshots/order_confirmation.png", full_page=True)
    
    # Video will be automatically saved when the context closes (in the fixture teardown)
    # The video will be saved in saucedemo/videos/ directory with an auto-generated name
    
    # Step 7: Verify price consistency across all pages
    verify_backpack_price(inventory_page_backpack_price, cart_page_backpack_price, checkout_step_two_page_backpack_price)
    
    # Step 8: Log the results
    with open("saucedemo/logs/backpack_price_verification_log.txt", "a") as log_file:
        log_file.write(f"Backpack price verified across inventory, cart, and checkout step two pages successfully. \t {get_current_timestamp()}\n")

    with open("saucedemo/logs/backpack_prices.txt", "a") as price_log:
        price_log.write(f"Inventory Page Backpack Price: {inventory_page_backpack_price} \t {get_current_timestamp()}\n")
        price_log.write(f"Cart Page Backpack Price: {cart_page_backpack_price} \t {get_current_timestamp()}\n")
        price_log.write(f"Checkout Step Two Page Backpack Price: {checkout_step_two_page_backpack_price} \t {get_current_timestamp()}\n")
