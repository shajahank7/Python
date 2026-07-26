import pytest
from pages.ApplyleavePage import Applyleave
<<<<<<< HEAD

# @pytest.mark.usefixtures("login_setup")
=======
@pytest.mark.skip(reason="Temporarily disabled")
@pytest.mark.usefixtures("login_setup")
>>>>>>> 8c3529154b601fe88761b2196ea597ad24069bb8
@pytest.mark.order(1)
class TestApplyLeaveTest:
    def test_applyleave(self, driver):
        apply_leave = Applyleave(driver)
        apply_leave.Apply_Leave()
