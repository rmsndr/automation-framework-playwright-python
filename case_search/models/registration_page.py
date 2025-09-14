from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

    def open_registration_form(self):
        self.page.get_by_role("link", name="Register", exact=True).click()

    def fill_user_details(self, first_name, last_name, email, password):
        self.page.get_by_role("textbox", name="First Name").fill(first_name)
        self.page.get_by_role("textbox", name="Last Name").fill(last_name)
        self.page.get_by_role("textbox", name="Email").fill(email)
        self.page.get_by_role("textbox", name="Password", exact=True).fill(password)
        self.page.get_by_role("textbox", name="Confirm Password").fill(password)

    def submit_registration(self):
        self.page.get_by_role("button", name="Register").click()

    def confirm_success(self):
        return self.page.get_by_role("alert")