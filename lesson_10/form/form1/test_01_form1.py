import allure
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from MainPageF import MainPageF

@allure.title("Инициализация браузера Edge для тестирования")
@allure.description("Фикстура создает и настраивает экземпляр WebDriver для браузера Microsoft Edge.")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.fixture
def browser():
    """Фикстура для инициализации и завершения работы драйвера Edge"""

    edge_driver_path = r"c:\Users\gavri\Desktop\edge\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование формы")
@allure.description("Тестирование веб-формы: открытие страницы, заполнение полей данными, отправка формы и проверка успешности")
@allure.severity(allure.severity_level.BLOCKER)
def test_form_submission_flow(browser):
    """Тестирование формы"""

    main_page = MainPageF(browser)
    main_page.open()
    main_page.fill_form()
    main_page.submit_form()
    main_page.check_form_submission()
