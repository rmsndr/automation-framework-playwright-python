def login(context):
    if not context.features.get("login_required", True):
        print("Login not required for this tenant.")
        return

    page = context.page
    print(f"Logging in to {context.base_url}")

    # Example login flow — update selectors after Codegen
    page.goto(context.base_url)
    page.fill("#username", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Optional: wait for post-login element
    page.wait_for_selector("#search-form", timeout=5000)
    print("Login successful.")