from playwright.sync_api import Page

class ContactInfoPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_contact_info(self, name: str, address1: str, address2: str, city: str, state: str, county: str, zip_code: str, phone: str):
        self.page.get_by_role("textbox", name="Your Name or Your Firm /").fill(name)
        self.page.get_by_role("textbox", name="Address Line 1 *").fill(address1)
        self.page.get_by_role("textbox", name="Address Line 2").fill(address2)
        self.page.get_by_role("textbox", name="City *").fill(city)
        self.page.get_by_label("State *").select_option(state)
        self.page.get_by_label("County *").select_option(county)
        self.page.get_by_role("textbox", name="ZIP Code *").fill(zip_code)
        self.page.get_by_role("textbox", name="Phone Number *").fill(phone)

    def continue_next(self):
        self.page.get_by_role("button", name="Next").click()