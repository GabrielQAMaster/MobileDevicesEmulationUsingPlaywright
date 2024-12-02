from playwright.sync_api import sync_playwright

# File to save the results
OUTPUT_FILE = "functional_test_results.txt"

def perform_functional_test(playwright):
    # Emulate a Pixel 5 Android device
    pixel_5 = playwright.devices['Pixel 5']

    # Launch the browser
    browser = playwright.chromium.launch(headless=False)  # Set to True for headless mode
    context = browser.new_context(**pixel_5)

    # Open a new page
    page = context.new_page()

    # Visit the website
    url = "https://compendiumdev.co.uk"
    page.goto(url)

    # Perform tests
    test_results = []
    try:
        # Verify page title
        page_title = page.title()
        expected_title = "Software Testing Consultancy & Training"
        if expected_title in page_title:
            test_results.append(f"PASS: Page title is correct: '{page_title}'")
        else:
            test_results.append(f"FAIL: Page title mismatch. Expected: '{expected_title}', Found: '{page_title}'")

        # Check for the presence of specific navigation links
        links_to_check = ["HOME", "ABOUT", "BLOG", "CONTACT"]
        for link_text in links_to_check:
            try:
                locator = page.locator(f"text={link_text}")
                if locator.is_visible():
                    test_results.append(f"PASS: Link '{link_text}' is visible on the page.")
                else:
                    test_results.append(f"FAIL: Link '{link_text}' is not visible on the page.")
            except Exception as e:
                test_results.append(f"FAIL: Error checking link '{link_text}': {e}")

        # Check if the main heading is present
        main_heading = "Software Testing Services"
        try:
            heading_locator = page.locator(f"text={main_heading}")
            if heading_locator.is_visible():
                test_results.append(f"PASS: Main heading '{main_heading}' is visible on the page.")
            else:
                test_results.append(f"FAIL: Main heading '{main_heading}' is not visible on the page.")
        except Exception as e:
            test_results.append(f"FAIL: Error checking main heading '{main_heading}': {e}")

    except Exception as e:
        test_results.append(f"ERROR: Exception occurred during the test: {e}")

    # Save results to a file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for result in test_results:
            file.write(result + "\n")

    print(f"Functional test completed. Results saved to {OUTPUT_FILE}")

    # Close the browser
    browser.close()

# Run the script
with sync_playwright() as playwright:
    perform_functional_test(playwright)
