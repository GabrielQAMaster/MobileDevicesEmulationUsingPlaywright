📱 Functional Test with Pixel 5 Android Emulation Using Playwright
This repository contains a Python script that performs functional testing on the Compendium Dev website by emulating a Google Pixel 5 Android device using the Playwright framework.

🧪 What Does This Script Do?
Device Emulation:
Simulates browsing on a Pixel 5 device to test a mobile-friendly experience.
Functional Tests:
Validates the correctness of the page title.
Checks for the presence and visibility of key navigation links (HOME, ABOUT, BLOG, CONTACT).
Verifies the visibility of the main heading (Software Testing Services).
Result Logging:
Outputs a detailed pass/fail report to functional_test_results.txt.
🛠️ Tech Stack
Language: Python
Framework: Playwright
Emulated Device: Google Pixel 5
🚀 How to Run the Script
Prerequisites
Install Python 3.12+.
Install Playwright:
pip install playwright
Install Playwright's browser binaries:
playwright install
Steps to Execute
Clone this repository or download the script file.
Save the script as pixel_5_functional_test.py.
Open a terminal and navigate to the script's directory.
Run the script:
python functional_test.py
View the results in the functional_test_results.txt file generated in the same directory.
📝 Sample Output in functional_test_results.txt
The script generates a detailed log of the test results:

PASS: Page title is correct: 'Software Testing Consultancy & Training'
PASS: Link 'HOME' is visible on the page.
PASS: Link 'ABOUT' is visible on the page.
PASS: Link 'BLOG' is visible on the page.
PASS: Link 'CONTACT' is visible on the page.
PASS: Main heading 'Software Testing Services' is visible on the page.
🔧 Customizing the Script
URL: Change the url variable to test a different website.
Links to Check: Modify the links_to_check list for other navigation links.
Main Heading: Update the main_heading variable to validate a different heading.
🤔 Why Use This Script?
Device-Specific Testing: Simulates Pixel 5 mobile browsing without needing a physical device.
Quick Setup: Minimal configuration and easy integration into existing workflows.
Scalability: Expandable to include more tests and support additional devices.
📜 License
This project is licensed under the MIT License. You are free to use, modify, and share it.

📱 iOS Emulation Functional Test with Playwright
Welcome to the iOS Emulation Functional Test project! This script uses Playwright to emulate an iPhone environment, visit a website, and perform a basic functional test. The results of the test are saved in a user-friendly text file for easy reference.

🧪 What This Script Does
Simulates an iPhone 12 Environment:
Emulates device settings like viewport size, touch capabilities, and user agent.
Navigates to a Website:
Loads the specified URL (https://www.uol.com.br).
Performs Functional Testing:
Extracts the page title as a simple validation.
Saves Test Results:
Outputs the results into a text file named ios_emulation_results.txt.
🛠️ Tech Stack
Language: Python 3.12+
Framework: Playwright (Async API)
Device Simulation: Chromium browser with iOS emulation.
🚀 How to Run the Script
Prerequisites
Install Python 3.12+.
Install Playwright:
pip install playwright
Install Playwright's browser binaries:
playwright install
Steps to Run
Clone this repository or download the script file.
Save the script as ios_device_emulation.py.
Open a terminal and navigate to the script's directory.
Run the script:
python ios_device_emulation.py
View the test results in the file ios_emulation_results.txt generated in the same directory.
📝 Output Example
After running the script, the following results will be saved in ios_emulation_results.txt:

Website URL: https://www.uol.com.br
Page Title: UOL - O melhor conteúdo
🛡️ Why Use This Script?
Cross-Platform Testing: Simulates an iPhone environment without physical devices.
Easy Integration: Suitable for CI/CD pipelines or standalone testing.
Customizable: Modify the script for different devices or functional tests.
🤔 Need Help?
If you encounter issues or have questions, feel free to open an issue or contribute to the project!

📜 License
This project is licensed under the MIT License. Feel free to use, modify, and share it as needed.

Happy Testing! 🎉