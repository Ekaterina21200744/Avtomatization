
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class OrderPage:

  def __init__ (self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self.wait = WebDriverWait(self._driver, 20) 

  def fill_fields (self):
        first_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name")))
        first_name.send_keys("Иван")

        last_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#last-name")))
        last_name.send_keys("Иванов")

        zip_postal_code = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#postal-code")))
        zip_postal_code.send_keys("1234567")


  def continue_to_overview(self):
        but_continue = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#continue")))
        but_continue.click()
        
    
  def get_total_amount(self):
        total = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
        result = total.text 
        print(f"Итоговая сумма: {result}")
        return result
  
  