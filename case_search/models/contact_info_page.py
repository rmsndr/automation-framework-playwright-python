from playwright.sync_api import Page, Locator

class ContactInfoPage:
    def continue_next(self, timeout: int = 10000):
        """
        Clicks the Next button to proceed after filling the contact info form.
        """
        next_btn = self.next_button()
        next_btn.wait_for(state="visible", timeout=timeout)
        next_btn.click()

    def fill_contact_info(self, name: str, address1: str, address2: str, city: str, state: str, county: str, zip_code: str, phone: str, timeout: int = 10000):
        """
        Fills out the contact info form fields.
        """
        self.name_field().wait_for(state="visible", timeout=timeout)
        self.name_field().fill(name)
        self.address1_field().fill(address1)
        self.address2_field().fill(address2)
        self.city_field().fill(city)
        self.state_select().select_option(state)
        self.county_select().select_option(county)
        self.zip_code_field().fill(zip_code)
        self.phone_field().fill(phone)
    def __init__(self, page: Page):
        self.page = page

    class TermsModal:
        def __init__(self, page: Page):
            self.page = page

        def continue_button(self) -> Locator:
            # Locate the Continue button inside the modal by modal id
            return self.page.locator("#termsAndConditionsModal button.btn.btn-primary", has_text="Continue")

        def click_continue_if_visible(self, timeout: int = 10000):
            # Wait for the modal to be visible, then click the Continue button if visible
            modal = self.page.locator("#termsAndConditionsModal")
            try:
                modal.wait_for(state="visible", timeout=timeout)
                btn = self.continue_button()
                btn.wait_for(state="visible", timeout=timeout)
                btn.click()
                print("[ContactInfoPage] Clicked Continue on Terms modal")
            except Exception:
                pass


    def terms_modal(self) -> TermsModal:
        return self.TermsModal(self.page)

    def name_field(self) -> Locator:
        return self.page.get_by_label("Your Name or Your Firm")

    def address1_field(self) -> Locator:
        return self.page.get_by_label("Address Line 1 *")

    def address2_field(self) -> Locator:
        return self.page.get_by_label("Address Line 2")

    def city_field(self) -> Locator:
        return self.page.get_by_label("City *")

    def state_select(self) -> Locator:
        return self.page.get_by_label("State *")

    def county_select(self) -> Locator:
        return self.page.get_by_label("County *")

    def zip_code_field(self) -> Locator:
        return self.page.get_by_label("ZIP Code *")

    def phone_field(self) -> Locator:
        return self.page.get_by_label("Phone Number *")

    def next_button(self) -> Locator:
        return self.page.get_by_role("button", name="Next")