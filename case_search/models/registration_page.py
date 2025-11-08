from playwright.sync_api import Page, Locator

class RegistrationPage:
    """Page model exposing registration page locators only (no actions)."""

    def __init__(self, page: Page):
        self.page = page

    @property
    def register_link(self) -> Locator:
        return self.page.get_by_role("link", name="Register", exact=True)

    @property
    def first_name_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="First Name")

    @property
    def last_name_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Last Name")

    @property
    def email_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Email")

    @property
    def password_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Password", exact=True)

    @property
    def confirm_password_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Confirm Password")

    @property
    def register_button(self) -> Locator:
        return self.page.get_by_role("button", name="Register")

    @property
    def alert(self) -> Locator:
        return self.page.get_by_role("alert")