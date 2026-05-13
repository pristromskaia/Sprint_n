from pages.base_page import BasePage
from locators.route_page_locators import RoutePageLocators


class RoutePage(BasePage):

    def click_tab_optimal(self):
        self.click(RoutePageLocators.TAB_OPTIMAL)

    def click_tab_fast(self):
        self.click(RoutePageLocators.TAB_FAST)

    def click_tab_custom(self):
        self.click(RoutePageLocators.TAB_CUSTOM)

    def get_active_tab_text(self):
        return self.get_text(RoutePageLocators.ACTIVE_TAB)

    def get_route_block_text(self):
        return self.get_text(RoutePageLocators.ROUTE_RESULT_BLOCK)

    def is_route_block_displayed(self):
        return self.is_visible(RoutePageLocators.ROUTE_RESULT_BLOCK)

    def is_call_taxi_button_active(self):
        btn = self.find_clickable(RoutePageLocators.BTN_CALL_TAXI)
        return btn.is_enabled() and btn.is_displayed()

    def is_book_drive_button_active(self):
        btn = self.find_clickable(RoutePageLocators.BTN_BOOK_DRIVE)
        self.scroll_to_element(btn)
        return btn.is_enabled() and btn.is_displayed()

    def click_transport_drive(self):
        self.click(RoutePageLocators.TRANSPORT_DRIVE)

    def click_call_taxi(self):
        self.click(RoutePageLocators.BTN_CALL_TAXI)

    def get_route_cost(self):
        return self.get_text(RoutePageLocators.ROUTE_COST)

    def get_route_time(self):
        return self.get_text(RoutePageLocators.ROUTE_TIME)

    def is_transport_type_active(self, locator):
        element = self.find_visible(locator)
        return "disabled" not in element.get_attribute("class")

    def are_all_transport_types_active(self):
        transport_types = [
            RoutePageLocators.TRANSPORT_CAR,
            RoutePageLocators.TRANSPORT_WALK,
            RoutePageLocators.TRANSPORT_TAXI,
            RoutePageLocators.TRANSPORT_BIKE,
            RoutePageLocators.TRANSPORT_SCOOTER,
            RoutePageLocators.TRANSPORT_DRIVE,
        ]

        return all(
            self.is_transport_type_active(locator) for locator in transport_types
        )
