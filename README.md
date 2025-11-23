# Final Project Autotests

Автоматизация тестирования для сайта Лабиринт

## Запуск тестов

```bash
# Все тесты
pytest

# Только UI тесты  
pytest -m ui

# Только API тесты
pytest -m api

# С Allure отчетами
pytest --alluredir=allure-results
allure serve allure-results
