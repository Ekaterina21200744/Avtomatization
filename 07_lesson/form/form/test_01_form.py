import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from MainPageForm import MainPageForm


@pytest.fixture
def driver():
    edge_driver_path = r"c:\Users\gavri\Desktop\edge\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))

    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission_flow(driver):
    main_page = MainPageForm(driver)
    main_page.open()
    main_page.fill_form()
    main_page.submit_form()
    main_page.check_form_submission()