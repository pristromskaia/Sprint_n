from selenium.webdriver.common.by import By


class WaitingOrderPageLocators:
    TITLE_SEARCH = (
        By.XPATH,
        "//*[contains(text(),'Поиск машины')]"
        " | //*[contains(@class,'search-title') or contains(@class,'waiting-title')]",
    )
    TIMER = (By.CSS_SELECTOR, ".order-header-time")
    BTN_CANCEL = (By.XPATH, "//*[contains(normalize-space(),'Отменить')]")
    BTN_DETAILS = (
        By.XPATH,
        "//div[contains(@class,'order')]//*[contains(normalize-space(),'Детали')]",
    )


class CompletedOrderPageLocators:
    TITLE_ETA = (
        By.XPATH,
        "//div[contains(@class,'order-header-title') and contains(.,'приедет')]",
    )

    BTN_CANCEL = (By.XPATH, "//*[contains(normalize-space(),'Отменить')]")
    BTN_DETAILS = (
        By.XPATH,
        '//div[contains(@class,"order-btn-group")][.//div[normalize-space()="Детали"]]//button[contains(@class,"order-button")]',
    )
    DETAILS_COST = (
        By.XPATH,
        "//div[contains(@class,'order-details') and contains(@class,'shown')]"
        "//*[contains(.,'Стоимость')]",
    )
