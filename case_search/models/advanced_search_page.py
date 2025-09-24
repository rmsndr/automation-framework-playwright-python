from playwright.sync_api import Page, expect

class AdvancedSearchPage:
    def __init__(self, page: Page):
        self.page = page

    def select_criteria(self, criteria: str):
        self.page.get_by_label("Select search criteria").select_option(criteria)

    def search_hearing_type(self, hearing_type: str):
        self.page.get_by_text("Search for Hearing Type").click()
        self.page.get_by_role("textbox", name="Search for Hearing Type").fill(hearing_type)
        self.page.get_by_role("textbox", name="Search for Hearing Type").press("Enter")
        self.page.get_by_role("button", name="Search").click()
        expect(self.page.locator("#advanced-search-results")).to_contain_text(hearing_type)