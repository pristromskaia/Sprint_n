# Sprint 3 — UI автотесты для сервиса маршрутов и такси

Проект содержит автотесты на Selenium + Pytest для проверки функциональности построения маршрутов, заказа такси и бронирования Drive.

## Стек

- Python
- Selenium
- Pytest
- Allure Report

---

# Структура проекта

```text
.
├── pages/                 # Page Object классы
├── locators/              # Локаторы элементов
├── tests/                 # UI тесты
├── allure-results/        # Результаты Allure
├── conftest.py            # Фикстуры pytest
├── test_data.py           # Тестовые данные
├── requirements.txt
└── pytest.ini
```

---

# Установка зависимостей

```bash
pip install -r requirements.txt
```

---

# Запуск тестов

## Запуск всех тестов

```bash
pytest
```

## Запуск с Allure

```bash
pytest --alluredir=allure-results
```

---

# Генерация Allure-отчёта

## Открыть отчёт

```bash
allure serve allure-results
```

## Сгенерировать html-отчёт

```bash
allure generate allure-results -o allure-report --clean
```

---

# Покрытие тестами

- Отрисовка маршрута
- Отображение блока выбора маршрута
- Переключение видов маршрута
- Проверка типов передвижения
- Заказ такси
- Полный flow заказа такси
- Проверка тарифов и tooltip
- Проверка деталей поездки

---

# Особенности проекта

- Используется паттерн Page Object
- Тестовые данные вынесены отдельно
- Для предусловий используются фикстуры
- Баги помечены через `@pytest.mark.xfail`
- В тестах отсутствуют локаторы и прямое обращение к driver