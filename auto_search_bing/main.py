from os import getenv
from time import sleep
from dotenv import load_dotenv
from settings import InitWebDriver

load_dotenv()


def main():
    init_driver = InitWebDriver()
    browser_webdriver = init_driver.browser_webdriver

    email_address = getenv("EMAIL_ADDRESS")
    password = getenv("PASSWORD")

    browser_webdriver.get("https://www.bing.com/?cc=br")
    sleep(5)

    init_driver.quit_driver()

if __name__ == '__main__':
    main()