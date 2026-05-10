from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_status_page_locators import (
    WaitingOrderPageLocators,
    CompletedOrderPageLocators,
)


class WaitingOrderPage(BasePage):

    def is_search_title_displayed(self):
        return self.is_visible(WaitingOrderPageLocators.TITLE_SEARCH)

    def is_timer_displayed(self):
        return self.is_visible(WaitingOrderPageLocators.TIMER)

    def is_cancel_button_displayed(self):
        return self.is_visible(WaitingOrderPageLocators.BTN_CANCEL)

    def is_details_button_displayed(self):
        return self.is_visible(WaitingOrderPageLocators.BTN_DETAILS)

    def click_details(self):
        self.find_clickable(WaitingOrderPageLocators.BTN_DETAILS).click()

    def click_cancel(self):
        self.find_clickable(WaitingOrderPageLocators.BTN_CANCEL).click()


class CompletedOrderPage(BasePage):

    def is_eta_title_displayed(self):
        return self.is_visible(CompletedOrderPageLocators.TITLE_ETA)

    def is_cancel_button_displayed(self):
        return self.is_visible(CompletedOrderPageLocators.BTN_CANCEL)

    def is_details_button_displayed(self):
        return self.is_visible(CompletedOrderPageLocators.BTN_DETAILS)

    def is_driver_info_displayed(self):
        return self.is_visible(CompletedOrderPageLocators.DRIVER_NAME)

    def click_details(self):
        self.find_clickable(CompletedOrderPageLocators.BTN_DETAILS).click()
        self.find_visible(CompletedOrderPageLocators.DETAILS_COST)

    def click_cancel(self):
        self.find_clickable(CompletedOrderPageLocators.BTN_CANCEL).click()

    def get_details_cost_text(self):
        return self.get_text(CompletedOrderPageLocators.DETAILS_COST)

    def is_details_cost_displayed(self):
        return self.is_visible(CompletedOrderPageLocators.DETAILS_COST)

    def wait_until_eta_visible(self):
        WebDriverWait(self.driver, 40).until(
            EC.text_to_be_present_in_element(
                CompletedOrderPageLocators.TITLE_ETA, "приедет"
            )
        )
