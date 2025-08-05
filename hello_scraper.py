#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # 1. Set up ChromeDriver (auto-downloads the right binary)
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # (Optional) comment out the next line if you *do* want to see the browser window
    # options.add_argument("--headless")

    driver = webdriver.Chrome(service=service, options=options)

    # 2. Navigate to a test URL
    test_url = "https://www.google.com"
    driver.get(test_url)

    # 3. Wait a little so you can see the window open (or let it fully load)
    time.sleep(5)

    # 4. Confirm in logs
    print(f"✅ Browser opened and navigated to {test_url}")

    # 5. Clean up
    driver.quit()

if __name__ == "__main__":
    main()
