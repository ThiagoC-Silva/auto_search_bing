from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def wait_clickable_element(driver, by, value, timeout=10):
    element = WebDriverWait(driver, timeout)
    element = element.until(expected_conditions.element_to_be_clickable((by, value)))
    return element


def wait_visible_element(driver, by, value, timeout=10):
    element = WebDriverWait(driver, timeout)
    element = element.until(
        expected_conditions.visibility_of_element_located((by, value))
    )
    return element
