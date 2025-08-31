# tests/conftest.py

import pytest
import os
from pytest_html import extras

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            page.screenshot(path=screenshot_path)

            # Embed screenshot in HTML report
            if hasattr(rep, "extra"):
                rep.extra.append(extras.image(screenshot_path))