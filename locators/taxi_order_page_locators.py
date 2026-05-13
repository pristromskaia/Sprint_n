from selenium.webdriver.common.by import By


class TaxiOrderPageLocators:
    TARIFF_CARDS = (By.CSS_SELECTOR, ".tariff-cards > .tcard")
    ACTIVE_TARIFF = (
        By.XPATH,
        "//*[contains(@class,'tcard-i') and contains(@class,'active')]",
    )
    TARIFF_TITLES = (
        By.CSS_SELECTOR,
        ".tcard-title",
    )

    TARIFF_TOOLTIP = (By.CSS_SELECTOR, "div[data-id='tooltip'].show")

    FIELD_PHONE = (
        By.XPATH,
        "//div[contains(@class,'np-text') and contains(.,'Телефон')]",
    )
    FIELD_PAYMENT = (
        By.XPATH,
        "//div[contains(@class,'pp-text') and contains(.,'Способ оплаты')]",
    )
    FIELD_COMMENT = (
        By.XPATH,
        "//input[contains(@placeholder,'Комментарий') or contains(@name,'comment')"
        " or contains(@id,'comment')]"
        " | //textarea[contains(@placeholder,'Комментарий')]",
    )
    FIELD_REQUIREMENTS = (
        By.XPATH,
        "//*[contains(text(),'Требования к заказу') or contains(@class,'requirements')]",
    )

    BTN_ENTER_PHONE = (
        By.XPATH,
        "//button[contains(.,'Ввести номер и заказать')]"
        " | //button[contains(.,'Ввести номер')]",
    )

    ACTIVE_INFO_ICON = (
    By.XPATH,
    "//div[contains(@class,'tcard') and contains(@class,'active')]"
    "//*[contains(@class,'i-button')]",
)

    CHECKBOX_LAPTOP_TABLE = (By.CSS_SELECTOR, ".switch .slider")

    REQUIREMENTS_BLOCK = (By.XPATH, "//div[contains(text(),'Требования к заказу')]")

    ACTIVE_TARIFF_PRICE = (
        By.XPATH,
        "//div[contains(@class,'tcard') and contains(@class,'active')]//div[contains(@class,'tcard-price')]",
    )

    TARIFF_WORKER = (
        By.XPATH,
        "//div[contains(@class,'tcard')][.//div[contains(@class,'tcard-title') and normalize-space()='Рабочий']]",
    )
