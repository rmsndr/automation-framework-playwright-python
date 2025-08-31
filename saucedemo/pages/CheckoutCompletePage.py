from symtable import Class
from playwright.sync_api import Page

class CheckoutCompletePage:
    def __init__(self, page: Page):
        self.page = page

    def verify_order_confirmation_message(self):
        confirmation_message = self.page.locator(".complete-header")
        return confirmation_message.text_content() if confirmation_message else Exception("Confirmation message not found")
    #returns text content of the confirmation message - Thank you for your order!ll 