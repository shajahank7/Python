import pytest
from Tools.scripts.mailerdaemon import emparse_list

from conftest import driver

from pages.Employeepage import  Employeepage
from utils import Actions

@pytest.mark.usefixtures("login_setup")
@pytest.mark.order(1)
class TestAddEmployee:
    def test_add_employee_setup(self, driver):
        Employee_page  = Employeepage(driver)
        Employee_page.Add_Employee()

