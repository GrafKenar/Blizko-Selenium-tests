import datetime
import os
import pytest
from selenium import webdriver

from Base.BaseClass import BaseClass
from Pages.MainPage import MainPage
from Utilities.AdditionalMethods import get_screenshot
from Utilities.Settings import Settings
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def set_up_logged():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    driver.get(Settings.base_url)

    mpg = MainPage(driver)
    mpg.enter_login_modal()\
       .log_in_application(Settings.test_email, Settings.test_password)  # логин в систему с данными тестового пользователя

    bc = BaseClass(driver)
    bc.click_close_alert_button()
    bc.click_close_region_confirmation_button()

    yield driver

    get_screenshot(driver)                # делаем скриншот на случай, если тест упал

    driver.get(Settings.base_url)
    if mpg.read_number_of_products_in_cart() != '':       # проверка на наличие продуктов в корзине, оставшихся после прогона тестов
        mpg.enter_cart()\
           .clean_up_all_added_products()         # удаление продуктов в корзине

    driver.close()

@pytest.fixture()
def set_up_guest():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Settings.base_url)

    bc = BaseClass(driver)
    # bc.click_close_alert_button()
    bc.click_close_region_confirmation_button()

    yield driver

    get_screenshot(driver)                # делаем скриншот на случай, если тест упал
    driver.close()


@pytest.fixture(scope='session', autouse=True)
def teardown_session():
    """Зачистка устаревших скриншотов"""
    for filename in os.listdir(Settings.screenshot_folder):
        file_creation_date = os.path.getmtime(Settings.screenshot_folder+filename)
        file_creation_date_formatted = datetime.date.fromtimestamp(file_creation_date)
        if file_creation_date_formatted < datetime.date.today():
            os.remove(Settings.screenshot_folder+filename)
