from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class DriverFactory:

    @staticmethod
    def get_driver(browser):

        if browser == "chrome":
            options = Options()
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")

            return webdriver.Chrome(options=options)

        elif browser == "firefox":
            options = FirefoxOptions()
            options.add_argument("--headless")
            return webdriver.Firefox(options=options)

        else:
            raise Exception(f"Browser '{browser}' not supported")