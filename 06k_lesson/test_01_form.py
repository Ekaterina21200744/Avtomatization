from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_driver_path = r"c:\Users\gavri\Desktop\edge\msedgedriver.exe"

driver = webdriver.Edge(service=EdgeService(edge_driver_path))

driver.get ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

wait = WebDriverWait(driver, 20)

first_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='first-name']"))).send_keys("Иван")

last_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='last-name']"))).send_keys("Петров")

adress = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='address']"))).send_keys("Ленина, 55-3")

email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='e-mail']"))).send_keys("test@skypro.com")

phone_number = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='phone']"))).send_keys("+7985899998787")

zip_code = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='zip-code']")))
zip_code.clear()

city = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='city']"))).send_keys("Москва")

country = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='country']"))).send_keys("Россия")

job_position = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='job-position']"))).send_keys("QA")

company = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='company']"))).send_keys("SkyPro")


button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn")))
button.click()

zip_code_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code")))
zip_code_field_color = zip_code_field.value_of_css_property("background-color")
print(zip_code_field_color)

assert zip_code_field_color == "rgba(248, 215, 218, 1)" in zip_code_field_color, f"Поле {zip_code_field} не подсвечено зеленым"
# fields = ["first-name", "last-name", "address", "city", "country", "email", "phone_number", "job-position", "company"]