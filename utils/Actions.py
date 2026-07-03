from lib2to3.pgen2 import driver
from telnetlib import EC

from _pytest import assertion
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Actions:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # 🔹 Wait + Click (stable)
    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise Exception(f"❌ Element not clickable: {locator}")

    def esc(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def send_keys(self,locator,text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.send_keys(text)
        except TimeoutException:
            raise Exception(f"❌ Element not visible: {locator}")

    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def assert_element_visiable(self, locator):
        try:
            element = self.wait_until_visible(locator)
            assert element.is_displayed()
        except TimeoutException:
            raise AssertionError(f"❌ Element not found in time: {locator}")

    def assert_text_is_present(self, locator, expected_text):
        try:
            element = self.wait_until_visible(locator)
            actual_text = element.text.strip()

            # ✅ Fix 1 — handle multiline text like "0\n1"
            actual_text = actual_text.split("\n")[-1].strip()

            # ✅ Fix 2 — convert both to string before comparing
            assert str(expected_text) == str(actual_text), \
                f"Text mismatch for {locator}: Expected='{expected_text}' Actual='{actual_text}'"

        except AssertionError:
            raise
        except TimeoutException:
            raise AssertionError(f"Element not visible for text check: {locator}")

    def select_by_index(self, locator, index):
        dropdown = self.driver.find_element(*locator)
        select = Select(dropdown)
        select.select_by_index(index)

