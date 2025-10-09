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

driver.get("https://the-internet.herokuapp.com/inputs")

search_locator = "input[type='number']"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

search_input.send_keys("Sky")
sleep (2)

search_input.clear()
sleep(2)

search_input.send_keys("Pro")
sleep (2)

driver.quit()