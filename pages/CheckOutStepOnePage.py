from playwright.sync_api import Page
from typing import Optional

class CheckOutStepOnePage:
    def __init__(self, page: Page):
        self.page = page

    def click_continue_button(self):
        continue_button = self.page.locator("#continue")
        continue_button.click()
        #self.page.wait_for_url("https://www.saucedemo.com/checkout-step-two.html")

    def error_message(self):
        error_message = self.page.locator(".error-message-container")
        return error_message.text_content() if error_message else None
    
    def fill_checkout_information(self, first_name: Optional[str] = None, 
                        last_name: Optional[str] = None, 
                        postal_code: Optional[str] = None):
        if first_name is not None:
            self.page.locator("#first-name").fill(first_name)
        if last_name is not None:
            self.page.locator("#last-name").fill(last_name)
        if postal_code is not None:
            self.page.locator("#postal-code").fill(postal_code)