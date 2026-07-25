import pytest
from pages.ApplyleavePage import Applyleave
@pytest.mark.skip(reason="Temporarily disabled")
@pytest.mark.usefixtures("login_setup")
@pytest.mark.order(1)
class TestApplyLeaveTest:
    def test_applyleave(self, driver):
        apply_leave = Applyleave(driver)
        apply_leave.Apply_Leave()
