from playwright.sync_api import Page, Locator

class InventoryPage:
    def __init__ (self, page: Page):
        self.page = page
        # Locators for InventoryPage
        self.add_to_cart_backpack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.add_to_cart_bike_light = page.locator("#add-to-cart-sauce-labs-bike-light")
        self.cart_icon = page.locator(".shopping_cart_link")
        
        #accessibility for InventoryPage
        self.header_role = page.locator('[role="banner"]')
        self.main_role = page.locator('[role="main"]')
        self.nav_role = page.locator('[role="navigation"]')
        self.product_images = page.locator("img")


    def add_backpack_to_cart(self):
        self.add_to_cart_backpack.click()

    def add_bike_light_to_cart(self):
        self.add_to_cart_bike_light.click()
    
    def navigate_to_cart(self):
        self.cart_icon.click()
        self.page.wait_for_url("https://www.saucedemo.com/cart.html")

    def get_backpack_price(self):
        # Assuming the backpack price is obtained from executing a JavaScript query
        backpack_price = self.page.evaluate(
            "document.querySelector('#item_4_title_link').parentElement.parentElement.querySelector('.inventory_item_price').textContent"
        )
        return backpack_price if backpack_price else Exception("Backpack price not found")

    # $('#item_4_title_link').parentElement.parentElement.querySelector(".inventory_item_price").textContent
