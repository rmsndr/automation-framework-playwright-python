from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

    class SubscriptionModal:
        def __init__(self, page: Page):
            self.page = page

        def get_basic_button(self):
            return self.page.get_by_role("button", name="Get Basic")

        def maybe_later_button(self):
            return self.page.get_by_role("button", name="Maybe Later")

    def basic_search_field(self):
        return self.page.get_by_role("textbox", name="Quick Search")

    def basic_search_button(self):
        return self.page.get_by_role("button", name="Search")

    def advanced_search_button(self):
        return self.page.get_by_role("button", name="Advanced Search")

    def profile_menu_button(self):
        return self.page.get_by_role("button", name="Profile Menu")

    def sign_out_button(self):
        return self.page.get_by_role("button", name="Sign out")

    def badge_research(self):
        return self.page.locator(".badge.badge-research")

    def search_icon_button(self):
        return self.page.get_by_role("button", name="")

    def consider_subscribing_modal(self):
        return self.page.locator("#considerSubscribingModal")

