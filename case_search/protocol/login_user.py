from playwright.sync_api import expect
from case_search.models.login_page import LoginPage

def login_user(context):
    if not context.email:
        try:
            with open("case_search/tmp/last_registered_email.txt") as f:
                context.email = f.read().strip()
                print(f"[Login] Loaded persisted email: {context.email}")
        except FileNotFoundError:
            raise ValueError("No generated email found. Run new user flow first.")

    email = context.email
    password = context.default_password
    if not email:
        raise ValueError("No generated email found in context. Did you run register_user first?")


    print(f"[Login] Logging in with {email}")

    page = context.page
    login = LoginPage(page)
    # Ensure the login page is loaded
    login.expect_sign_in_info_message()  # wait for sign-in info message to appear
    
    # Step 1: Open login form
    login.email_field.fill(email)

    # Step 2: Fill credentials
    login.password_field.fill(password)

    # Step 3: Submit login
    login.form_submit_button.click()

    # Step 4: Verify landing page
    expect(page.locator("text=Quick Search")).to_be_visible(timeout=15000)

    print("[Login] Successfully logged in")