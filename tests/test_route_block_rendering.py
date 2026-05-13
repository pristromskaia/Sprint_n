import allure
from utils import test_data


@allure.feature("Отрисовка блока с выбором маршрута")
class TestRouteBlockRendering:

    @allure.title("Блок выбора маршрута отображается при вводе двух разных адресов")
    def test_route_block_displayed_with_different_addresses(
        self, route_with_two_addresses
    ):
        with allure.step("Проверить отображение блока выбора маршрута"):
            assert route_with_two_addresses.is_route_block_displayed()

    @allure.title(
        "Блок маршрута при одинаковых адресах содержит 'Авто Бесплатно В пути 0 мин.'"
    )
    def test_route_block_with_same_addresses_contains_expected_text(
        self, main_with_same_address, route_page
    ):
        with allure.step("Получить текст блока выбора маршрута"):
            block_text = route_page.get_route_block_text()

        with allure.step("Проверить текст блока маршрута"):
            assert test_data.SAME_ADDRESS_ROUTE_FULL_TEXT in block_text
