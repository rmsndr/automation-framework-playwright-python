from playwright.sync_api import Page

class CheckoutCompletePage:
    def __init__(self, page: Page):
        self.page = page

    def verify_order_confirmation_message(self):
        """Verify and return the order confirmation message."""
        confirmation_message = self.page.locator(".complete-header")
        if not confirmation_message.is_visible():
            raise ValueError("Order confirmation message not found")
        return confirmation_message.text_content()
    #returns text content of the confirmation message - Thank you for your order!ll 