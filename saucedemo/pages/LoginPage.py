from playwright.sync_api import Page

class LoginPage: #blueprint for the LoginPage class
    def __init__(self, page: Page): #tells Playwright this is a browser page we can interact with
        #self is a reference to the instance of the class (object) being created
        #page is a Playwright object that represents the browser page we want to interact with
        self.page = page #- Stores the page object inside the class so other methods like login() can use it.        
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()