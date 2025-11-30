import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Магазин")
class MainPageShop:

    """Класс для автоматизации тестирования главной страницы магазина."""

    @allure.step("Инициализация главной страницы магазина")
    def __init__(self, driver):
        """Инициализирует главную страницу магазина и ожидает загрузки основных элементов."""
        with allure.step("Инициализация WebDriver"):
            self._driver = driver
        with allure.step("Открытие главной страницы магазина"):
            self._driver.get("https://www.saucedemo.com/inventory.html")
        with allure.step("Установка ожидания"):
            self.wait = WebDriverWait(self._driver, 20)

    @allure.step("Добавить продукты в корзину")
    def add_products_to_cart(self):
        """Добавляет три продукта в корзину."""
        with allure.step("Добавление продуктов в корзину"):
            products = [
                ("#add-to-cart-sauce-labs-backpack", "Sauce Labs Backpack"),
                ("#add-to-cart-sauce-labs-bolt-t-shirt", "Sauce Labs Bolt T-Shirt"),
                ("#add-to-cart-sauce-labs-onesie", "Sauce Labs Onesie")
            ]

        with allure.step("Клик по кнопкам добавления продуктов в корзину"):
            for selector, product_name in products:
                product = self.wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, selector)))
                product.click()
        with allure.step("Возврат к главной странице магазина"):
            return MainPageShop(self._driver)

    @allure.step("Переход в корзину")
    def get_cart(self):
        """Переходит в корзину после добавления продуктов."""

        with allure.step("Поиск и клик по иконке корзины"):
            cart = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".shopping_cart_badge")))
        with allure.step("Переход в корзину"):
            cart.click()
