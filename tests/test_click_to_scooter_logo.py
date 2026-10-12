import allure
from pages.main_page import MainPage

@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Переход на главную страницу при нажатии на логотип «Самокат»")
    @allure.story("Проверка, что клик по логотипу возвращает на главную")
    def test_click_to_scooter_logo(self, driver):
        main_page = MainPage(driver)

        with allure.step("Закрываем баннер cookie-согласия"):
            main_page.close_cookie_banner()

        with allure.step("Кликаем на логотип «Самокат»"):
            main_page.scroll_to_element(main_page.locators.Scooter_button)
            main_page.click_element_with_wait(main_page.locators.Scooter_button)

        with allure.step("Проверяем, что вернулись на главную страницу"):
            main_page.find_element_with_wait(main_page.locators.Text_on_main_page)

        assert True, "Логотип «Самокат» при клике возвращает на главную страницу"