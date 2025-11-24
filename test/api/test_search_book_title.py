import requests
import pytest
import allure


class TestLabirintAPI:
    """API тесты для поиска книг на Лабиринте"""

    BASE_URL = "https://www.labirint.ru"
    SEARCH_ENDPOINT = "/search/"

    @pytest.mark.api
    @allure.title("Поиск книги по кириллице")
    @allure.description("Тест 1: Поиск книги 'Война и мир' на кириллице")
    def test_search_books_by_title_cyrillic(self):
        with allure.step("Отправить GET запрос с кириллическим названием"):
            url = (f"{self.BASE_URL}{self.SEARCH_ENDPOINT}"
                   f"Война%20и%20мир/?stype=0")
            response = requests.get(url)

        with allure.step("Проверить статус код и содержимое ответа"):
            assert response.status_code == 200
            assert "Война и мир" in response.text
            assert response.elapsed.total_seconds() < 3

            allure.attach(
                f"Время ответа: {response.elapsed.total_seconds()} сек",
                name="Производительность",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                "Тест пройден: поиск по кириллице работает",
                name="Результат",
                attachment_type=allure.attachment_type.TEXT
            )

    @pytest.mark.api
    @allure.title("Поиск книги по латинице")
    @allure.description("Тест 2: Поиск книги 'War and peace' на латинице")
    def test_search_books_by_title_latin(self):
        with allure.step("Отправить GET запрос с латинским названием"):
            url = (f"{self.BASE_URL}{self.SEARCH_ENDPOINT}"
                   f"War%20and%20peace/?stype=0")
            response = requests.get(url)

        with allure.step("Проверить статус код и содержимое ответа"):
            assert response.status_code == 200
            assert "War and peace" in response.text
            assert response.elapsed.total_seconds() < 3

            allure.attach(
                f"Время ответа: {response.elapsed.total_seconds()} сек",
                name="Производительность",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                "Тест пройден: поиск по латинице работает",
                name="Результат",
                attachment_type=allure.attachment_type.TEXT
            )

    @pytest.mark.api
    @allure.title("Поиск книги по автору")
    @allure.description("Тест 3: Поиск книг по автору 'Лев Толстой'")
    def test_search_books_by_author(self):
        with allure.step("Отправить GET запрос с именем автора"):
            url = (f"{self.BASE_URL}{self.SEARCH_ENDPOINT}"
                   f"Лев%20Толстой/?stype=0")
            response = requests.get(url)

        with allure.step("Проверить статус код и содержимое ответа"):
            assert response.status_code == 200
            assert "Лев Толстой" in response.text
            assert response.elapsed.total_seconds() < 3

            allure.attach(
                f"Время ответа: {response.elapsed.total_seconds()} сек",
                name="Производительность",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                "Тест пройден: поиск по автору работает",
                name="Результат",
                attachment_type=allure.attachment_type.TEXT
            )

    @pytest.mark.api
    @allure.title("Поиск со спецсимволами")
    @allure.description("Тест 4: Поиск с использованием специальных символов")
    def test_search_with_special_characters(self):
        with allure.step("Отправить GET запрос со спецсимволами"):
            url = (f"{self.BASE_URL}{self.SEARCH_ENDPOINT}"
                   f"!%40%23%24%25/?stype=0")
            response = requests.get(url)

        with allure.step("Проверить статус код и время ответа"):
            assert response.status_code == 200
            assert response.elapsed.total_seconds() < 5

            allure.attach(
                f"Время ответа: {response.elapsed.total_seconds()} сек",
                name="Производительность",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                "Тест пройден: спецсимволы обрабатываются",
                name="Результат",
                attachment_type=allure.attachment_type.TEXT
            )

    @pytest.mark.api
    @allure.title("Поиск через POST метод")
    @allure.description("Тест 5: Проверка POST метода вместо GET")
    def test_search_with_post_method(self):
        with allure.step("Отправить POST запрос вместо GET"):
            url = f"{self.BASE_URL}{self.SEARCH_ENDPOINT}Война%20и%20мир"
            response = requests.post(url)

        with allure.step("Проверить статус код и время ответа"):
            assert response.status_code == 200
            assert response.elapsed.total_seconds() < 3

            allure.attach(
                f"Время ответа: {response.elapsed.total_seconds()} сек",
                name="Производительность",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                "Тест пройден: POST метод работает",
                name="Результат",
                attachment_type=allure.attachment_type.TEXT
            )
