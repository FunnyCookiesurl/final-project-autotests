import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLabirintSearch:
    @pytest.mark.ui
    @allure.title("Поиск книги по названию")
    @allure.description("ST-03: Поиск книги по названию 'Война и мир'")
    def test_search_by_book_title(self, browser):
        wait = WebDriverWait(browser, 10)

        with allure.step("Шаг 1: Кликнуть на строку поиска"):
            search_input = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='search-field']"))
            )
            search_input.click()

        with allure.step("Шаг 2: Ввести название книги 'Война и мир'"):
            search_input.send_keys("Война и мир")

        with allure.step("Шаг 3: Нажать кнопку поиска"):
            search_button = browser.find_element(
                By.XPATH, "//button[@type='submit']")
            search_button.click()

        with allure.step("Шаг 4: Ждем результаты поиска"):
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[contains(text(), 'Война и мир')]"))
            )

        with allure.step("Шаг 5: Проверить результаты поиска"):
            search_results = browser.find_elements(
                By.XPATH, "//a[contains(text(), 'Война и мир')]")
            assert len(search_results) > 0, (
                "Книга 'Война и мир' не найдена")

            allure.attach(
                f"Найдено результатов: {len(search_results)}",
                name="Результаты поиска",
                attachment_type=allure.attachment_type.TEXT
            )
