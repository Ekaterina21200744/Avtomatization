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


# images = waiter.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img")))

sleep (10)
pictures = driver.find_elements(By.CSS_SELECTOR, "img")

# l = len(pictures)
# print(l)

src = pictures[2].get_attribute("src")

print(src)

driver.quit()

