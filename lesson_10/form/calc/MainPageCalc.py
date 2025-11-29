import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Главная страница калькулятора")
@allure.description("Класс для автоматизации тестирования главной страницы калькулятора с задержкой.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("Калькулятор")
class MainPageCalc:

    """Класс для автоматизации тестирования главной страницы калькулятора с задержкой."""

    @allure.title("Инициализация главной страницы калькулятора")
    @allure.description("Инициализирует драйвер и открывает страницу калькулятора.")
    @allure.step("Инициализация главной страницы калькулятора")
    def __init__(self, driver):

        with allure.step("Инициализация WebDriwer"):
            self._driver = driver

        with allure.step("Открытие страницы калькулятора"):
            self._driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        with allure.step("Установка ожидания"):
            self.wait = WebDriverWait(self._driver, 20)

    @allure.title("Установка задержки")
    @allure.description(
        "Выставляет задержку 45 с, чтобы получить результат основных арифметических операций.")
    @allure.step("Установка задержки")
    def set_delay(self, delay_value: str = "45"):
        """Выставляет задержку 45 с, чтобы получить результат основных арифметических операций."""
        with allure.step(f"Установка задержки вычислений"):
            with allure.step(f"Поиск поля ввода задержки"):
                delay_input = self.wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "#delay")))

            with allure.step(f"Очистка поля ввода"):
                delay_input.clear()

            with allure.step(f"Ввод задержки вычислений"):
                delay_input.send_keys(str(delay_value))

    @allure.title("Нажатие на кнопки калькулятора")
    @allure.description("Нажимает на кнопки калькулятора для выполнения операции 7 + 8 =")
    @allure.step("Нажатие на кнопки калькулятора")
    def clicK_button(self):
        """ Нажатие на установленные кнопки"""

        buttons_to_click = ["7", "+", "8", "="]
        with allure.step("Выполнение арифметической операции: 7 + 8 ="):
            for button_text in buttons_to_click:
                with allure.step(f"Нажатие кнопки: '{button_text}'"):
                    button = self._driver.find_element(
                        By.XPATH, f"//span[text()='{button_text}']")
                    button.click()

    @allure.title("Получение результата")
    @allure.description("Получение результата после выполнения операции с задержкой.")
    @allure.step("Получение результата")
    def get_result(self):
        """Получение результата"""

        with allure.step("Ожидание результата вычислений с задержкой 47 секунд"):
            long_wait = WebDriverWait(self._driver, 47)
            long_wait.until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, ".screen"), "15"))

        with allure.step("Извлечение текста результата из элемента .screen"):
            result = self._driver.find_element(By.CSS_SELECTOR, ".screen")
            actual_result = result.text

        with allure.step("Возврат текста результата из элемента .screen"):
            return actual_result

    @allure.title("Проверка результата")
    @allure.description("Проверка полученного результата после выполнения операции с задержкой.")
    @allure.step("Пооверка полученного результата")
    def check_result(self, expected_result: str = "15"):
        """Поверка полученного результата"""

        with allure.step("Получение фактического результата вычислений"):
            actual_result = self.get_result()

        with allure.step("Сравнение ожидаемого и получееного результа"):
            assert actual_result == expected_result, f"Ожидалось '{expected_result}', получено '{actual_result}'"

    @allure.title("Закрытие браузера")
    @allure.description("Закрытие браузера после завершения тестирования.")
    @allure.step("Завершение работы браузера")
    def close_browser(self):
        """Закрытие браузера"""

        self._driver.quit()
