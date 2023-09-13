from selenium.common import NoSuchElementException, NoSuchFrameException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:
    def __init__(self, driver):
        self.driver = driver

    # locators
    close_region_confirmation_button = '//*[@class="js-cr-close cr-close"]'
    close_alert_button = "//*[@data-fl-close='1800']"

    # getters
    def get_close_alert_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.close_alert_button)))

    def get_close_region_confirmation_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.close_region_confirmation_button)))
        # return self.driver.find_element(By.XPATH, self.close_region_confirmation_button)

    # methods
    def click_close_region_confirmation_button(self):
        try:
            self.get_close_region_confirmation_button().click()
        except NoSuchElementException:
            pass

    def click_close_alert_button(self):
        """Нажатие на кнопку закрытия поп-апа, всплывающего периодически"""
        try:
            WebDriverWait(self.driver, 6).until(EC.frame_to_be_available_and_switch_to_it("fl-714756"))
            self.get_close_alert_button().click()
            self.driver.switch_to.parent_frame()
        except TimeoutException:
            pass

    # asserts
    @staticmethod
    def assert_product_is_present(elements, product_name):
        element = list(filter(lambda x: x.text == product_name, elements))
        assert len(element) == 1, "No such product is found"

    @staticmethod
    def assert_element_name_is_correct(element, expected_result):
        actual_result = element.text
        assert expected_result == actual_result, "There is no element with such text"


