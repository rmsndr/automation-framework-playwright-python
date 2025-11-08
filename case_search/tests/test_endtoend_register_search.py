from multiprocessing import context
import os
import pytest
from case_search.context.test_context import TestContext
from case_search.protocol.register_user import register_user
from case_search.protocol.activate_account import activate_account
from case_search.protocol.login_user import login_user
from case_search.protocol.onboard_user import onboard_user
from case_search.protocol.search_case import search_case
from case_search.models.dashboard_page import DashboardPage

@pytest.mark.endtoend
def test_registeration(user_type = "new"):
    print(f"Running as {user_type} user")
    # tenant and browser still come from os.getenv
    tenant = os.getenv("tenant", "txstage")
    browser = os.getenv("browser", "chromium")

    context = TestContext(tenant, browser)
    context.launch_page()

    try:
        if user_type == "new":
            register_user(context)
            # create a new tab
            activate_account(context)
        print("[DEBUG] Before login_user, current page URL:", context.page.url)

        login_user(context)
        onboard_user(context)   # adaptive: handles terms + contact info if needed
        search_case(context)

    finally:
        dashboard = DashboardPage(context.page)
        try:
            dashboard.open_profile_menu()
            dashboard.sign_out()
        except Exception as e:
            print(f"[WARN] Could not sign out cleanly: {e}")
        context.browser.close()
#python runner.py --tenant txstage --browser chromium --marker endtoend --user_type new
#python runner.py --tenant txstage --browser chromium --marker endtoend --user_type existing