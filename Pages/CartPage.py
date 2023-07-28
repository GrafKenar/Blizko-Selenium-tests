from Base.BaseClass import BaseClass
from Pages.FinalBuyPage import FinalBuyPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BaseClass):
    """Класс, описывающий страницу корзины"""
    def __init__(self, driver, product_price='', product_name=''):
        super().__init__(driver)
        self.product_price = product_price
        self.product_name = product_name
        self.driver = driver

    # locators
    go_to_buy_page_button = "//*[contains(text(), 'Перейти к оформлению')]"
    cart_page_product_price = "//p[@class='orders-item__total js-orders-item__total']"
    cart_page_product_name = "//a[@class='orders-item__title']"
    all_delete_product_buttons = "//button[@title = 'Удалить из корзины']"
    cart_product_total_sum = "//*[contains(text(), 'product_name')]//..//..//..//..//..//..//..//" \
                             "p[contains(@class, 'orders-cart-amount__total-value js-orders-cart-item__total')]"  # сложный составной xpath для поиска суммы по названию продукта

    # getters
    def get_go_to_buy_page_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.go_to_buy_page_button)))

    def get_cart_page_product_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_page_product_price)))

    def get_cart_page_product_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_page_product_name)))

    def get_all_delete_product_buttons(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.all_delete_product_buttons)))

    def get_cart_product_total_sum(self, product_name):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_product_total_sum.replace("product_name", product_name))))

    # actions
    def click_go_to_buy_page_button(self):
        self.get_go_to_buy_page_button().click()

    def click_all_delete_product_buttons(self):
        for button in self.get_all_delete_product_buttons():
            button.click()

    # methods
    def go_to_final_buy_page(self):
        """Переход на страницу оформления заказа"""
        self.click_go_to_buy_page_button()
        print("Переход на страницу оформления заказа")
        fbp = FinalBuyPage(self.driver, product_price=self.product_price, product_name=self.product_name)
        return fbp

    def clean_up_all_added_products(self):
        """Удаление всех продуктов, которые есть в корзине"""
        self.click_all_delete_product_buttons()
        print("\nВсе товары удалены из корзины")

    # asserts
    def assert_product_and_price_in_cart_is_correct(self):
        """Проверка правильности товара и корректной стоимости выбранного количества единиц товара"""
        assert self.product_price == self.get_cart_page_product_price().text
        assert self.product_name == self.get_cart_page_product_name().text
        print("Товар и его стоимость отображаются в корзине корректно")
        return self

    def assert_total_prices_for_all_products_are_correct(self, product_details):
        """Проверка правильности итоговыъ сумм для всех продуктов в корзине"""
        for product in product_details:
            assert self.get_cart_product_total_sum(product).text == product_details[product]
            print(f"\nИнформация для продукта {product} отображается верно")

