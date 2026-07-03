import time
from selenium.webdriver.common.by import By

from utils.fakers import Faker, FakerUtils

from utils.Actions import Actions


class ResourceTrackingPage(Actions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.faker = FakerUtils()

    ResourceTracking= (By.XPATH,"//p[text()='Resource Tracking' and contains(@class, 'mt-4')]/parent::li")
    ResouceTab = (By.XPATH,"//button[text()='Resources' and contains(@class, 'btn-tabs')]")
    AddResourceButton =(By.XPATH,"//button[text()='Add Resource']")
    Allocated_Date = (By.NAME,"allocatedDate")
    Device_type = (By.NAME,"deviceType")
    SerialId = (By.NAME,"serialId")
    model = (By.NAME,"model")
    submit = (By.XPATH,"//button[text()='Submit']")

    def Verify_resource_tracking_fill(self):
        time.sleep(5)
        self.assert_element_visiable(self.ResourceTracking)
        self.click(self.ResourceTracking)
        self.click(self.ResouceTab)
        self.click(self.AddResourceButton)
        self.send_keys(self.Allocated_Date, "2026/5/12")
        self.select_by_index(self.Device_type, 1)
        self.send_keys(self.SerialId, self.faker.get_serial_number())
        self.send_keys(self.model, self.faker.get_model())
        self.click(self.submit)
