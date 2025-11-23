import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLabirintNavigation:
    @pytest.mark.ui
    @allure.title("Фильтрация по жанру")
    @allure.description("ST-05: Навигация по разделам книг")
    def test_filter_by_genre(self, browser):
        wait = WebDriverWait(browser, 10)

        with allure.step("Шаг 1: Кликнуть на раздел 'Книги'"):
            books_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Книги"))
            )
            books_link.click()
            allure.attach(
                "Перешли в раздел Книги",
                name="Навигация",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Шаг 2: Кликнуть раздел 'Художественная литература'"):
            fiction_link = wait.until(
                EC.element_to_be_clickable(
                    (By.LINK_TEXT, "Художественная литература")
                )
            )
            fiction_link.click()
            allure.attach(
                "Перешли в Художественную литературу",
                name="Навигаation",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Шаг 3: Кликнуть на раздел 'Фантастика'"):
            fantasy_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Фантастика"))
            )
            fantasy_link.click()
            allure.attach(
                "Перешли в раздел Фантастика",
                name="Навигация",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Шаг 4: Проверить заголовок страницы"):
            page_title = wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "h1"))
            )
            assert "фантастика" in page_title.text.lower()
            allure.attach(
                f"Заголовок страницы: {page_title.text}",
                name="Проверка заголовка",
                attachment_type=allure.attachment_type.TEXT
            )

        allure.attach(
            "Успешно перешли в раздел фантастики",
            name="Результат",
            attachment_type=allure.attachment_type.TEXT
        )
