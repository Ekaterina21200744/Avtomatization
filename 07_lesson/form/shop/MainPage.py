from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/inventory.html")
        self.wait = WebDriverWait(self._driver, 20)

    def add_products_to_cart(self):
    
        products = [
            ("#add-to-cart-sauce-labs-backpack", "Sauce Labs Backpack"),
            ("#add-to-cart-sauce-labs-bolt-t-shirt", "Sauce Labs Bolt T-Shirt"), 
            ("#add-to-cart-sauce-labs-onesie", "Sauce Labs Onesie")
        ]
    
        for selector, product_name in products:
            product = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
            product.click()

        return MainPage(self._driver)

    def get_cart(self):
         cart = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge")))
         cart.click()

   
         
        
