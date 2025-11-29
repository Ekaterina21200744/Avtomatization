import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Страница корзины")
@allure.feature("Корзина")
@allure.severity(allure.severity_level.BLOCKER)
class CartPage:

    """Класс для автоматизации тестирования страницы корзины."""

    @allure.title("Инициализация страницы корзины")
    @allure.description("Инициализирует страницу корзины и ожидает загрузки основных элементов")
    @allure.step("Инициализация страницы корзины")
    def __init__(self, driver):
        with allure.step("Инициализация WebDriver"):
            self._driver = driver
        with allure.step("Открытие страницы корзины"):
            self._driver.get("https://www.saucedemo.com/cart.html")
        with allure.step("Установка ожидания"):
            self.wait = WebDriverWait(self._driver, 20)

    @allure.title("Нажатие кнопки 'Checkout'")
    @allure.description("Нажимает кнопку 'Checkout' для оформления заказа.")
    @allure.feature("Корзина")
    @allure.step("Нажать кнопку 'Checkout'")
    def click_checkout(self):
        """Нажимает кнопку 'Checkout' для оформления заказа."""
        with allure.step("Поиск кнопки 'Checkout'"):
            checkout = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#checkout")))
        with allure.step("Клик по кнопке 'Checkout'"):
            checkout.click()
