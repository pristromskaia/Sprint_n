import allure
from utils import test_data


@allure.feature("Подготовка к заказу такси")
class TestTaxiOrderPreparation:

    @allure.title("Переключение на таб Оптимальный — таб становится активным")
    def test_switch_to_optimal_tab(self, route_with_two_addresses):
        with allure.step("Нажать на таб 'Оптимальный'"):
            route_with_two_addresses.click_tab_optimal()
        with allure.step("Проверить, что активный таб — 'Оптимальный'"):
            active_tab = route_with_two_addresses.get_active_tab_text()
            assert test_data.ROUTE_TYPES["optimal"] in active_tab

    @allure.title("Переключение на таб Быстрый — таб становится активным")
    def test_switch_to_fast_tab(self, route_with_two_addresses):
        with allure.step("Нажать на таб 'Быстрый'"):
            route_with_two_addresses.click_tab_fast()
        with allure.step("Проверить, что активный таб — 'Быстрый'"):
            active_tab = route_with_two_addresses.get_active_tab_text()
            assert test_data.ROUTE_TYPES["fast"] in active_tab

    @allure.title(
        "Переключение между табами Оптимальный и Быстрый пересчитывает маршрут"
    )
    def test_switch_tabs_recalculates_route(self, route_with_two_addresses):

        with allure.step("Нажать на таб 'Оптимальный' и сохранить время и стоимость"):
            route_with_two_addresses.click_tab_optimal()

            optimal_time = route_with_two_addresses.get_route_time()
            optimal_price = route_with_two_addresses.get_route_cost()

        with allure.step("Нажать на таб 'Быстрый' и сохранить время и стоимость"):
            route_with_two_addresses.click_tab_fast()

            fast_time = route_with_two_addresses.get_route_time()
            fast_price = route_with_two_addresses.get_route_cost()

        with allure.step("Проверить, что маршрут пересчитался"):
            assert optimal_time != fast_time or optimal_price != fast_price, (
                f"Маршрут не изменился. "
                f"Оптимальный: {optimal_price}, {optimal_time}; "
                f"Быстрый: {fast_price}, {fast_time}"
            )

    @allure.title("При выборе таба Свой все типы передвижения становятся активными")
    def test_custom_tab_shows_all_transport_types(self, route_with_two_addresses):
        with allure.step("Нажать на таб 'Свой'"):
            route_with_two_addresses.click_tab_custom()

        with allure.step("Проверить, что все типы передвижения активны"):
            assert route_with_two_addresses.are_all_transport_types_active()

    @allure.title("Таб Свой — становится активным после нажатия")
    def test_custom_tab_becomes_active(self, route_with_two_addresses):
        with allure.step("Нажать на таб 'Свой'"):
            route_with_two_addresses.click_tab_custom()
        with allure.step("Проверить, что активный таб — 'Свой'"):
            active_tab = route_with_two_addresses.get_active_tab_text()
            assert test_data.ROUTE_TYPES["custom"] in active_tab

    @allure.title("При выборе таба Быстрый активна кнопка Вызвать такси")
    def test_fast_tab_shows_call_taxi_button(self, route_with_two_addresses):
        with allure.step("Нажать на таб 'Быстрый'"):
            route_with_two_addresses.click_tab_fast()
        with allure.step("Проверить, что кнопка 'Вызвать такси' активна"):
            assert route_with_two_addresses.is_call_taxi_button_active()

    @allure.title("При выборе типа Драйв в табе Свой активна кнопка Забронировать")
    def test_drive_transport_shows_book_button(self, route_with_two_addresses):
        with allure.step("Нажать на таб 'Свой'"):
            route_with_two_addresses.click_tab_custom()
        with allure.step("Выбрать тип передвижения 'Драйв'"):
            route_with_two_addresses.click_transport_drive()
        with allure.step("Проверить, что кнопка 'Забронировать' активна"):
            assert route_with_two_addresses.is_book_drive_button_active()
