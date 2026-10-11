import allure
import time
from pages.base_page import BasePage
from locators.main_page_locators import OrderButton, MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urls import URLs


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def scroll_to_question(self, question_locator):
        self.scroll_to_element(question_locator)

    def click_question(self, question_locator):
        self.click_element_with_wait(question_locator)

    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)

    @allure.step("Открыть текст вопроса и получить текст ответа")
    def open_question_and_get_answer(self, question_locator, answer_locator):
        self.scroll_to_question(question_locator)
        self.click_question(question_locator)
        return self.get_answer_text(answer_locator)


    def click_on_order_button_first(self):
        self.click_element_with_wait(OrderButton.Order_button_first)

    def scroll_to_order_button_second(self):
        self.scroll_to_element(OrderButton.Order_button_second)

    def click_on_order_button_second(self):
        self.click_element_with_wait(OrderButton.Order_button_second)

    def click_yandex_logo(self):
        self.click_element_with_wait(MainPageLocators.Yandex_button)

    def click_scooter_logo(self):
        self.click_element_with_wait(MainPageLocators.Scooter_button)

    @allure.step("Кликнуть на логотип Яндекс и перейти на Дзен")
    def transition_to_Dzen(self, timeout=15):
        # 1. Запоминаем, где мы сейчас
        original_window = self.driver.current_window_handle

        # 2. Кликаем на логотип
        self.click_element_with_wait(MainPageLocators.Yandex_button)

        # 3. Ждём, пока появится новая вкладка
        start_time = time.time()
        while time.time() - start_time < timeout:
            if len(self.driver.window_handles) > 1:
                break
            time.sleep(0.5)
        else:
            raise TimeoutException("Не появилась новая вкладка после клика на логотип")

        # 4. Переключаемся на новую вкладку
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break
        DZEN_PART = URLs.DZEN_PART
        
        # 5. Ждём, чтобы в адресной строке появилось "dzen.ru"
        start_time = time.time()
        while time.time() - start_time < timeout:
            current_url = self.driver.current_url
            if DZEN_PART in current_url:
                return
            time.sleep(0.5)

        raise TimeoutException(f"Не дождались Дзена. Сейчас в браузере: {current_url}")


    def check_transition_to_main_page(self):
        element = self.wait.until(EC.visibility_of_element_located(MainPageLocators.Text_on_main_page))
        return element
    