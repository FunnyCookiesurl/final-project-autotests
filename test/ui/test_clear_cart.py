import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLabirintUI:
    @pytest.mark.ui
    @allure.title("Очистка корзины")
    @allure.description("Очистка корзины после добавления товара")
    def test_clear_cart(self, browser):
        with allure.step("Шаг 1: Найти и добавить книгу в корзину"):
            wait = WebDriverWait(browser, 10)
            search_input = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='search-field']"))
            )
            search_input.send_keys("Цветок яблони: Алексей Пехов")

            search_button = browser.find_element(
                By.XPATH, "//button[@type='submit']")
            search_button.click()

            wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "btn-tocart"))
            )

            add_to_cart_buttons = browser.find_elements(
                By.CLASS_NAME, "btn-tocart")

            if add_to_cart_buttons:
                add_to_cart_buttons[0].click()
                allure.attach(
                    "Книга добавлена в корзину",
                    name="Добавление",
                    attachment_type=allure.attachment_type.TEXT
                )
            else:
                raise AssertionError("Кнопки 'В КОРЗИНУ' не найдены!")

        with allure.step("Шаг 2: Проверить счетчик и открыть корзину"):
            wait.until(
                EC.text_to_be_present_in_element(
                    (By.XPATH, "//span[contains(@class, 'basket-in-cart-a')]"),
                    "1"
                )
            )

            open_cart = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cart-icon-js"))
            )
            open_cart.click()

        with allure.step("Шаг 3: Очистить корзину"):
            clear_cart_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[contains(@class, 'b-link-popup') "
                     "and contains(text(), 'Очистить корзину')]")
                )
            )
            clear_cart_button.click()
            allure.attach(
                "Корзина очищена",
                name="Очистка",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Шаг 4: Проверить завершение теста"):
            allure.attach(
                "Тест завершен успешно",
                name="Результат",
                attachment_type=allure.attachment_type.TEXT
            )
