import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Форма")
class MainPageF:

    """Класс для автоматизации тестирования главной страницы формы."""

    @allure.step("Инициализация главной страницы Формы")
    def __init__(self, driver):

        with allure.step("Инициализация WebDriwer"):
            self.driver = driver
        with allure.step("Установка ожидания"):
            self.wait = WebDriverWait(driver, 5)
        with allure.step("Заполнение полей формы тестовыми данными"):    
            self.fields: dict = {
                'first-name': "Иван",
                'last-name': "Петров",
                'address': "Ленина, 55-3",
                'zip-code': "",
                'city': "Москва",
                'country': "Россия",
                'e-mail': "test@skypro.com",
                'phone': "+7985899998787",
                'job-position': "QA",
                'company': "SkyPro"
            }

    @allure.step("Открыть браузер и перейти на страницу формы")
    def open(self):
        """Открывает браузер"""

        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Заполнение формы")
    def fill_form(self):
        """ Заполняет все поля формы данными из словаря 'fields'.
            Поле zip-code остается пустым ("")"""

        for field, value in self.fields.items():
            with allure.step(f"Заполнить поле {field} значением '{value}'"):
                self.wait.until(
                    EC.presence_of_element_located(
                        (By.NAME, field))).send_keys(value)

    @allure.step("Нажать кнопку отправки формы")
    def submit_form(self):
        """Нажимает кнопку отправки формы 'Submit'"""

        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[type="submit"]'))).click()

    @allure.step("Получить класс поля формы с id '{field_id}'")
    def get_field_class(self, field_id: str) -> str:
        """Проверяет заполнение полей формы по их id"""

        element = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, field_id))).get_attribute("class")
        return element

    @allure.step("Проверить наличие ошибки для поля zip-code")
    def check_zip_code_error(self):
        """Проверяет, что для незаполненного поля zip-code установился класс ошибки"""

        return "alert-danger" in self.get_field_class("zip-code")

    @allure.step("Проверить успешное заполнение всех полей формы")
    def check_fields_success(self):
        """Проверяет, что для всех заполненных полей установился класс успешного заполнения"""

        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            with allure.step(f"Проверить поле {field}"):
                if "success" not in self.get_field_class(field):
                    return False
        return True

    @allure.step("Проверить корректность заполнения формы после отправки")
    def check_form_submission(self):
        """Проверяет корректность заполнения формы после ее отправки"""

        with allure.step("Проверить наличие ошибки в поле zip-code"):
            assert self.check_zip_code_error()
        with allure.step("Проверить успешное заполнение всех остальных полей"):
            assert self.check_fields_success()
