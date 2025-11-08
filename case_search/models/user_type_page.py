from playwright.sync_api import Page

class UserTypePage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def general_public_option(self):
        return self.page.get_by_text("General Public")

    @property
    def continue_button(self):
        return self.page.get_by_role("button", name="Continue")