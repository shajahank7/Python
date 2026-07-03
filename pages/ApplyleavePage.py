from datetime import time
import time
from time import sleep

from selenium.webdriver.common.by import By

from utils.Actions import Actions


class Applyleave(Actions):

    leave_management = (By.XPATH, "//p[text()='Leave Management']")
    apply_leave_button = (By.XPATH, "//button[text()='Apply Leave']")

    from_date = (By.XPATH,"//input[@placeholder='From']")
    to_date = (By.XPATH, "//input[@placeholder='To']")

    subject_for_leave = (By.NAME, "subject")
    reason_for_leave = (By.NAME, "reason")

    wfh_checkbox = (By.ID, "workFromHome")
    submit_button = (By.XPATH, "//button[text()='Submit']")

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def Apply_Leave(self):

        self.click(self.leave_management)
        self.click(self.apply_leave_button)
        self.click(self.from_date)
        self.send_keys(self.from_date, "08-05-2026")
        self.esc()
        time.sleep(2)
        self.click(self.subject_for_leave)
        self.send_keys(self.subject_for_leave, "subject leave")
        self.send_keys(self.reason_for_leave, "leave health problem")
        time.sleep(2)
        self.send_keys(self.to_date, "09-05-2026")
        self.click(self.to_date)

        time.sleep(1)
        time,sleep(2)
        self.click(self.wfh_checkbox)
