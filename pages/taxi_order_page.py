from pages.base_page import BasePage
from locators.taxi_order_page_locators import TaxiOrderPageLocators
from selenium.common.exceptions import TimeoutException


class TaxiOrderPage(BasePage):

    def get_tariff_cards(self):
        return self.find_all(TaxiOrderPageLocators.TARIFF_CARDS)

    def get_tariff_count(self):
        return len(self.get_tariff_cards())

    def is_any_tariff_active(self):
        return self.is_visible(TaxiOrderPageLocators.ACTIVE_TARIFF)

    def select_tariff_worker(self):
        self.click(TaxiOrderPageLocators.TARIFF_WORKER)

    def get_tooltip_text(self):
        return self.get_text(TaxiOrderPageLocators.TARIFF_TOOLTIP)

    def is_tooltip_visible(self):     
        try:
            self.find_visible(
                TaxiOrderPageLocators.TARIFF_TOOLTIP,
                timeout=5
            )
            return True
        except TimeoutException:
            return False

    def is_phone_field_displayed(self):
        return self.is_visible(TaxiOrderPageLocators.FIELD_PHONE)

    def is_payment_field_displayed(self):
        return self.is_visible(TaxiOrderPageLocators.FIELD_PAYMENT)

    def is_comment_field_displayed(self):
        return self.is_visible(TaxiOrderPageLocators.FIELD_COMMENT)

    def is_requirements_displayed(self):
        return self.is_visible(TaxiOrderPageLocators.FIELD_REQUIREMENTS)

    def click_laptop_table_checkbox(self):
        self.click(TaxiOrderPageLocators.REQUIREMENTS_BLOCK)
        self.click(TaxiOrderPageLocators.CHECKBOX_LAPTOP_TABLE)

    def click_enter_phone_button(self):
        self.click(TaxiOrderPageLocators.BTN_ENTER_PHONE)

    def activate_tariff(self, index):
        cards = self.get_tariff_cards()
        self.js_click(cards[index])

    def get_active_info_icon(self):
        return self.find_visible(TaxiOrderPageLocators.ACTIVE_INFO_ICON)

    def hover_active_info_icon(self):
        icon = self.get_active_info_icon()
        self.hover(icon)

    def get_active_tariff_price(self):
        return self.get_text(TaxiOrderPageLocators.ACTIVE_TARIFF_PRICE)

    def get_tariff_names(self):
        return [
            element.text
            for element in self.find_all_visible(TaxiOrderPageLocators.TARIFF_TITLES)
        ]
