# tests/conftest.py
import pytest
import os
from pytest_html import extras
from playwright.sync_api import Page

# Screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = None
        # Check for page_with_video first, then regular page, then context
        if "page_with_video" in item.funcargs:
            page = item.funcargs["page_with_video"]
        elif "page" in item.funcargs:
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

@pytest.fixture
def page_with_video(page: Page):
    """
    Fixture that provides a page with video recording enabled.
    Can be used by any test that needs video recording by using 'page_with_video' instead of 'page'.
    
    Usage:
        def test_example(page_with_video: Page):
            page_with_video.goto("https://example.com")
            # Video will be automatically saved when test completes
    """
    # Get the browser from the existing page context
    browser = page.context.browser
    if browser is None:
        # If browser is not available, use the default page fixture
        yield page
        return
    
    # Create a new context with video recording enabled
    video_dir = "saucedemo/videos"
    os.makedirs(video_dir, exist_ok=True)
    
    # Create new context with video recording
    context = browser.new_context(
        record_video_dir=video_dir,
        record_video_size={"width": 1280, "height": 720}
    )
    video_page = context.new_page()
    
    yield video_page
    
    # Close the context (this will save the video automatically)
    context.close()