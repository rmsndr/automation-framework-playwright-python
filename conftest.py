# tests/conftest.py
import pytest
import os
from pytest_html import extras

# Screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = None
        if "page" in item.funcargs:
            page = item.funcargs["page"]
        elif "context" in item.funcargs:
            page = item.funcargs["context"].page

        if page:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            page.screenshot(path=screenshot_path)

            if hasattr(rep, "extra"):
                rep.extra.append(extras.image(screenshot_path))

# Register CLI options
def pytest_addoption(parser):

    parser.addoption(
        "--user_type",
        action="store",
        default="new",
        choices=["new", "existing"],
        help="Choose whether to run flow as new or existing user"
    )

# Fixtures for easy access

@pytest.fixture
def user_type(request):
    return request.config.getoption("--user_type")