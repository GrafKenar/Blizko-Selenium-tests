from Base.BaseClass import BaseClass
from Pages.CartPage import CartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Settings import Settings
from Utilities.AdditionalMethods import get_total_sum_for_product


class AddedToCartModal(BaseClass):
    """Класс, описывающий модал, который открывается после нажатия кнопки добавления продукта в корзину"""
    def __init__(self, driver, product_price, product_name):
        super().__init__(driver)
        self.product_price = product_price
        self.product_name = product_name
        self.driver = driver
        self.final_price = ''

    # Locators
    add_more_product_button = "//*[@class='ui-icon ui-icon-triangle-1-n']"
    go_to_cart_button = "//*[contains(text(), 'Перейти к оформлению')]"
    product_name_in_modal = "//*[@class='orders-item-description-container']/p"
    product_total_price = "//*[@class='orders-item-total js-orders-item-total']"
    close_modal_button = "//*[contains(text(), 'Вернуться к покупкам')]"

    # getters
    def get_add_more_product_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_more_product_button)))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button)))

    def get_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_name_in_modal)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_total_price)))

    def get_close_modal_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.close_modal_button)))

    # actions
    def click_add_more_product_button(self):
        self.get_add_more_product_button().click()

    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()

    def click_close_modal_button(self):
        self.get_close_modal_button().click()

    # methods
    def count_final_price(self, times):
        """Цена товара умножается на его количество и преобразуется в значение, которое будет сравниваться"""
        price = float(self.product_price.replace(' ', ''))
        self.final_price = get_total_sum_for_product(price, times)
        print(f"Итогая стоимость выбранного количества товара - {self.final_price}")

    def add_more_units_of_product(self, times):
        """Добавление дополнительных единиц товара times раз"""
        for _time in range(times):
            self.click_add_more_product_button()
        print(f"Добавлено дополнительно еще {times} единиц товара")
        self.count_final_price(times)
        return self

    def go_to_cart_from_modal(self):
        """Переход из промежуточного модала в корзину"""
        self.click_go_to_cart_button()
        cp = CartPage(self.driver, product_price=self.final_price, product_name=self.product_name)
        print("Переход в корзину")
        return cp

    def wait_until_correct_price_is_displayed(self):
        """Ожидание правильного отображения итоговой суммы"""
        try:
            WebDriverWait(self.driver, 4).until(EC.text_to_be_present_in_element(locator=(By.XPATH, self.product_total_price), text_=self.final_price))
        except:
            exception = Exception("PriceIsWrong")
            raise exception

    def close_modal_and_go_to_main_page(self):
        """Закрытие модала и возвращение на главную страницу"""
        self.click_close_modal_button()
        self.driver.get(Settings.base_url)

    # asserts
    def assert_product_and_sum_in_modal_is_correct(self):
        """Проверка правильности товара и корректной стоимости выбранного количества единиц товара"""
        assert self.product_name == self.get_product_name().text
        self.wait_until_correct_price_is_displayed()
        print("Наименование товара и стоимость отображаются корректно в промежуточном модале")
        return self

