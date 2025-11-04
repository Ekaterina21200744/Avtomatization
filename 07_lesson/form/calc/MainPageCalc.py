from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPageCalc:

    def __init__(self,driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        self.wait = WebDriverWait(self._driver, 20)

    def set_delay(self, delay_value = "45"):
        delay_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def clicK_button (self):
        buttons_to_click = ["7", "+", "8", "="]
        
        for button_text in buttons_to_click:
            button = self._driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
            button.click()

    def get_result (self):
        long_wait = WebDriverWait(self._driver, 47)
        long_wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        
        result = self._driver.find_element(By.CSS_SELECTOR, ".screen")
        actual_result = result.text
        return actual_result
    
    def check_result(self, expected_result="15"):
        actual_result = self.get_result()
        assert actual_result == expected_result, f"Ожидалось '{expected_result}', получено '{actual_result}'"

    def close_browser(self):
        self._driver.quit()
        

    




    


