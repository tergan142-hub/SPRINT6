import allure
from pages.main_page import MainPage
from urls import URLs

@allure.feature("Навигация и переходы между доменами")
class TestYandexLogoTransition:

    @allure.title("Клик по Яндекс‑логотипу открывает Дзен в новой вкладке")
    @allure.story("Проверка перехода на dzen.ru при клике на логотип Яндекса")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)

        with allure.step("Закрываем баннер cookie-согласия"):
            main_page.close_cookie_banner()

        with allure.step("Запоминаем текущую вкладку"):
            original_handle = driver.current_window_handle

        with allure.step("Кликаем по Яндекс‑логотипу"):
            main_page.scroll_to_element(main_page.locators.Yandex_button)
            main_page.click_element_with_wait(main_page.locators.Yandex_button)

        with allure.step("Ждём появления новой вкладки"):
            new_handle = main_page.wait_for_new_window(original_handle)
            driver.switch_to.window(new_handle)

        with allure.step("Ждём загрузки страницы Дзена"):
            main_page.wait_for_url(URLs.DZEN_URL)

        assert driver.current_url.startswith("https://dzen.ru"), "Переход на Дзен не произошёл или URL неверный"