import time
import pytest
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
def test_add_to_basket_button(browser):
    browser.get(link)
    # time.sleep(30)

    try:
        browser.find_element_by_css_selector(".btn-add-to-basket")
        res = True
    except NoSuchElementException:
        res = False
                
    assert res, "Button is not found"
