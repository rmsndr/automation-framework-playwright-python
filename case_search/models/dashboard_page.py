from playwright.sync_api import Page
from case_search.models.basic_search_page import BasicSearchPage
from case_search.models.advanced_search_page import AdvancedSearchPage

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

    class SubscriptionModal:
        def __init__(self, page: Page):
            self.page = page

        def select_basic(self):
            self.page.get_by_role("button", name="Get Basic").click()

        def maybe_later(self):
            self.page.get_by_role("button", name="Maybe Later").click()

    def open_basic_search(self, query: str) -> BasicSearchPage:
        self.page.get_by_role("textbox", name="Quick Search").fill(query)
        self.page.get_by_role("button", name="Search").click()
        return BasicSearchPage(self.page)

    def open_advanced_search(self) -> AdvancedSearchPage:
        self.page.get_by_role("button", name="Advanced Search").click()
        return AdvancedSearchPage(self.page)

    def open_profile_menu(self):
        self.page.get_by_role("button", name="Profile Menu").click()

    def sign_out(self):
        self.page.get_by_role("button", name="Sign out").click()