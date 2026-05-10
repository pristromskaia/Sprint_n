from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def open(self, url):
        self.driver.get(url)
        self.wait_for_page_load()
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
        self.close_all_popups()

    def enter_address_from(self, address):
        field = self.find_clickable(MainPageLocators.INPUT_FROM)
        field.clear()
        field.send_keys(address)

    def enter_address_to(self, address):
        field = self.find_clickable(MainPageLocators.INPUT_TO)
        field.clear()
        field.send_keys(address)

    def enter_addresses(self, address_from, address_to):
        self.enter_address_from(address_from)
        self.enter_address_to(address_to)

    def get_map_markers(self):
        self.wait.until(
            EC.presence_of_all_elements_located(MainPageLocators.MAP_MARKERS)
        )
        return self.driver.find_elements(*MainPageLocators.MAP_MARKERS)

    def is_map_displayed(self):
        return self.is_visible(MainPageLocators.MAP_LAYER)

    def is_route_block_displayed(self):
        return self.is_visible(MainPageLocators.ROUTE_BLOCK)

    def get_route_block_text(self):
        return self.get_text(MainPageLocators.ROUTE_BLOCK)

    def close_all_popups(self):
        buttons = self.driver.find_elements(*MainPageLocators.POPUP_CLOSE_BTN)
        for btn in buttons:
            try:
                btn.click()
            except Exception:
                pass
