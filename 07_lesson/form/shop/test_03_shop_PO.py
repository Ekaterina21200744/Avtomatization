from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from AuthorizationPage import AuthorizationPage
from MainPage import MainPage
from CartPage import CartPage
from OrderPage import OrderPage

def test_shop(expected_total="Total: $58.29"):

    # driver = webdriver.Firefox(service=FirefoxService())
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    authorization_page = AuthorizationPage(browser)
    authorization_page.open()
    authorization_page.login(username = "standard_user", password_text = "secret_sauce")

    main_page = MainPage(browser)
    main_page.add_products_to_cart()
    main_page.get_cart()

    cart_page = CartPage(browser)
    cart_page.click_checkout()

    order_page = OrderPage(browser)
    order_page.fill_fields()
    order_page.continue_to_overview()
    order_page.get_total_amount()

    total_amount = order_page.get_total_amount()

    assert total_amount == expected_total, f"Ожидалось '{expected_total}', получено '{total_amount}'"
        
    print("Тест пройден.")

    browser.quit()



