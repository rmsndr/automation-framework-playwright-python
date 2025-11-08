from playwright.sync_api import Page, Locator

class ContactInfoPage:
    def __init__(self, page: Page):
        self.page = page

    class TermsModal:
        def __init__(self, root: Locator):
            self._root = root

        def continue_button(self) -> Locator:
            #$("#termsAndConditionsModal .btn-primary").length 
            return self._root.locator("#termsAndConditionsModal").get_by_role("button", name="Continue")


    def terms_modal(self) -> TermsModal:
        modal_root = self.page.get_by_role("dialog", name="Terms")
        return self.TermsModal(modal_root)

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