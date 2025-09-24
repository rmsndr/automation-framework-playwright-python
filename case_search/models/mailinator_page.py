from playwright.sync_api import Page, expect

class MailinatorPage:
    def __init__(self, page: Page):
        self.page = page

    def open_inbox(self, email: str):
        self.page.goto("https://www.mailinator.com/")
        self.page.get_by_role("textbox", name="Enter public inbox").fill(email)
        self.page.get_by_role("button", name="GO").click()

    def open_activation_email(self):
        self.page.get_by_role("cell", name="re:SearchTX - Activate Account").click()

    def click_activation_link(self):
        frame = self.page.frame(name="html_msg_body")
        with self.page.expect_popup() as popup_info:
            frame.get_by_role("link", name="Activate Account").click()
        return popup_info.value