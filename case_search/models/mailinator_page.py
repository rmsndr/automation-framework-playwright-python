from playwright.sync_api import Page, Locator

class MailinatorPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_mailinator(self):
        return self.page.goto("https://www.mailinator.com/")

    def inbox_textbox(self) -> Locator:
        return self.page.get_by_role("textbox", name="Enter public inbox")

    def go_button(self) -> Locator:
        return self.page.get_by_role("button", name="GO")

    def activation_email_subject_for(self, client_code: str) -> str:
        # returns the message subject substring to search for; caller provides client_code like "TX", "CA", etc.
        return f"re:Search{client_code} - Activate Account"

    def activation_email_cell(self, client_code: str) -> Locator:
        subject = self.activation_email_subject_for(client_code)
        return self.page.get_by_role("cell", name=subject)

    def activation_email_frame_locator(self) -> Locator:
        return self.page.frame_locator("iframe#html_msg_body, iframe[id='html_msg_body'], iframe[name='html_msg_body']")

    # def activation_link_in_frame(self, name_substring: str = "Activate Account") -> Locator:
    #     return self.activation_email_frame_locator().get_by_role("link", name=name_substring, exact=False)

    def activation_link_on_page(self, name_substring: str = "Activate Account") -> Locator:
        return self.page.get_by_role("link", name=name_substring, exact=True)

    def activation_link_in_frame(self):
        return self.activation_email_frame_locator().get_by_role("link", name="Activate Account")

    
    