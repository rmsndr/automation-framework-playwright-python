from playwright.sync_api import Page, expect
from case_search.models.advanced_search_page import AdvancedSearchPage

class BasicSearchPage:
    def __init__(self, page: Page):
        self.page = page

    def validate_first_result_contains(self, term: str):
        first_result = self.page.locator("#basic-search-results .result-item").first
        expect(first_result).to_contain_text(term)

    def open_advanced_search(self) -> AdvancedSearchPage:
        self.page.get_by_role("button", name="Advanced Search").click()
        return AdvancedSearchPage(self.page)