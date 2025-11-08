import os
import datetime
from playwright.sync_api import Page

def take_screenshot(page: Page, name: str, folder: str = "case_search/screenshots") -> str:
    """
    Capture a screenshot with a timestamped filename.

    Args:
        page (Page): The Playwright page object.
        name (str): A short descriptive name for the screenshot.
        folder (str): Directory to save screenshots (default: case_search/screenshots).

    Returns:
        str: The full path of the saved screenshot.
    """
    # Ensure folder exists
    os.makedirs(folder, exist_ok=True)

    # Timestamped filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"
    path = os.path.join(folder, filename)

    try:
        page.screenshot(path=path, full_page=True)
        print(f"[Screenshot] Saved: {path}")
    except Exception as e:
        print(f"[Screenshot] Failed to capture screenshot: {e}")
        return ""

    return path


def safe_expect(locator, assertion_fn, screenshot_name: str, **kwargs):
    """
    Wraps a Playwright expect assertion with screenshot-on-failure.

    Args:
        locator: The Playwright locator to assert against.
        assertion_fn: A lambda or function that performs the assertion.
        screenshot_name (str): Base name for the screenshot file.
        kwargs: Extra keyword args passed to the assertion function.
    """
    try:
        assertion_fn(locator, **kwargs)
    except Exception:
        take_screenshot(locator.page, screenshot_name)
        raise