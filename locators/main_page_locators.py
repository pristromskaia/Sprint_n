from selenium.webdriver.common.by import By


class MainPageLocators:
    INPUT_FROM = (By.ID, "from")
    INPUT_TO = (By.ID, "to")
    MAP_LAYER = (By.CLASS_NAME, "map")
    MAP_MARKERS = (
        By.XPATH,
        "//*[contains(@class,'ymaps') and contains(@class,'placemark')]",
    )
    ROUTE_BLOCK = (By.XPATH, "//*[contains(@class,'result')]")
    POPUP_CLOSE_BTN = (By.CLASS_NAME, "section-close")
