#!/usr/bin/env python3
import time
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    # 1. Set up ChromeDriver
    service = Service(ChromeDriverManager().install())

    # 2. Create a unique temp directory for Chrome’s user-data
    profile_dir = tempfile.mkdtemp(prefix="chrome-profile-")

    # 3. Configure ChromeOptions
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"--user-data-dir={profile_dir}")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=service, options=options)
    try:
        # 4. Navigate and pause
        test_url = "https://example.com"
        driver.get(test_url)
        time.sleep(3)
        print(f"✅ Browser opened and navigated to {test_url}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
