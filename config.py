# Конфигурация проекта для тестирования сайта Лабиринт

class Config:
    BASE_URL = "https://www.labirint.ru"

    # Тестовые данные
    BOOK_TITLE = "Война и мир"
    BOOK_AUTHOR = "Достоевский"
    BOOK_FOR_CART = "Цветок яблони: Алексей Пехов"
    GENRE = "фантастика"

    # Таймауты
    TIMEOUT = 10

    # Селекторы
    SEARCH_INPUT = "//input[@id='search-field']"
    SEARCH_BUTTON = "//button[@type='submit']"
    ADD_TO_CART_BUTTON = "//a[contains(@class, 'btn-buy')]"
    CART_COUNTER = "//span[@class='basket-in-cart-a']"
    CART_ICON = "//a[@class='b-basket']"
    CLEAR_CART_BUTTON = "//a[contains(text(), 'Очистить корзину')]"
    BOOKS_CATEGORY = "//a[contains(@href, 'books')]"
    FICTION_CATEGORY = "//a[contains(@href, 'fiction')]"
    FANTASY_CATEGORY = "//a[contains(@href, 'fantasy')]"
    SEARCH_RESULTS = "//div[contains(@class, 'product')]"
    CART_ITEMS = "//div[contains(@class, 'cart-item')]"
