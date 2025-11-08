from playwright.sync_api import expect, Page
from case_search.models.dashboard_page import DashboardPage
from case_search.models.basic_search_page import BasicSearchPage
from case_search.models.advanced_search_page import AdvancedSearchPage

# Helpers

def dismiss_subscription_modal_if_present(dashboard: DashboardPage, timeout: int = 2000) -> None:
    try:
        modal = dashboard.subscription_modal()
        maybe_later = modal.get_maybe_later_button()
        if maybe_later.is_visible(timeout=timeout):
            maybe_later.click()
    except Exception:
        pass

def enter_quick_search_text(dashboard: DashboardPage, text: str) -> None:
    search_field = dashboard.quick_search_textbox()
    expect(search_field).to_be_visible(timeout=5000)
    search_field.click()
    search_field.fill(text)

def click_quick_search_and_open_basic(dashboard: DashboardPage) -> BasicSearchPage:
    # Try primary button; fall back to alternate icon if necessary
    try:
        dashboard.quick_search_button().click()
    except Exception:
        dashboard.search_icon_button().click()
    # Wait for a reliable BasicSearchPage anchor
    expect(dashboard.badge_research()).to_be_visible(timeout=10000)
    return BasicSearchPage(dashboard.page)

def dismiss_got_it_popup_if_present(basic: BasicSearchPage, timeout: int = 2000) -> None:
    try:
        popup = basic.got_it_popup_button()
        if popup.is_visible(timeout=timeout):
            popup.click()
    except Exception:
        pass

def select_sorting_option(basic: BasicSearchPage, option_name: str = "Relevance") -> None:
    valid_options = ["Relevance", "Case Filed Date - Newest", "Case Filed Date - Oldest"]
    if option_name not in valid_options:
        raise ValueError(f"Invalid sorting option: {option_name}. Choose from {valid_options}")
    dropdown = basic.sorting_dropdown()
    expect(dropdown).to_be_visible(timeout=3000)
    dropdown.select_option(label=option_name)

def validate_first_result_contains(basic: BasicSearchPage, text: str) -> None:
    first = basic.first_result()
    expect(first).to_be_visible(timeout=10000)
    expect(first).to_contain_text(text, timeout=10000)

def open_advanced_search_from_basic(basic: BasicSearchPage) -> AdvancedSearchPage:
    basic.advanced_search_button().click()
    expect(basic.page.locator("#AdvancedSearchCard")).to_be_visible(timeout=10000)
    return AdvancedSearchPage(basic.page)

def set_advanced_search_criteria(advanced: AdvancedSearchPage, value: str) -> None:
    selector = advanced.page.get_by_label("Select search criteria")
    expect(selector).to_be_visible(timeout=5000)
    selector.select_option(value)

def search_case_description(advanced: AdvancedSearchPage, text: str) -> None:
    desc = advanced.page.get_by_role("textbox", name="Case Description")
    expect(desc).to_be_visible(timeout=5000)
    desc.click()
    desc.fill(text)
    advanced.page.get_by_role("button", name="Search").click()

def validate_advanced_first_result_contains(advanced: AdvancedSearchPage, text: str) -> None:
    results = advanced.page.locator("#advanced-search-results")
    expect(results).to_be_visible(timeout=10000)
    expect(results).to_contain_text(text, timeout=10000)


# Orchestration

def search_case(context) -> None:
    """
    1) Dismiss subscription modal on dashboard
    2) Perform quick search for 'trial' and validate results
    3) Open advanced search, set criteria, search description, and validate results
    """
    page: Page = context.page

    # Step 1: Dashboard
    dashboard = DashboardPage(page)
    dismiss_subscription_modal_if_present(dashboard)
    enter_quick_search_text(dashboard, "trial")
    basic_search = click_quick_search_and_open_basic(dashboard)

    # Step 2: Basic search
    dismiss_got_it_popup_if_present(basic_search)
    select_sorting_option(basic_search, "Relevance")
    validate_first_result_contains(basic_search, "trial")

    # Step 3: Advanced search
    advanced_search = open_advanced_search_from_basic(basic_search)
    set_advanced_search_criteria(advanced_search, "number:6")
    search_case_description(advanced_search, "trial")
    validate_advanced_first_result_contains(advanced_search, "trial")