import time

from faker.generator import random
from selenium.webdriver.common.by import By

from utils.Actions import Actions
from utils.fakers import Faker, FakerUtils



class Employeepage(Actions):
        def __init__(self, driver):
            super().__init__(driver)
            self.driver = driver
            self.faker = FakerUtils()


        employee_button = (By.XPATH, "//p[text()='Employees']")
        add_employee_button = (By.XPATH, "//button[text()='Add Employee']")

        first_name = (By.NAME, "firstName")
        last_name = (By.NAME, "lastName")
        employee_id = (By.NAME, "id")
        personal_email = (By.NAME, "personalEmail")
        experience = (By.NAME, "pastExperience")
        email = (By.NAME, "email")
        role_dropdown = (By.NAME, "role")
        password = (By.NAME, "password")
        dob = (By.NAME, "dob")
        joining_date = (By.NAME, "joiningDate")
        qualification_dropdown = (By.NAME, "qualifications")
        department = (By.NAME, "department")
        gender_dropdown = (By.NAME, "gender")
        mobile_number = (By.NAME, "mobileNumber")
        blood_group_dropdown = (By.NAME, "bloodGroup")
        designation = (By.NAME, "designation")
        salary = (By.NAME, "salary")
        location = (By.NAME, "location")
        reporting_to_dropdown = (By.NAME, "reportingTo")
        Emp_idfield= (By.XPATH,"//input[@aria-label='EMP ID Filter Input']")

        add_button = (By.XPATH, "//button[text()='Add']")
        logout_button = (By.XPATH, "//p[text()='Logout']")
        table_cell =(By.XPATH,"//span[contains(@id,'cell-id')]")
        check_box = (By.XPATH,"//input[@aria-label='Press Space to toggle row selection (unchecked)']")


        def Add_Employee(self):
            emp_id = "1" + str(random.randint(10000, 99999))
            phone = "9" + str(random.randint(100000000, 999999999))

            self.click(self.employee_button)
            self.click(self.add_employee_button)

            self.send_keys(self.first_name, self.faker.get_first_name())
            self.send_keys(self.last_name, self.faker.get_last_name())
            emp_id=self.faker.get_random()
            self.send_keys(self.employee_id, emp_id)
            self.send_keys(self.email, self.faker.get_email())
            self.send_keys(self.personal_email, self.faker.get_email())
            self.send_keys(self.experience,"12")

            self.select_by_index(self.role_dropdown, 1)

            self.send_keys(self.password, self.faker.get_password())
            self.send_keys(self.dob, "07-12-2024")
            self.send_keys(self.joining_date, "05/06/2024")

            self.select_by_index(self.qualification_dropdown, 1)

            self.send_keys(self.department, self.faker.get_department_name())

            self.select_by_index(self.gender_dropdown, 1)

            self.send_keys(self.mobile_number, phone)
            self.select_by_index(self.blood_group_dropdown, 1)

            self.send_keys(self.designation, self.faker.get_department_name())
            self.send_keys(self.salary, "15420")
            self.send_keys(self.location, self.faker.get_location())

            self.select_by_index(self.reporting_to_dropdown, 1)
            self.click(self.add_button)
            time.sleep(5)
            self.send_keys(self.Emp_idfield, emp_id)
            time.sleep(5)
            self.assert_text_is_present(self.table_cell, str(emp_id))
            time.sleep(5)


