from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calc():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        
        wait = WebDriverWait(driver, 20)
        
        delay = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay.clear()
        delay.send_keys("45")
        

        buttons_to_click = ["7", "+", "8", "="]
        
        for button_text in buttons_to_click:
            button = driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
            button.click()
        

        long_wait = WebDriverWait(driver, 47)
        long_wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        
        result= driver.find_element(By.CSS_SELECTOR, ".screen")
        actual_result = result.text
        
        assert actual_result == "15", f"Ожидалось '15', получено '{actual_result}'"
        print("Тест пройден.")
        
    finally:
        driver.quit()

# Запуск теста
if __name__ == "__main__":
    test_calc()


