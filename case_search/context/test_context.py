import json
from pathlib import Path
from playwright.sync_api import sync_playwright

class TestContext:
    __test__ = False

    def __init__(self, tenant: str, browser_type: str):
        self.tenant = tenant
        self.browser_type = browser_type
        self.browser = self._launch_browser()
        self.page = None
        self.config = self._load_config(tenant)
        self.base_url = self.config.get("base_url")
        self.features = self.config.get("features", {})
        self.email = None  # To be set during user login
        self.default_password = self.config.get("default_password")

    def _launch_browser(self):
        p = sync_playwright().start()
        if self.browser_type == "chromium":
            return p.chromium.launch(headless=False)
        elif self.browser_type == "firefox":
            return p.firefox.launch(headless=False)
        elif self.browser_type == "webkit":
            return p.webkit.launch(headless=False)
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")

    def _load_config(self, tenant: str):
        config_path = Path(__file__).parent.parent / "configs" / f"{tenant}.json"
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found for tenant: {tenant}")
        with open(config_path, "r") as f:
            return json.load(f)

    def launch_page(self):
        self.page = self.browser.new_page()
        self.page.goto(self.base_url)
        return self.page