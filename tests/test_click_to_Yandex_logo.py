import allure
from pages.main_page import MainPage

@allure.feature("Переход на главную страницу Дзен при нажатии на логотип 'Яндекс'")
@allure.story("Проверка перехода на главную страницу Дзен")
def test_click_to_Yandex_logo(driver):
    main_page = MainPage(driver)

    with allure.step("Этап 1. Подготовка страницы и переход по логотипу 'Яндекс'"):
        main_page.close_cookie_banner()
        main_page.transition_to_Dzen()