from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

waiter = WebDriverWait(driver, 20)


driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

done = waiter.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))


picture = driver.find_element(By.CSS_SELECTOR, "#award")

src = picture.get_attribute("src")

print(src)

driver.quit()

