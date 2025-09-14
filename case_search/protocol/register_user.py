import uuid
from playwright.sync_api import expect
from case_search.models.registeration_page import RegistrationPage

def register_user(context):
    page = context.page
    email = f"codegen_public_{uuid.uuid4().hex[:8]}@mailinator.com"
    context.generated_email = email 

    print(f"[Registration] Using email: {email}")

    page.goto(context.base_url)
    registration = RegistrationPage(page)
    registration.open_registration_form()
    registration.fill_user_details("Test", "Codegen", email, "Abcd1234")
    registration.submit_registration()

    # Guard: wait for confirmation
    expect(registration.confirm_success()).to_contain_text("activation email", timeout=10000)

    # Log result
    with open("case_search/logs/registration_log.txt", "a") as log:
        log.write(f"Registered user: {email}\n")

    print("[Registration] Registration flow completed.")