import asyncio
from playwright.async_api import async_playwright

async def main():
    # Define the iOS device emulation settings
    ios_device = {
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "viewport": {"width": 390, "height": 844},  # iPhone 12 dimensions
        "deviceScaleFactor": 3,
        "isMobile": True,
        "hasTouch": True,
    }

    # Launch the browser
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Set headless=True to run without a UI
        context = await browser.new_context(
            user_agent=ios_device["userAgent"],
            viewport=ios_device["viewport"],
            device_scale_factor=ios_device["deviceScaleFactor"],
            is_mobile=ios_device["isMobile"],
            has_touch=ios_device["hasTouch"]
        )
        page = await context.new_page()

        # Navigate to the website
        url = "https://www.uol.com.br"
        await page.goto(url)

        # Perform a functional test: Get the page title
        title = await page.title()

        # Save the results to a text file
        with open("ios_emulation_results.txt", "w", encoding="utf-8") as file:
            file.write(f"Website URL: {url}\n")
            file.write(f"Page Title: {title}\n")
        
        print("Test completed. Results saved to 'ios_emulation_results.txt'.")

        # Close the browser
        await browser.close()

# Run the script
asyncio.run(main())
