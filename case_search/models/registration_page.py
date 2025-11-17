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
    
    def click_signin_and_wait(self, wait_url: str = None, timeout: int = 10000):
        """
        Clicks the sign-in button (by id) and waits for the next page to load.
        Optionally waits for a specific URL if wait_url is provided.
        """
        locator = self.page.locator("#signInLink")
        if wait_url:
            with self.page.expect_navigation(url=wait_url, timeout=timeout):
                locator.click()
        else:
            with self.page.expect_navigation(timeout=timeout):
                locator.click()
        return locator
    