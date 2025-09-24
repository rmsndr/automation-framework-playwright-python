from playwright.sync_api import Page

class UserTypePage:
    def __init__(self, page: Page):
        self.page = page

    def select_general_public(self):
        self.page.get_by_text("General Public").click()
        self.page.get_by_role("button", name="Continue").click()