# case_search/protocols/mailinator_protocol.py
from playwright.sync_api import Page, expect
from case_search.models.mailinator_page import MailinatorPage

'''
def open_mailinator_inbox(page: Page, email: str, client_code: str) -> None:
    mail = MailinatorPage(page)
    mail.goto_mailinator()
    mail.inbox_textbox().fill(email)
    mail.go_button().click()
    expect(mail.activation_email_cell(client_code)).to_be_visible(timeout=20000)
    mail.activation_email_cell(client_code).click()
    # Wait for message body to render either in iframe or on page
    try:
        mail.activation_email_frame_locator().first.wait_for(timeout=15000)
    except Exception:
        # try:
        #     mail.page.locator(".msg-body, #msg_body").wait_for(state="visible", timeout=15000)
        # except Exception:
        print("[DEBUG] Could not find message body in iframe or page.")
        print("[DEBUG] Page content snippet:", mail.page.content()[:1000])
        raise


def click_activation_link_and_capture_popup(page: Page, client_code: str) -> Page:
    mail = MailinatorPage(page)
    # Wait for the iframe to be attached
    frame_locator = mail.activation_email_frame_locator()
    frame_locator.wait_for(timeout=15000)
    # Select the link by its text inside the iframe
    link = frame_locator.get_by_text("Activate Account", exact=True)
    link.wait_for(timeout=10000)
    with page.expect_popup() as popup_info:
        link.click()
    activation_page = popup_info.value
    expect(activation_page).not_to_be_none()
    return activation_page

'''
def open_mailinator_inbox(page: Page, email: str, client_code: str) -> None:
    mail = MailinatorPage(page)
    mail.goto_mailinator()
    mail.inbox_textbox().fill(email)
    mail.go_button().click()
    expect(mail.activation_email_cell(client_code)).to_be_visible(timeout=20000)
    mail.activation_email_cell(client_code).click()
    # Wait for the "Activate Account" link inside the iframe to appear
    frame_locator = mail.activation_email_frame_locator()
    link = frame_locator.get_by_text("Activate Account", exact=True)
    link.wait_for(timeout=15000)

def click_activation_link_and_capture_popup(page: Page) -> Page:
    mail = MailinatorPage(page)
    # Wait for the "Activate Account" link inside the iframe to appear
    frame_locator = mail.activation_email_frame_locator()
    link = frame_locator.get_by_text("Activate Account", exact=True)
    link.wait_for(timeout=10000)
    with page.expect_popup() as popup_info:
        link.click()
    activation_page = popup_info.value
    assert activation_page is not None, "Activation popup did not open"
    return activation_page