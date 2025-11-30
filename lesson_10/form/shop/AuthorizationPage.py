import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthorizationPage:

    """Класс для автоматизации тестирования страницы авторизации."""

    @allure.step("Инициализация страницы авторизации")
    def __init__(self, driver):
        with allure.step("Инициализация WebDriver"):
            self._driver = driver
        with allure.step("Установка ожидания"):
            self.wait = WebDriverWait(self._driver, 20)

    @allure.step("Открыть страницу авторизации")
    def open(self):
        """Открывает страницу авторизации и ожидает загрузки основных элементов."""

        with allure.step("Открытие страницы авторизации"):
            self._driver.get("https://www.saucedemo.com/")

        with allure.step("Ожидание загрузки поля для ввода имени пользователя"):
            self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#user-name")))
            return self

    @allure.step("Авторизовать пользователя с логином '{username}'")
    def login(self, username: str, password_text: str):
        """Выполняет процесс авторизации пользователя.
        Заполняет поля логина и пароля, затем нажимает кнопку входа."""

        with allure.step("Ввод имени пользователя"):
            user_name = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#user-name")))
            user_name.send_keys(username)

        with allure.step("Ввод пароля"):
            password = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#password")))
            password.send_keys(password_text)

        with allure.step("Нажатие кнопки входа"):

            with allure.step("Поиск кнопки 'Login'"):
                login_button = self.wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "#login-button")))
            with allure.step("Клик по кнопке 'Login'"):
                login_button.click()
