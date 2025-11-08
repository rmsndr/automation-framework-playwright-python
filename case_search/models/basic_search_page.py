from playwright.sync_api import Page, expect

class BasicSearchPage:
    def __init__(self, page: Page):
        self.page = page

    def first_result(self):
        return self.page.locator("#basic-search-results .result-item").first

    def got_it_popup_button(self):
        return self.page.get_by_role("button", name="Got It")

    def sorting_dropdown(self):
        # The label is 'Sorting Options' in the recording
        return self.page.get_by_label("Sorting Options")

    def advanced_search_button(self):
        # The recording uses a link named 'Advanced'
        return self.page.get_by_role("link", name="Advanced")

    def results_table(self):
        return self.page.locator("tbody")

