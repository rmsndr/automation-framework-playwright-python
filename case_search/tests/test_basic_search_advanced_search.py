import os
import pytest
from case_search.context.test_context import TestContext
from case_search.protocol.search_case import search_case
from case_search.protocol.login_user import login_user


@pytest.mark.endtoend
def test_login_search(context: TestContext):
    tenant = os.getenv("tenant", "txstage")
    browser_type = os.getenv("browser", "chromium")

    context = TestContext(tenant, browser_type)
    context.launch_page()
    user_credentials = {"username": "codegen_public_2eac4451@mailinator.com", "password": "Abcd1234"}
    login_user(context, **user_credentials)
    #generate code to login and perform a basic search and advanced search
    search_case(context)
    context.browser.close()