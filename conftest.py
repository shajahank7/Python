import pytest
import time

from driver_factory import DriverFactory
from config_reader import ConfigReader
from pages.Loginpage import Loginpage


# ---------------- DRIVER FIXTURE ----------------
@pytest.fixture(scope="class")
def driver():

    driver = DriverFactory.get_driver(ConfigReader.get_browser())
    driver.maximize_window()

    yield driver   # 👉 test runs here

    driver.quit()  # 👉 teardown


# ---------------- LOGIN FIXTURE ----------------
@pytest.fixture(scope="class")
def login_setup(driver):

    driver.get(ConfigReader.get_url())

    login = Loginpage(driver)
    login.Verify_Login(
        ConfigReader.get_username(),
        ConfigReader.get_password()
    )

    # yield driver   # 👉 tests run here

    # OPTIONAL TEARDOWN
    # login.Verify_Logout()


import allure

def after_scenario(context, scenario):

    if scenario.status == "failed":

        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )