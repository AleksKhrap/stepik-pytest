from selenium.webdriver.common.by import By
# import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestItems:
    def test_availability_of_the_order_button(self, browser):
        browser.get(link)
        # time.sleep(15)
        assert browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button[type='submit']")
