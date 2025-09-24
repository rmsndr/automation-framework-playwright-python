import os
import pytest
from case_search.context.test_context import TestContext
from case_search.protocol.register_user import register_user

@pytest.mark.registration
@pytest.mark.smoke
def test_registration():
    tenant = os.getenv("tenant", "txstage")
    browser_type = os.getenv("browser", "chromium")

    context = TestContext(tenant, browser_type)
    context.launch_page()

    register_user(context)

    #assert context.page.locator("text=Quick Search").is_visible()
    context.browser.close()