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
        # Assuming the backpack price is obtained from executing a JavaScript query
        backpack_price = self.page.evaluate(
            "document.querySelector('#item_4_title_link').nextElementSibling.nextElementSibling.querySelector('.inventory_item_price').textContent"
        )
        return backpack_price if backpack_price else Exception("Backpack price not found")
    #$('#item_4_title_link').nextElementSibling.nextElementSibling.querySelector(".inventory_item_price").textContent