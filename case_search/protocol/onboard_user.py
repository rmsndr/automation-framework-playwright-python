from playwright.sync_api import expect
from case_search.models.contact_info_page import ContactInfoPage
from case_search.models.user_type_page import UserTypePage

def onboard_user(context):
    page = context.page
    print("[Onboarding] Checking if onboarding is required...")

    # Step 1: Handle Terms modal
    try:
        contact_info = ContactInfoPage(page)
        terms = contact_info.terms_modal()
        terms.click_continue_if_visible()
        print("[Onboarding] Accepting Terms & Conditions")
    except Exception:
        print("[Onboarding] No Terms modal shown")

    # Step 2: Contact Info form
    try:
        contact_info = ContactInfoPage(page)
        # Wait for the contact info section to be visible before filling fields
        contact_info_section = page.locator("#FirmName")
        contact_info_section.wait_for(state="visible", timeout=10000)
        print("[Onboarding] Filling Contact Info")
        contact_info.fill_contact_info(
            name="Tyler Tech",
            address1="123 Main St",
            address2="Suite 100",
            city="Tyler",
            state="number:17",
            county="number:295",
            zip_code="75024",
            phone="2345678901"
        )
        contact_info.continue_next()

        # Step 3: Role type
        user_type = UserTypePage(page)
        user_type.select_general_public()
    except Exception:
        print("[Onboarding] Skipped Contact Info (likely existing user)")

    # Step 4: Verify dashboard
    expect(page.locator("text=Quick Search")).to_be_visible(timeout=20000)
    print("[Onboarding] Completed onboarding flow")
