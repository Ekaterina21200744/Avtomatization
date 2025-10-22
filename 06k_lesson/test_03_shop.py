from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form(username="standard_user", password_text="secret_sauce", expected_total="Total: $58.29"):
  
    driver = webdriver.Firefox(service=FirefoxService())
    
    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 20)
        
        login(driver, wait, username, password_text)
        
        add_products_to_cart(driver, wait)
        
        checkout_process(driver, wait)
        
        total_amount = get_total_amount(driver, wait)
        

        assert total_amount == expected_total, f"Ожидалось '{expected_total}', получено '{total_amount}'"
        
        print("Тест пройден.")
        return True
    
        
    except AssertionError as e:
        print(f"Тест не пройден: {e}")
        return False

    finally:
        driver.quit()
        print("Браузер закрыт.")

def login(driver, wait, username, password_text):
    
    user_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name")))
    user_name.send_keys(username)

    password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))
    password.send_keys(password_text)

    login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#login-button")))
    login_button.click()
    

def add_products_to_cart(driver, wait):
    
    products = [
        ("#add-to-cart-sauce-labs-backpack", "Sauce Labs Backpack"),
        ("#add-to-cart-sauce-labs-bolt-t-shirt", "Sauce Labs Bolt T-Shirt"), 
        ("#add-to-cart-sauce-labs-onesie", "Sauce Labs Onesie")
    ]
    
    for selector, product_name in products:
        product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        product.click()

def checkout_process(driver, wait):
    
    cart = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge")))
    cart.click()
    
    checkout = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#checkout")))
    checkout.click()
    
    first_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#first-name")))
    first_name.send_keys("Иван")

    last_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#last-name")))
    last_name.send_keys("Иванов")

    zip_postal_code = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#postal-code")))
    zip_postal_code.send_keys("1234567")
    
    but_continue = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#continue")))
    but_continue.click()

def get_total_amount(driver, wait):
    
    total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
    result = total.text 
    print(f"   Итоговая сумма: {result}")
    
    return result

if __name__ == "__main__":
    test_form()