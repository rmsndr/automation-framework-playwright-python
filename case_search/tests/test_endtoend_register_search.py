import os
import pytest
from case_search.context.test_context import TestContext
from case_search.protocol.register_user import register_user
from case_search.protocol.activate_account import activate_account
from case_search.protocol.login_user import login_user
from case_search.protocol.onboard_user import onboard_user
from case_search.protocol.search_case import search_case
from case_search.models.dashboard_page import DashboardPage

STATE_FILE = "state/session_state.json"
EMAIL_FILE = "state/last_user.txt"

@pytest.mark.endtoend
def test_registeration(user_type="new"):
    print(f"Running as {user_type} user")
    tenant = os.getenv("tenant", "txstage")
    browser = os.getenv("browser", "chromium")

    context = TestContext(tenant, browser)

    # Launch page with resume support
    if os.path.exists(STATE_FILE) and os.path.exists(EMAIL_FILE):
        context.browser_context = context.browser.new_context(storage_state=STATE_FILE)
        context.page = context.browser_context.new_page()
        with open(EMAIL_FILE) as f:
            context.generated_email = f.read().strip()
        print(f"[Resume] Loaded session for {context.generated_email}")
        context.page.goto(context.base_url)
    else:
        context.launch_page()

    # Only register/activate if no saved email
    if not context.generated_email and user_type == "new":
        register_user(context)
        activate_account(context)

    print("[DEBUG] Before login_user, current page URL:", context.page.url)
    # Persist session + email after successful login
    context.browser_context.storage_state(path=STATE_FILE)
    with open(EMAIL_FILE, "w") as f:
        f.write(context.generated_email)
    print(f"[Persist] Saved session for {context.generated_email}")

    login_user(context)
    onboard_user(context)   # adaptive: handles terms + contact info if needed
    search_case(context)    
    dashboard = DashboardPage(context.page)
    try:
        dashboard.open_profile_menu()
        dashboard.sign_out()
    except Exception as e:
        print(f"[WARN] Could not sign out cleanly: {e}")
    context.browser.close()
    print("[Test Complete] End-to-end register/search test finished.")