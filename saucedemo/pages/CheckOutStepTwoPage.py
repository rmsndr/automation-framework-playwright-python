from playwright.sync_api import Page
class CheckOutStepTwoPage:
    def __init__(self, page: Page):
        self.page = page

    def click_finish_button(self):
        finish_button = self.page.locator("#finish")
        finish_button.click()
        # Optionally wait for the URL to change or for a confirmation message
        # self.page.wait_for_url("https://www.saucedemo.com/checkout-complete.html")
   
    def get_backpack_price_on_checkout(self):
        """Get the backpack price from the checkout step two page."""
        backpack_price = self.page.evaluate(
            "document.querySelector('#item_4_title_link').nextElementSibling.nextElementSibling.querySelector('.inventory_item_price').textContent"
        )
        if not backpack_price:
            raise ValueError("Backpack price not found on checkout step two page")
        return backpack_price
    #$('#item_4_title_link').nextElementSibling.nextElementSibling.querySelector(".inventory_item_price").textContent