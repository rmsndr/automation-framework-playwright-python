
from playwright.sync_api import Page
class CartPage:
    def __init__(self, page: Page):
        self.page = page
    def click_checkout_button(self):
        checkout_button = self.page.locator("#checkout")
        checkout_button.click()
        self.page.wait_for_url("https://www.saucedemo.com/checkout-step-one.html")

    def get_backpack_price_on_cart(self):
        # Assuming the backpack price is obtained from executing a JavaScript query
        backpack_price = self.page.evaluate("document.querySelector('#item_4_title_link').nextElementSibling.nextElementSibling.querySelector('.inventory_item_price').textContent")
        return backpack_price if backpack_price else Exception("Backpack price not found")
    #$('#item_4_title_link').nextElementSibling.nextElementSibling.querySelector(".inventory_item_price").textContent

    def get_cart_count(self):
        # Assuming the cart count is obtained from executing a JavaScript query
        cart_count = self.page.evaluate("document.querySelector('.shopping_cart_badge').textContent")
        return int(cart_count) if cart_count else 0