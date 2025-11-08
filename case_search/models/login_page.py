from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def header_sign_in_button(self):
        return self.page.get_by_role("button", name="Sign in")

    @property
    def email_field(self):
        return self.page.get_by_role("textbox", name="Email")

    @property
    def password_field(self):
        return self.page.get_by_role("textbox", name="Password")

    @property
    def form_submit_button(self):
        return self.page.get_by_role("button", name="Sign In")
    
    def expect_sign_in_info_message(self):
        locator = self.page.locator("div.list-group-item.callout.callout-info")
        locator.get_by_text("Please sign in to continue").wait_for(state="visible", timeout=30000)