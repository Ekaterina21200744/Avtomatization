from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


firefox_options = Options()

driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()),
        options=firefox_options
)

driver.get("http://the-internet.herokuapp.com/login")

search_locator_username = "input[name='username']"

search_input_locator_username = driver.find_element(By.CSS_SELECTOR, search_locator_username)
search_input_locator_username.send_keys("tomsmith")
sleep(2)


search_locator_password = "input[name='password']"

search_input_locator_password = driver.find_element(By.CSS_SELECTOR, search_locator_password)
search_input_locator_password.send_keys("SuperSecretPassword!")
sleep(2)

button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

button.click()

search_green_text = driver.find_element(By.CSS_SELECTOR, "div[class='flash success']")
banner_text = search_green_text.text
print(banner_text)



driver.quit()