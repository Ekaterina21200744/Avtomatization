
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthorizationPage:

    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 20)

    def open(self):
    
        self._driver.get("https://www.saucedemo.com/")
        
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name")))
        return self


    def login(self, username, password_text):

        user_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name")))
        user_name.send_keys(username)

        password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))
        password.send_keys(password_text)

        login_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#login-button")))
        login_button.click()

