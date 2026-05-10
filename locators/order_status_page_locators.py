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
    CAR_NUMBER = (
        By.XPATH,
        "//*[contains(@class,'car-number') or contains(@class,'plate') or contains(@class,'license')]",
    )
    TARIFF_IMAGE = (
        By.XPATH,
        "//*[contains(@class,'tariff')]//img | //*[contains(@class,'car-image')]",
    )
    DRIVER_NAME = (
        By.XPATH,
        "//*[contains(@class,'driver')]//*[contains(@class,'name')"
        " or contains(@class,'title') or self::span or self::p]",
    )
    DRIVER_PHOTO = (
        By.XPATH,
        "//*[contains(@class,'driver')]//img" " | //*[contains(@class,'avatar')]//img",
    )
    DRIVER_RATING = (
        By.XPATH,
        "//*[contains(@class,'rating') or contains(@class,'stars')]",
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
    DETAILS_ADDRESS_FROM = (
        By.XPATH,
        "//*[contains(text(),'Адрес подачи')]/following-sibling::*[1]",
    )
    DETAILS_ADDRESS_TO = (
        By.XPATH,
        "//*[contains(text(),'Адрес назначения')]/following-sibling::*[1]",
    )
