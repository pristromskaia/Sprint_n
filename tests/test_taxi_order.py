import pytest
import allure
import test_data


@allure.feature("Заказ тарифа Такси")
class TestTaxiTariff:

    @allure.title("Форма заказа отображает 6 тарифов")
    def test_taxi_form_shows_six_tariffs(self, taxi_form_opened):
        with allure.step("Подсчитать количество тарифов"):
            count = taxi_form_opened.get_tariff_count()
        with allure.step("Проверить, что отображается 6 тарифов"):
            assert count == 6, f"Ожидалось 6 тарифов, отображается {count}"

    @allure.title("Форма заказа содержит все тарифы по ТЗ")
    def test_taxi_form_contains_expected_tariffs(self, taxi_form_opened):
        with allure.step("Получить названия тарифов"):
            tariff_names = taxi_form_opened.get_tariff_names()

        with allure.step("Проверить, что отображаются все тарифы по ТЗ"):
            for expected_tariff in test_data.EXPECTED_TARIFFS_TAXI_LIST:
                assert expected_tariff in tariff_names

    @allure.title("Один из тарифов активен по умолчанию")
    def test_one_tariff_is_active_by_default(self, taxi_form_opened):
        with allure.step("Проверить, что хотя бы один тариф активен"):
            assert taxi_form_opened.is_any_tariff_active()

    @allure.title("Отображается поле Телефон")
    def test_phone_field_is_displayed(self, taxi_form_opened):
        with allure.step("Проверить отображение поля Телефон"):
            assert taxi_form_opened.is_phone_field_displayed()

    @allure.title("Отображается поле Способ оплаты")
    def test_payment_field_is_displayed(self, taxi_form_opened):
        with allure.step("Проверить отображение поля Способ оплаты"):
            assert taxi_form_opened.is_payment_field_displayed()

    @allure.title("Отображается поле Комментарий водителю")
    def test_comment_field_is_displayed(self, taxi_form_opened):
        with allure.step("Проверить отображение поля Комментарий водителю"):
            assert taxi_form_opened.is_comment_field_displayed()

    @allure.title("Отображается блок Требования к заказу")
    def test_requirements_block_is_displayed(self, taxi_form_opened):
        with allure.step("Проверить отображение блока Требования к заказу"):
            assert taxi_form_opened.is_requirements_displayed()

    @allure.title("Всплывающее окно при наведении на иконку i каждого тарифа")
    @pytest.mark.parametrize("index", range(6))
    def test_tooltip_shown_on_hover_info_icon(self, taxi_form_opened, index):

        with allure.step(f"Активировать тариф №{index + 1}"):
            taxi_form_opened.activate_tariff(index)

        with allure.step("Навести на иконку i активного тарифа"):
            taxi_form_opened.hover_active_info_icon()

        with allure.step("Проверить отображение tooltip"):
            assert taxi_form_opened.is_tooltip_visible()

    @allure.title(
        "Текст заголовка и описания tooltip соответствует ТЗ для всех тарифов"
    )
    @pytest.mark.parametrize(
        "tariff",
        [
            test_data.TARIFFS_INFO_WORK_TEXTS,
            pytest.param(
                test_data.TARIFFS_INFO_SLEEP_TEXTS,
                marks=pytest.mark.xfail(
                    reason="описания для тарифов не соответствуют ТЗ"
                ),
            ),
            test_data.TARIFFS_INFO_HOLIDAY_TEXTS,
            pytest.param(
                test_data.TARIFFS_INFO_TALK_TEXTS,
                marks=pytest.mark.xfail(
                    reason="описания для тарифов не соответствуют ТЗ"
                ),
            ),
            test_data.TARIFFS_INFO_COMFORTING_TEXTS,
            test_data.TARIFFS_INFO_GLAM_TEXTS,
        ],
    )
    def test_tariff_tooltip_text(self, taxi_form_opened, tariff):
        with allure.step(f"Активировать тариф {tariff['title']}"):
            taxi_form_opened.activate_tariff(tariff["index"])

        with allure.step("Навести на иконку i активного тарифа"):
            taxi_form_opened.hover_active_info_icon()

        with allure.step("Проверить заголовок tooltip"):
            tooltip_text = taxi_form_opened.get_tooltip_text()
            assert tariff["title"] in tooltip_text

        with allure.step("Проверить описание tooltip"):
            assert tariff["description"] in tooltip_text


