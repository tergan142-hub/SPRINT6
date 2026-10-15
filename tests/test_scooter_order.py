import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderLocatorsFirst, OrderLocatorsSecond


@allure.feature("Оформление заказа самоката")
class TestScooterOrder:

    @allure.title("Вариант 1: оформление заказа на 1 сутки, чёрный самокат")
    @allure.story("Проверка оформления заказа и получение номера заказа")
    def test_scooter_order_1(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Подготовка страницы и переход к форме заказа"):
            main_page.close_cookie_banner()
            main_page.click_on_order_button_first()

        with allure.step("Заполнение данных для заказа"):
            order_page.fill_name()
            order_page.fill_last_name()
            order_page.fill_address()
            order_page.select_metro_station()
            order_page.fill_phone()
            order_page.click_next_button()

        with allure.step("Выбор параметров аренды"):
            order_page.set_rental_date(days_offset=1)
            order_page.set_rental_period(option_locator=OrderLocatorsSecond.Quantity_1_day)
            order_page.select_scooter_color()
            order_page.submit_order()

        with allure.step("Подтверждение заказа"):
            order_page.confirm_order()

        with allure.step("Проверяем, что отображается кнопка статуса заказа"):
            is_visible = order_page.verify_status_button_visible()
            assert is_visible, "Кнопка статуса заказа не отображается — заказ не подтверждён"

    @allure.title("Вариант 2: заказ на 5 суток, серый самокат, комментарий курьеру")
    @allure.story("Проверка оформления заказа с дополнительными параметрами")
    def test_scooter_order_2(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        with allure.step("Подготовка страницы и переход к форме заказа (второй блок)"):
            main_page.close_cookie_banner()
            main_page.scroll_to_order_button_second()
            main_page.click_on_order_button_second()

        with allure.step("Заполнение данных для заказа"):
            order_page.fill_name()
            order_page.fill_last_name()
            order_page.fill_address()
            order_page.select_metro_station(station_locator=OrderLocatorsFirst.Komsomolskya_station_locator)
            order_page.fill_phone()
            order_page.click_next_button()

        with allure.step("Выбор параметров аренды"):
            order_page.set_rental_date(days_offset=5)
            order_page.set_rental_period(option_locator=OrderLocatorsSecond.Quantity_5_days)
            order_page.select_scooter_color(color_locator=OrderLocatorsSecond.Scooter_color_grey)
            order_page.fill_comment(comment="Пожалуйста, принесите самокат к подъезду.")
            order_page.submit_order()

        with allure.step("Подтверждение заказа"):
            order_page.confirm_order()

        with allure.step("Проверяем, что отображается кнопка статуса заказа"):
            is_visible = order_page.verify_status_button_visible()
            assert is_visible, "Кнопка статуса заказа не отображается — заказ не подтверждён"