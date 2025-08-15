from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BrowserService
from selenium.webdriver.chrome.options import Options as BrowserOptions
from webdriver_manager.chrome import ChromeDriverManager

# Initialize and configure the Chrome WebDriver
class InitWebDriver:
    def __init__(self):
        options = BrowserOptions()
        # options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-images")
        options.add_argument("--disable-blink-features=AutomationControlled")

        service = BrowserService(ChromeDriverManager().install())

        self.browser_webdriver = webdriver.Chrome(service=service, options=options)

    def quit_driver(self):
        if self.browser_webdriver:
            self.browser_webdriver.quit()
