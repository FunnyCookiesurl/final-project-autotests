import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config import Config


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get(Config.BASE_URL)

    # Закрыть cookie-баннер перед каждым тестом
    try:
        cookie_accept = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Принять')]")
        cookie_accept.click()
    except Exception:
        pass  # Если баннера нет - продолжаем

    yield driver
    driver.quit()
