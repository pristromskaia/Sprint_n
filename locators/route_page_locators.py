from selenium.webdriver.common.by import By


class RoutePageLocators:
    TAB_OPTIMAL = (By.XPATH, "//div[contains(@class,'mode') and text()='Оптимальный']")

    TAB_FAST = (By.XPATH, "//div[contains(@class,'mode') and text()='Быстрый']")

    TAB_CUSTOM = (
        By.XPATH,
        "//div[contains(@class,'mode') and normalize-space()='Свой']",
    )

    ACTIVE_TAB = (By.CSS_SELECTOR, ".mode.active")

    ROUTE_RESULT_BLOCK = (
        By.XPATH,
        "//*[contains(@class,'result') or contains(@class,'route-block') or contains(@class,'results')]",
    )
    ROUTE_COST = (
        By.XPATH,
        "//*[contains(text(),'Бесплатно') or contains(text(),'руб')]",
    )
    ROUTE_TIME = (
        By.XPATH,
        "//*[contains(@class,'time') or contains(@class,'duration') or contains(@class,'travel-time')]",
    )

    BTN_CALL_TAXI = (
        By.XPATH,
        "//button[contains(.,'Вызвать такси')]"
        " | //*[@role='button' and contains(.,'Вызвать такси')]",
    )
    BTN_BOOK_DRIVE = (By.XPATH, "//button[normalize-space()='Забронировать']")

    TRANSPORT_CAR = (
        By.XPATH,
        '//div[contains(@class,"types-container")]/div[contains(@class,"type")][1]',
    )

    TRANSPORT_WALK = (
        By.XPATH,
        '//div[contains(@class,"types-container")]/div[contains(@class,"type")][2]',
    )

    TRANSPORT_TAXI = (
        By.XPATH,
        '//div[contains(@class,"types-container")]/div[contains(@class,"type")][3]',
    )

    TRANSPORT_BIKE = (
        By.XPATH,
        '//div[contains(@class,"types-container")]/div[contains(@class,"type")][4]',
    )

    TRANSPORT_SCOOTER = (
        By.XPATH,
        '//div[contains(@class,"types-container")]/div[contains(@class,"type")][5]',
    )

    TRANSPORT_DRIVE = (By.CSS_SELECTOR, ".type.drive")
