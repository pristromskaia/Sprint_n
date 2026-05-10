import allure


@allure.feature("Отрисовка маршрута")
class TestRouteRendering:
    @allure.title("Карта отображается на начальном экране")
    def test_map_is_displayed(self, main_page):
        with allure.step("Проверить, что карта отображается"):
            assert main_page.is_map_displayed()

    @allure.title("Две точки маршрута на карте при вводе двух разных адресов")
    def test_two_map_markers_displayed_with_different_addresses(
        self, main_with_two_addresses
    ):
        with allure.step("Получить маркеры на карте"):
            markers = main_with_two_addresses.get_map_markers()
        with allure.step("Проверить, что на карте отображается не менее двух маркеров"):
            assert len(markers) >= 2
