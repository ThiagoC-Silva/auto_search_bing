from time import sleep
from .settings import InitWebDriver
from .pages.home_bing import BingPages


def main():
    init_driver = InitWebDriver()
    browser_webdriver = init_driver.browser_webdriver

    bing = BingPages(browser_webdriver)
    bing.login_microsoft()

    sleep(600)
    init_driver.quit_driver()


if __name__ == "__main__":
    main()
