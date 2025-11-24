import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLabirintUI:
    @pytest.mark.ui
    @allure.title("Добавление товара в корзину")
    @allure.description(
        "ST-02: Проверка добавления книги в корзину и обновления счетчика")
    def test_add_to_cart(self, browser):
        with allure.step("Шаг 1: Найти книгу через поиск"):
            wait = WebDriverWait(browser, 10)
            search_input = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='search-field']"))
            )
            search_input.send_keys("Цветок яблони: Алексей Пехов")

            search_button = browser.find_element(
                By.XPATH, "//button[@type='submit']")
            search_button.click()

        with allure.step("Шаг 2: Ждем загрузки результатов поиска"):
            wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "btn-tocart"))
            )

        with allure.step("Шаг 3: Добавить книгу в корзину"):
            add_to_cart_buttons = browser.find_elements(
                By.CLASS_NAME, "btn-tocart")
            allure.attach(
                f"Найдено кнопок: {len(add_to_cart_buttons)}",
                name="Количество кнопок",
                attachment_type=allure.attachment_type.TEXT
            )

            if add_to_cart_buttons:
                add_to_cart_buttons[0].click()
                allure.attach(
                    "Книга добавлена в корзину",
                    name="Статус добавления",
                    attachment_type=allure.attachment_type.TEXT
                )
            else:
                raise AssertionError("Кнопки 'В КОРЗИНУ' не найдены!")

        with allure.step("Шаг 4: Проверить обновление счетчика корзины"):
            wait.until(
                EC.text_to_be_present_in_element(
                    (By.XPATH, "//span[contains(@class, 'basket-in-cart-a')]"),
                    "1"
                )
            )

            cart_counter = browser.find_element(
                By.XPATH, "//span[contains(@class, 'basket-in-cart-a')]")

            with allure.step("Проверить что счетчик = 1"):
                assert cart_counter.text == "1", (
                    f"Ожидался счетчик 1, но получили: {cart_counter.text}")

            allure.attach(
                f"Счетчик корзины: {cart_counter.text}",
                name="Результат счетчика",
                attachment_type=allure.attachment_type.TEXT
            )
