from symtable import Class

import pytest

from config_reader import ConfigReader
from pages.Loginpage import Loginpage

class TestLogin:

    def test_valid_login(self, driver):

        # 🔹 Open URL from config
        driver.get(ConfigReader.get_url())

        # 🔹 Create page object
        login = Loginpage(driver)

        # 🔹 Perform login using config data

        login.Verify_Login(
            ConfigReader.get_username(),
            ConfigReader.get_password()
        )


