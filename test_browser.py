#!/usr/bin/env python3
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # 1. Set up ChromeDriver (auto-downloads the right binary)
    service = Service(ChromeDriverManager().install())

    # 2. Configure ChromeOptions with CI-friendly flags
    options = webdriver.ChromeOptions()
    # Run headless in CI
    options.add_argument("--headless=new")
    # These ensure Chrome can run in GitHub's container environment
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Give it its own temp profile
    options.add_argument(f"--user-data-dir={os.getcwd()}/.chrome_user_data")
    # (Optional) disable GPU acceleration
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=service, options=options)

    try:
        # 3. Navigate to a test URL
        test_url = "https://example.com"
        driver.get(test_url)

        # 4. Wait a bit so the page fully loads
        time.sleep(3)

        # 5. Confirm in logs
        print(f"✅ Browser opened and navigated to {test_url}")
    finally:
        # 6. Clean up
        driver.quit()

if __name__ == "__main__":
    main()
