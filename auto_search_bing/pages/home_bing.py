from os import getenv
from dotenv import load_dotenv
from auto_search_bing.utils.wait_for_element import (
    wait_clickable_element,
    wait_visible_element,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, InvalidSessionIdException

load_dotenv()


class BingPages:
    def __init__(self, web_driver):
        self.web_driver = web_driver
        self.url = "https://login.live.com"
        # Elements from page
        self.email_input_id = "usernameEntry"
        self.password_input_id = "passwordEntry"
        self.close_button_id = "close-button"
        # Credentials
        self.email_address = getenv("EMAIL_ADDRESS")
        self.password = getenv("PASSWORD")

    def login_microsoft(self):
        try:
            # Open the Bing login page
            self.web_driver.get(self.url)

            email_input_field = wait_visible_element(
                self.web_driver, By.ID, self.email_input_id
            )
            email_input_field.send_keys(self.email_address)
            email_input_field.send_keys(Keys.ENTER)

            entry_form = wait_clickable_element(
                self.web_driver, By.XPATH, self.entry_form_xpath
            )
            entry_form.click()

            password_input_field = wait_visible_element(
                self.web_driver, By.ID, self.password_input_id
            )
            password_input_field.send_keys(self.password)
            password_input_field.send_keys(Keys.ENTER)

            close_button = wait_clickable_element(
                self.web_driver, By.ID, self.close_button_id
            )
            close_button.click()

        except TimeoutException:
            print("Error during waiting for elements.")
        except InvalidSessionIdException:
            print(
                "The browser crashed, closed, or the connection between the script and the browser was interrupted for some reason."
            )
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
