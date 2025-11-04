from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait


from MainPageCalc import MainPageCalc


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 20)

def test_calc():

    main_page = MainPageCalc(driver)
    main_page.set_delay
    main_page.clicK_button
    main_page.get_result
    main_page.check_result
    main_page.close_browser

