import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLabirintSearch:
    @pytest.mark.ui
    @allure.title("Поиск книги по автору")
    @allure.description("ST-04: Поиск книг по фамилии автора Достоевский")
    def test_search_by_author(self, browser):
        wait = WebDriverWait(browser, 10)

        with allure.step("Шаг 1: Кликнуть на строку поиска"):
            search_input = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='search-field']"))
            )
            search_input.click()

        with allure.step("Шаг 2: Ввести фамилию автора 'Достоевский'"):
            search_input.send_keys("Достоевский")

        with allure.step("Шаг 3: Нажать кнопку поиска"):
            search_button = browser.find_element(
                By.XPATH, "//button[@type='submit']")
            search_button.click()

        with allure.step("Шаг 4: Ждем результаты поиска"):
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[contains(text(), 'Достоевский')]"))
            )

        with allure.step("Шаг 5: Проверить результаты поиска"):
            search_results = browser.find_elements(
                By.XPATH, "//a[contains(text(), 'Достоевский')]")
            assert len(search_results) > 0, (
                "Книги Достоевского не найдены в результатах поиска")

            allure.attach(
                f"Найдено книг Достоевского: {len(search_results)}",
                name="Результаты поиска",
                attachment_type=allure.attachment_type.TEXT
            )
