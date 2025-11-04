from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__ (self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/cart.html")
        self.wait = WebDriverWait(self._driver, 20)

    def click_checkout (self):
        checkout = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#checkout")))
        checkout.click()