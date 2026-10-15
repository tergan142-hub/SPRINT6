import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Переход на главную страницу при нажатии на логотип «Самокат»")
    @allure.story("Проверка, что клик по логотипу возвращает на главную")
    def test_click_to_scooter_logo(self, driver):
        main_page = MainPage(driver)
        locators = MainPageLocators()

        with allure.step("Закрываем баннер cookie-согласия, если он есть"):
            main_page.close_cookie_banner()

        with allure.step("Кликаем на логотип «Самокат»"):
            main_page.scroll_to_element(locators.Scooter_button)
            main_page.click_element_with_wait(locators.Scooter_button)

        with allure.step("Проверяем, что мы действительно на главной странице"):
            header_element = main_page.find_element_with_wait(locators.Text_on_main_page)
            actual_text = header_element.text

            expected_text = "Самокат на пару дней"

            assert expected_text in actual_text, (f"Неверный заголовок на главной: ожидали '{expected_text}', " f"а получили '{actual_text}'")