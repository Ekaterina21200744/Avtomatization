import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Корзина")
class CartPage:

    """Класс для автоматизации тестирования страницы корзины."""

    @allure.step("Инициализация страницы корзины")
    def __init__(self, driver):
        with allure.step("Инициализация WebDriver"):
            self._driver = driver
        with allure.step("Открытие страницы корзины"):
            self._driver.get("https://www.saucedemo.com/cart.html")
        with allure.step("Установка ожидания"):
            self.wait = WebDriverWait(self._driver, 20)

    @allure.step("Нажать кнопку 'Checkout'")
    def click_checkout(self):
        """Нажимает кнопку 'Checkout' для оформления заказа."""
        with allure.step("Поиск кнопки 'Checkout'"):
            checkout = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#checkout")))
        with allure.step("Клик по кнопке 'Checkout'"):
            checkout.click()
