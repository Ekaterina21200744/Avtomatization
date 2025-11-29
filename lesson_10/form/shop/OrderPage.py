import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from AuthorizationPage import AuthorizationPage
from MainPageShop import MainPageShop
from CartPage import CartPage


@allure.title("Страница оформления заказа")
@allure.feature("Оформление заказа")
class OrderPage:

    """Класс для автоматизации тестирования страницы оформления заказа."""

    @allure.title("Инициализация страницы оформления заказа")
    @allure.description(
        "Инициализирует страницу оформления заказа и ожидает загрузки основных элементов")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("Инициализация страницы оформления заказа")
    def __init__(self, driver):
        """Инициализирует страницу оформления заказа и ожидает загрузки основных элементов."""
        with allure.step("Инициализация WebDriver"):
            self._driver = driver
        with allure.step("Открытие страницы оформления заказа"):
            self._driver.get(
                "https://www.saucedemo.com/checkout-step-one.html")
        with allure.step("Установка ожидания"):
            self.wait = WebDriverWait(self._driver, 20)

    @allure.title("Заполнение полей для оформления заказа")
    @allure.description("Заполняет поля для оформления заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("Заполнение полей для оформления заказа")
    def fill_fields(self):
        """Заполняет поля 'First Name', 'Last Name', 'Zip/Postal Code' для оформления заказа."""

        with allure.step("Заполнение поля 'First Name'"):
            first_name = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#first-name")))
            first_name.send_keys("Иван")

        with allure.step("Заполнение поля 'Last Name'"):
            last_name = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#last-name")))
            last_name.send_keys("Иванов")

        with allure.step("Заполнение поля 'Zip/Postal Code'"):
            zip_postal_code = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#postal-code")))
            zip_postal_code.send_keys("1234567")

    @allure.title("Переход к обзору заказа")
    @allure.description("Нажимает кнопку 'Continue' для перехода к обзору заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("Нажать кнопку 'Continue' для перехода к обзору заказа")
    def continue_to_overview(self):
        """Нажимает кнопку 'Continue' для перехода к обзору заказа."""
        with allure.step("Поиск кнопки 'Continue'"):
            but_continue = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#continue")))
        with allure.step("Клик по кнопке 'Continue'"):
            but_continue.click()

    @allure.title("Получение итоговой суммы заказа")
    @allure.description("Получает и возвращает итоговую сумму заказа на странице обзора заказа")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self) -> str:
        """Получает и возвращает итоговую сумму заказа на странице обзора заказа."""

        with allure.step("Поиск элемента с итоговой суммой заказа {total}"):
            total = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".summary_total_label")))
        with allure.step("Извлечение и возврат текста с итоговой суммой заказа {result}"):
            result = total.text
            print(f"Итоговая сумма: {result}")
            return result
