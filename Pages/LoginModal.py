from Base.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginModal(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    email_field = "//input[@name='phone']"
    password_field = "//input[@name='password' and not(@disabled)]"
    enter_button = "//div[contains(text(), 'Войти')]"

    # getters
    def get_email_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    # actions
    def enter_email(self, email):
        self.get_email_field().send_keys(email)

    def enter_password(self, password):
        self.get_password_field().send_keys(password)

    def click_enter_button(self):
        self.get_enter_button().click()

    # methods
    def log_in_application(self, email, password):
        """Ввод логина и пароля в модале авторизации"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_enter_button()
        print(f"\nАвторизация тестового пользователя {email} осуществлена")