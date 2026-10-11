import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Оформление заказа самоката - Вариант 1")
@allure.story("Проверка оформления заказа и получение номера заказа")
def test_scooter_order_2(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    with allure.step("Этап 1. Подготовка страницы и переход к форме заказа"):
        main_page.close_cookie_banner()
        main_page.scroll_to_order_button_second()
        main_page.click_on_order_button_second()

    with allure.step("Этап 2. Заполнение данных для заказа"):
        order_page.name_field()
        order_page.last_name_field()
        order_page.address_field()
        order_page.metro_station()
        order_page.phone_number()
        order_page.next_button()
    with allure.step("Этап 3. Выбор параметров аренды"):
        order_page.next_page_1()
        order_page.date_field_second()
        order_page.rental_period_second()
        order_page.color_choice_second()
        order_page.comment_for_courier()
        order_page.order_button()

    with allure.step("Этап 4. Подтверждение заказа и проверка статуса"):
        order_page.next_field()
        order_page.yes_button()
        order_page.check_status()
        