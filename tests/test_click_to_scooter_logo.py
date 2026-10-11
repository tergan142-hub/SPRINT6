import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature("Переход на главную страницу при нажатии на логотип 'Самокат'")
@allure.story("Проверка перехода на главную страницу")
def test_click_to_scooter_logo(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    with allure.step("Этап 1. Подготовка страницы и переход по логотипу 'Самокат'"):
        main_page.close_cookie_banner()
        main_page.click_on_order_button_first()
        order_page.click_on_scooter_logo()
        main_page.check_transition_to_main_page()
        