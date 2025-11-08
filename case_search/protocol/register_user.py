import os
import uuid
from playwright.sync_api import expect
from case_search.models.registration_page import RegistrationPage

def register_user(context):
    page = context.page
    email = f"codegen_public_{uuid.uuid4().hex[:8]}@mailinator.com"
    context.generated_email = email

    print(f"[Registration] Using email: {email}")

    page.goto(context.base_url)
    registration = RegistrationPage(page)

    # Open registration
    registration.register_link.click()

    # Wait for form to appear
    expect(registration.first_name_field).to_be_visible(timeout=5000)

    # Fill form
    registration.first_name_field.fill("Test")
    registration.last_name_field.fill("Codegen")
    registration.email_field.fill(email)
    registration.password_field.fill("Abcd1234")
    registration.confirm_password_field.fill("Abcd1234")

    # Submit
    registration.register_button.click()

    # Persist email for reuse
    os.makedirs("case_search/tmp", exist_ok=True)
    with open("case_search/tmp/last_registered_email.txt", "w") as f:
        f.write(email)

    # Guard: wait for confirmation (adjust expected text to app actual)
    try:
        expect(registration.alert).to_be_visible(timeout=30000)
        # Optionally assert specific content
        # expect(registration.alert).to_contain_text("activation email", timeout=30000)
    except Exception:
        page.screenshot(path="case_search/screenshots/registration_failure.png")
        raise

    # Log result
    os.makedirs("case_search/logs", exist_ok=True)
    with open("case_search/logs/registration_log.txt", "a") as log:
        log.write(f"Registered user: {email}\n")

    print(f"Registered user: {email}")