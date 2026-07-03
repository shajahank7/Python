from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            return webdriver.Chrome()
        elif browser == "firefox":
            return webdriver.Firefox()
        else:
            raise Exception(f"Browser '{browser}' not supported")