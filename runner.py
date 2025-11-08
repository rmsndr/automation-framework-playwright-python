import argparse
import os
import pytest

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tenant", required=True, help="Tenant to run tests against")
    parser.add_argument("--browser", default="chromium", help="Browser type")
    parser.add_argument("--path", default="case_search/tests", help="Path to tests")
    parser.add_argument("--marker", help="Pytest marker to select tests")
    parser.add_argument("--test", help="Specific test file or test function")
    parser.add_argument("--user_type", choices=["new", "existing"], default="new", help="Run as new or existing user")

    args = parser.parse_args()

    # Export tenant and browser as environment variables
    os.environ["tenant"] = args.tenant
    os.environ["browser"] = args.browser

    # Build pytest args – only forward user_type (pytest knows about this)
    pytest_args = [args.path, f"--user_type={args.user_type}"]

    if args.marker:
        pytest_args.extend(["-m", args.marker])
    if args.test:
        pytest_args.append(args.test)

    print(f"Running tests for tenant: {args.tenant} on browser: {args.browser} as {args.user_type} user")
    pytest.main(pytest_args)

if __name__ == "__main__":
    main()