import random
import string

from faker import Faker
from selenium.webdriver.support.select import Select

fake = Faker()


class FakerUtils:

    @staticmethod
    def get_first_name():
        return fake.first_name()

    @staticmethod
    def get_last_name():
        return fake.last_name()

    @staticmethod
    def get_full_name():
        return fake.name()

    def get_random(self):
        return fake.random_number(digits=6)

    def get_email(self):
        return fake.email()

    def get_password(self):
        return fake.password()
    def get_date_of_birth(self):
        return fake.date_of_birth()

    def get_department_name(self):
        departments = [
            "Human Resources",
            "Finance",
            "Marketing",
            "Sales",
            "Engineering",
            "IT Support",
            "Operations",
            "Customer Service",
            "Research and Development",
            "Legal",
            "Procurement",
            "Administration"
        ]
        return random.choice(departments)

    def get_salary(self):
        return fake.salary()

    def get_model(self):
        brands = ["Dell", "HP", "Lenovo", "Asus", "Acer"]
        series = ["Pro", "Elite", "Think", "Ultra", "Book"]

        return f"{random.choice(brands)}-{random.choice(series)}-{random.randint(100, 999)}"

    def get_serial_number(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
    def get_location(self):
        return fake.city()

