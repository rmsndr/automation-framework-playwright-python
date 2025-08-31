from playwright.sync_api import Page
from axe_playwright_python.sync_playwright import Axe



class accessibility_utils:
    @staticmethod
    def run_axe_scan(page: Page):
        """
        Run accessibility checks on the page using axe-core.
        """
        # Ensure axe-core is loaded
        axe = Axe()
        results = axe.run(page)
        
        # Run the accessibility scan
        return results
