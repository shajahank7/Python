
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from utils.Actions import Actions

class Loginpage(Actions):

    user_name = (By.ID, "userEmail")
    password = (By.ID, "userPassword")
    login_button = (By.XPATH,"//button[text()='Login']")
    dashboard = (By.XPATH,"//p[contains(@class,'sc-feUZmu')]")
    Logout_button = (By.XPATH,"//p[text()='Logout']")
    yes_button = (By.XPATH,"//button[text()='Yes']")


    def Verify_Login(self,name,pwd):
        self.send_keys(self.user_name,name)
        self.send_keys(self.password,pwd)
        self.click(self.login_button)

    def Verify_Logout(self):
        self.assert_element_visiable(self.dashboard)
        self.click(self.Logout_button)
        self.click(self.yes_button)
