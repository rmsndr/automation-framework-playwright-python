from playwright.sync_api import Page, expect

class AdvancedSearchPage:
    def __init__(self, page: Page):
        self.page = page

    def criteria_dropdown(self):
        return self.page.get_by_label("Select search criteria")

    def hearing_type_trigger(self):
        return self.page.get_by_text("Search for Hearing Type")

    def hearing_type_field(self):
        return self.page.get_by_role("textbox", name="Search for Hearing Type")

    def search_button(self):
        return self.page.get_by_role("button", name="Search")

    def search_results(self):
        return self.page.locator("#advanced-search-results")
    

    def case_description_field(self):
        return self.page.get_by_role("textbox", name="Case Description")

    def first_search_result(self):
        return self.page.locator("#advanced-search-results >> nth=0")



