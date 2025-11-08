import re
from playwright.sync_api import expect
from case_search.models.activation_page import ActivationPage
from case_search.protocol.mailinator_protocol import open_mailinator_inbox, click_activation_link_and_capture_popup

def activate_account(context):
    """
    Protocol that:
    - opens Mailinator in a new tab
    - opens the activation message (subject driven by client_code on context)
    - clicks the activation link and captures the popup deterministically
    - performs Sign in on the activation page and switches context.page to that tab
    """
    email = context.generated_email
    if not email:
        raise ValueError("No generated email found in context. Run register_user first.")

    client_code = getattr(context, "client_code", "TX")  # reasonable default if not provided

 
    open_mailinator_inbox(context.page, email, client_code)
    activation_page = click_activation_link_and_capture_popup(context.page)


    # Switch context.page so subsequent protocols operate on the activation tab
    context.page = activation_page

    # Guards: ensure the popup loaded an activation flow
    # Wait for the activation tab to open and load (can take up to 30 seconds)
    expect(context.page).to_have_url(re.compile("AccountActivated|activation"), timeout=30000)
    #https://researchtx-stage.tylerhost.net/CourtRecordsSearch/Account/AccountActivated/50e6a272-46ea-4eae-a8c8-248640fb2fe9#!/profile
    # Perform Sign in on the activation page (models remain locator-only)
    activation = ActivationPage(context.page)
    expect(activation.sign_in_button()).to_be_visible(timeout=10000)
    activation.sign_in_button().click()

    print(f"[Activation] Activated account for {email} and switched to activation tab.")

