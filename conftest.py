import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.route_page import RoutePage
from pages.taxi_order_page import TaxiOrderPage
from pages.order_status_page import WaitingOrderPage, CompletedOrderPage
import test_data


def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    return webdriver.Chrome(options=options)


@pytest.fixture()
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    page.open(test_data.BASE_URL)
    return page


@pytest.fixture()
def route_page(driver):
    return RoutePage(driver)


@pytest.fixture()
def taxi_order_page(driver):
    return TaxiOrderPage(driver)


@pytest.fixture()
def waiting_page(driver):
    return WaitingOrderPage(driver)


@pytest.fixture()
def completed_page(driver):
    return CompletedOrderPage(driver)


@pytest.fixture()
def main_with_two_addresses(driver):
    main = MainPage(driver)
    main.open(test_data.BASE_URL)
    main.enter_addresses(test_data.ADDRESS_FROM, test_data.ADDRESS_TO)
    return main


@pytest.fixture()
def main_with_same_address(driver):
    main = MainPage(driver)
    main.open(test_data.BASE_URL)
    main.enter_addresses(test_data.ADDRESS_FROM, test_data.ADDRESS_SAME)
    return main


@pytest.fixture()
def route_with_two_addresses(driver):
    main = MainPage(driver)
    main.open(test_data.BASE_URL)
    main.enter_addresses(test_data.ADDRESS_FROM, test_data.ADDRESS_TO)
    return RoutePage(driver)


@pytest.fixture()
def taxi_form_opened(driver):
    main = MainPage(driver)
    main.open(test_data.BASE_URL)
    main.enter_addresses(test_data.ADDRESS_FROM, test_data.ADDRESS_TO)
    route = RoutePage(driver)
    route.click_tab_fast()
    route.click_call_taxi()
    return TaxiOrderPage(driver)
