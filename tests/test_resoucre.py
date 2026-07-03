import pytest
from pygments.lexers import resource

from pages.ResourceTrackingPage import ResourceTrackingPage

@pytest.mark.usefixtures("login_setup")
@pytest.mark.order(3)
class TestResoucre:
    def test_resoucre(self, driver):
        resource_page = ResourceTrackingPage(driver)
        resource_page.Verify_resource_tracking_fill()
