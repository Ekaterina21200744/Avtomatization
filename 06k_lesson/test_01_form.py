from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():
    
    edge_driver_path = r"c:\Users\gavri\Desktop\edge\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    
    try:
    
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        wait = WebDriverWait(driver, 20)
    
        first_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='first-name']")))
        first_name.send_keys("Иван")
        
        last_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='last-name']")))
        last_name.send_keys("Петров")
        
        address = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='address']")))
        address.send_keys("Ленина, 55-3")
        
        email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='e-mail']")))
        email.send_keys("test@skypro.com")
      
        phone_number = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='phone']")))
        phone_number.send_keys("+7985899998787")
       
        zip_code = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='zip-code']")))
        zip_code.clear()
        
        city = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='city']")))
        city.send_keys("Москва")
        
        country = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='country']")))
        country.send_keys("Россия")
        
        job_position = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='job-position']")))
        job_position.send_keys("QA")
        
        company = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='company']")))
        company.send_keys("SkyPro")
        
       
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn")))
        button.click()
    

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code")))
        
        zip_code_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")
        zip_code_field_color = zip_code_field.value_of_css_property("background-color")
        print(f"Цвет фона ZIP-кода: {zip_code_field_color}")
        
        expected_red_color = "rgba(248, 215, 218, 1)"
        assert expected_red_color in zip_code_field_color, f"Поле ZIP-кода не подсвечено красным. Получен цвет: {zip_code_field_color}"

        green_fields = [
            "first-name", "last-name", "address", "e-mail", "phone",
            "city", "country", "job-position", "company"]
        
        for field_name in green_fields:
            field = driver.find_element(By.CSS_SELECTOR, f"#{field_name}")
            field_color = field.value_of_css_property("background-color")
            expected_green_color = "rgba(209, 231, 221, 1)" 
            
            assert expected_green_color in field_color, f"Поле {field_name} не подсвечено зеленым. Получен цвет: {field_color}"
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_form()