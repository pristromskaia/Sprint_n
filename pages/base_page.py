from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    TimeoutException,
)
from utils.waiters import TIMEOUT

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout)

    def wait_until(self, condition, timeout=TIMEOUT):
        return self.wait(timeout).until(condition)

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def open_url(self, url):
        self.driver.get(url)

    def find_visible(self, locator, timeout=TIMEOUT):
        return self.wait_until(
            EC.visibility_of_element_located(locator),
            timeout
        )

    def find_clickable(self, locator, timeout=TIMEOUT):
        return self.wait_until(
            EC.element_to_be_clickable(locator),
            timeout
        )

    def find_all(self, locator, timeout=TIMEOUT):
        return self.wait_until(
            EC.presence_of_all_elements_located(locator),
            timeout
        )

    def find_all_visible(self, locator, timeout=TIMEOUT):
        return self.wait_until(
            EC.visibility_of_all_elements_located(locator),
            timeout
        )

    def wait_presence(self, locator, timeout=TIMEOUT):
        return self.wait_until(
            EC.presence_of_element_located(locator),
            timeout
        )

    def wait_all_present(self, locator, timeout=TIMEOUT):
        return self.wait_until(
            EC.presence_of_all_elements_located(locator),
            timeout
        )

    def wait_visibility(self, locator, timeout=TIMEOUT):
        return self.find_visible(locator, timeout)

    def wait_text_in_element(self, locator, text, timeout=TIMEOUT):
        return self.wait_until(
            EC.text_to_be_present_in_element(locator, text),
            timeout
        )

    def wait_for_page_load(self, timeout=TIMEOUT):
        return self.wait_until(
            lambda d: d.execute_script("return document.readyState") == "complete",
            timeout
        )

    def get_text(self, locator, timeout=TIMEOUT):
        return self.find_visible(locator, timeout).text

    def click(self, locator, timeout=TIMEOUT):
        element = self.find_clickable(locator, timeout)
        element.click()

    def js_click(self, element):
        self.execute_script("arguments[0].click();", element)

    def click_js(self, locator, timeout=TIMEOUT):
        element = self.find_clickable(locator, timeout)
        self.js_click(element)

    def click_element_js(self, element):
        self.js_click(element)

    def safe_click(self, element):
        try:
            element.click()
            return True
        except (
            ElementClickInterceptedException,
            StaleElementReferenceException,
            ElementNotInteractableException,
        ):
            return False

    def scroll_to_element(self, element):
        self.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

    def scroll_to_element_center(self, element):
        self.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            element
        )

    def hover(self, element):
        self.scroll_to_element_center(element)
        ActionChains(self.driver).move_to_element_with_offset(element, 1, 2).perform()

    def is_visible(self, locator, timeout=TIMEOUT):
        try:
            self.find_visible(locator, timeout)
            return True
        except TimeoutException:
            return False