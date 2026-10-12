import allure
from pages.base_page import BasePage
from locators.main_page_locators import QuestionLocators, OrderButton, MainPageLocators
from urls import URLs

class MainPage(BasePage):

    locators = MainPageLocators
    
    @allure.step("Открыть вопрос и получить текст ответа")
    def open_question_and_get_answer(self, question_locator, answer_locator):
        self.scroll_to_element(question_locator)
        self.click_element_with_wait(question_locator)
        return self.get_text(answer_locator)

    @allure.step("Клик на кнопку «Заказать» (верхний блок)")
    def click_on_order_button_first(self):
        self.click_element_with_wait(OrderButton.Order_button_first)

    @allure.step("Скроллить к кнопке «Заказать» (нижний блок)")
    def scroll_to_order_button_second(self):
        self.scroll_to_element(OrderButton.Order_button_second)

    @allure.step("Клик на кнопку «Заказать» (нижний блок)")
    def click_on_order_button_second(self):
        self.click_element_with_wait(OrderButton.Order_button_second)

    @allure.step("Клик на логотип Яндекс")
    def click_yandex_logo(self):
        self.click_element_with_wait(MainPageLocators.Yandex_button)

    @allure.step("Перейти на Дзен и дождаться загрузки")
    def transition_to_Dzen(self):
        original_handle = self.driver.current_window_handle
        self.click_yandex_logo()
        new_handle = self.wait_for_new_window(original_handle)
        self.driver.switch_to.window(new_handle)
        self.wait_for_url(URLs.DZEN_URL)

    @allure.step("Проверить, что мы на главной странице")
    def check_transition_to_main_page(self):
        self.find_element_with_wait(MainPageLocators.Text_on_main_page)