import json
from pathlib import Path

class TestContext:
    def __init__(self, tenant: str, browser):
        self.tenant = tenant
        self.browser = browser
        self.page = None
        self.config = self._load_config(tenant)
        self.base_url = self.config.get("base_url")
        self.features = self.config.get("features", {})

    def _load_config(self, tenant: str):
        config_path = Path(__file__).parent.parent / "configs" / f"{tenant}.json"
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found for tenant: {tenant}")
        with open(config_path, "r") as f:
            return json.load(f)

    def launch_page(self):
        self.page = self.browser.new_page()
        self.page.goto(self.base_url)