from playwright.sync_api import Page, Locator

class FingerPrintSignOutPage:
    """
    Page model for the 'You already have an active session in progress' (fingerprint sign-out) page.
    """
    def __init__(self, page: Page):
        self.page = page

    @property
    def sign_in_end_other_session_button(self) -> Locator:
        return self.page.get_by_role("button", name="SIGN IN AND END THE OTHER SESSION", exact=True)

    def click_sign_in_end_other_session_and_wait(self, wait_url: str = None, timeout: int = 15000):
        """
        Clicks the 'SIGN IN AND END THE OTHER SESSION' button if visible and waits for navigation.
        Optionally waits for a specific URL if wait_url is provided.
        """
        button = self.sign_in_end_other_session_button
        if button.is_visible(timeout=10000):
            if wait_url:
                with self.page.expect_navigation(url=wait_url, timeout=timeout):
                    button.click()
            else:
                with self.page.expect_navigation(timeout=timeout):
                    button.click()
            return True
        return False
