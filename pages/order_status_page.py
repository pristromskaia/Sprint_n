from pages.base_page import BasePage
from locators.order_status_page_locators import (
    WaitingOrderPageLocators,
    CompletedOrderPageLocators,
)
from utils.test_data import EXPECTED_STATUS_TEXT


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
        self.click(WaitingOrderPageLocators.BTN_DETAILS)

    def click_cancel(self):
        self.click(WaitingOrderPageLocators.BTN_CANCEL)

class CompletedOrderPage(BasePage):

    def is_eta_title_displayed(self):
        return self.is_visible(CompletedOrderPageLocators.TITLE_ETA)

    def is_cancel_button_displayed(self):
        return self.is_visible(CompletedOrderPageLocators.BTN_CANCEL)

    def is_details_button_displayed(self):
        return self.is_visible(CompletedOrderPageLocators.BTN_DETAILS)

    def click_details(self):
        self.click(CompletedOrderPageLocators.BTN_DETAILS)
        self.find_visible(CompletedOrderPageLocators.DETAILS_COST)

    def click_cancel(self):
        self.click(CompletedOrderPageLocators.BTN_CANCEL)

    def get_details_cost_text(self):
        return self.get_text(CompletedOrderPageLocators.DETAILS_COST)

    def is_details_cost_displayed(self):
        return self.is_visible(CompletedOrderPageLocators.DETAILS_COST)

    def wait_until_eta_visible(self):
        self.wait_text_in_element(
            CompletedOrderPageLocators.TITLE_ETA,
            EXPECTED_STATUS_TEXT,
            timeout=40,
        )
