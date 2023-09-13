import allure
from Pages.main_page import MainPage
from Utilities.additional_methods import get_total_sum_for_product
from Utilities.test_data import TestData
from conftest import *


@allure.description("Проверки для неавторизованного пользователя")
class TestGuestUser():
    @staticmethod
    @pytest.mark.parametrize('data_set', TestData.random_data_set(2))             # тест прогоняется 2 раза по рандомным товарам
    @allure.description("Выбор продукта, добавление его в корзину, проверка правильного отображения в корзине и на "
                        "странице покупки")
    def test_select_product(set_up_guest, data_set):
        main_page = MainPage(driver=set_up_guest)

        main_page.open_product_page(category_name=data_set["category"],
                                    sub_category_name=data_set["sub_category"])\
            .assert_category_name_is_correct(data_set["sub_category"])\
            .aplly_all_filters(price_low=data_set["price_low"],
                               price_high=data_set["price_high"],
                               additional_filters=data_set["additional_filters"])\
            .add_product_to_cart(product_id=data_set["product_id"])\
            .add_more_units_of_product(data_set["times"])\
            .assert_product_and_sum_in_modal_is_correct()\
            .go_to_cart_from_modal()\
            .assert_product_and_price_in_cart_is_correct()\
            .go_to_final_buy_page()\
            .assert_product_and_price_in_final_page_is_correct()

    @staticmethod
    @allure.description("Выбор 2 продуктов и добавление их в корзину, проверка правильного отображения в корзине")
    def test_select_two_products(set_up_guest, data_sets=TestData.random_data_set(2)):            # для теста берется 2 рандомных товара
        main_page = MainPage(driver=set_up_guest)

        products_details = {}

        for data_set in data_sets:                          # каждый товар из списка добавляется в корзину
            main_page.open_product_page(category_name=data_set["category"],
                                        sub_category_name=data_set["sub_category"])\
                .assert_category_name_is_correct(data_set["sub_category"])\
                .aplly_all_filters(price_low=data_set["price_low"],
                                   price_high=data_set["price_high"],
                                   additional_filters=data_set["additional_filters"])\
                .add_product_to_cart(product_id=data_set["product_id"])\
                .add_more_units_of_product(data_set["times"])\
                .assert_product_and_sum_in_modal_is_correct()\
                .close_modal_and_go_to_main_page()

            products_details[data_set["product_name"]] = get_total_sum_for_product(data_set["product_price"], data_set["times"])    # формируется словарь "имя продукта": "цена"

        main_page.enter_cart()\
            .assert_total_prices_for_all_products_are_correct(products_details)               # проверятся корректность отображения товаров в корзине,
                                                                                              # общая покупка продуктов невозможна, поэтому здесь тест заканчивается

    @staticmethod
    @pytest.mark.parametrize('data_set',  TestData.random_data_set(1))
    @allure.description("Поиск по наименованию продукта, проверка наличия на возвращаемой странице")
    def test_find_product_by_search(set_up_guest, data_set):
        main_page = MainPage(driver=set_up_guest)

        main_page.search_by_query(query=data_set["product_name"])\
                 .assert_product_is_present_on_the_page(product_id=data_set["product_id"],
                                                        expected_product_name=data_set["product_name"])
