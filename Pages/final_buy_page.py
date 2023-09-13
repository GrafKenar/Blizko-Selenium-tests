import allure

from Base.base_class import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FinalBuyPage(BaseClass):
    """Класс, описывающий страницу оформления покупки товара"""
    def __init__(self, driver, product_price, product_name):
        super().__init__(driver)
        self.product_price = product_price
        self.product_name = product_name
        self.driver = driver

    # locators
    total_sum_on_final_page = "//*[@class='order-total__sum']"
    product_name_on_final_page = "//*[@class='item__name']"

    # getters
    def get_total_sum(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.total_sum_on_final_page)))

    def get_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_name_on_final_page)))

    # methods
    @allure.step("Проверка правильности товара и корректной стоимости выбранного количества единиц товара")
    def assert_product_and_price_in_final_page_is_correct(self):
        assert self.product_price == self.get_total_sum().text
        assert self.product_name == self.get_product_name().text
        print("Товар и его стоимость отображаются на странице оформления заказа корректно")
        return self

    @allure.step("Проверка правильности товара и корректной стоимости выбранного количества единиц товара")
    def assert_total_price_in_final_page_is_correct(self, total_price):
        assert total_price == self.get_total_sum().text
        return self