@allure.feature("Заказ тарифа Такси — полный флоу")
class TestTaxiFullFlow:

    @allure.title("Полный флоу: выбор тарифа Рабочий — окно ожидания машины")
    def test_full_flow_waiting_window_elements(self, taxi_form_opened, waiting_page):
        with allure.step("Выбрать тариф Рабочий"):
            taxi_form_opened.select_tariff_worker()
        with allure.step("Включить чекбокс 'Столик для ноутбука'"):
            taxi_form_opened.click_laptop_table_checkbox()
        with allure.step("Нажать кнопку 'Ввести номер и заказать'"):
            taxi_form_opened.click_enter_phone_button()
        with allure.step("Проверить заголовок окна ожидания"):
            assert (
                waiting_page.is_search_title_displayed()
            ), f"Заголовок '{test_data.WAITING_WINDOW_TITLE}' не отображается"
        with allure.step("Проверить отображение таймера обратного отсчёта"):
            assert waiting_page.is_timer_displayed()
        with allure.step("Проверить отображение кнопки 'Отменить'"):
            assert waiting_page.is_cancel_button_displayed()
        with allure.step("Проверить отображение кнопки 'Детали'"):
            assert waiting_page.is_details_button_displayed()

    @allure.title("Полный флоу: окно совершенного заказа после окончания таймера")
    def test_full_flow_completed_order_window(
        self, taxi_form_opened, waiting_page, completed_page
    ):
        with allure.step("Выбрать тариф Рабочий"):
            taxi_form_opened.select_tariff_worker()
        with allure.step("Включить чекбокс 'Столик для ноутбука'"):
            taxi_form_opted = taxi_form_opened
            taxi_form_opted.click_laptop_table_checkbox()
        with allure.step("Нажать кнопку 'Ввести номер и заказать'"):
            taxi_form_opted.click_enter_phone_button()
        with allure.step("Дождаться появления окна завершённого заказа"):
            completed_page.wait_until_eta_visible()
        with allure.step("Проверить заголовок окна совершённого заказа"):
            assert completed_page.is_eta_title_displayed()
        with allure.step("Проверить отображение кнопки 'Отменить'"):
            assert completed_page.is_cancel_button_displayed()
        with allure.step("Проверить отображение кнопки 'Детали'"):
            assert completed_page.is_details_button_displayed()

    @allure.title("Полный флоу: в деталях поездки указана стоимость тарифа")
    def test_full_flow_details_show_cost(
        self, taxi_form_opened, waiting_page, completed_page
    ):
        with allure.step("Выбрать тариф Рабочий"):
            taxi_form_opened.select_tariff_worker()
        with allure.step("Сохранить стоимость выбранного тарифа"):
            tariff_price = taxi_form_opened.get_active_tariff_price().replace(" ", "")
        with allure.step("Включить чекбокс 'Столик для ноутбука'"):
            taxi_form_opened.click_laptop_table_checkbox()
        with allure.step("Нажать кнопку 'Ввести номер и заказать'"):
            taxi_form_opened.click_enter_phone_button()
        with allure.step("Дождаться появления окна завершённого заказа"):
            completed_page.wait_until_eta_visible()
        with allure.step("Нажать кнопку 'Детали' в блоке завершённого заказа"):
            completed_page.click_details()
        with allure.step("Проверить, что стоимость отображается в деталях"):
            details_price = completed_page.get_details_cost_text().replace(" ", "")
            assert completed_page.is_details_cost_displayed()
            assert tariff_price in details_price

    @allure.title("Полный флоу: нажатие кнопки Отмена закрывает окно заказа")
    def test_full_flow_cancel_closes_window(
        self, taxi_form_opened, waiting_page, completed_page
    ):
        with allure.step("Выбрать тариф Рабочий"):
            taxi_form_opened.select_tariff_worker()
        with allure.step("Включить чекбокс 'Столик для ноутбука'"):
            taxi_form_opened.click_laptop_table_checkbox()
        with allure.step("Нажать кнопку 'Ввести номер и заказать'"):
            taxi_form_opened.click_enter_phone_button()
        with allure.step("Дождаться окончания таймера"):
            completed_page.wait_until_eta_visible()
        with allure.step("Нажать кнопку 'Отмена'"):
            completed_page.click_cancel()
        with allure.step("Проверить, что окно заказа закрылось"):
            assert not completed_page.is_eta_title_displayed()
