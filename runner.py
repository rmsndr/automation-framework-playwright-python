import os
import argparse
import pytest

def main():
    parser = argparse.ArgumentParser(description="Run Playwright tests with tenant and browser context.")
    parser.add_argument("--tenant", required=True, help="Tenant name (e.g., txstage, castage)")
    parser.add_argument("--browser", default="chromium", help="Browser type (chromium, firefox, webkit)")
    parser.add_argument("--path", help="Path to specific test file")
    parser.add_argument("--marker", help="Run tests with specific pytest marker")
    parser.add_argument("--test", help="Run specific test function (e.g., test_registration)")

    args = parser.parse_args()

    # Export tenant and browser as environment variables
    os.environ["tenant"] = args.tenant
    os.environ["browser"] = args.browser

    print(f"Running tests for tenant: {args.tenant} on browser: {args.browser}")

    pytest_args = [args.path if args.path else "case_search/tests", "-s"]

    if args.marker:
        pytest_args.extend(["-m", args.marker])
    if args.test:
        pytest_args.append(f"::{args.test}")

    pytest.main(pytest_args)

if __name__ == "__main__":
    main()