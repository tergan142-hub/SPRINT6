import allure
from pages.base_page import BasePage
from locators.main_page_locators import QuestionLocators, MainPageOrderButtonLocators, MainPageLocators
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
        self.click_element_with_wait(MainPageOrderButtonLocators.Order_button_first)

    @allure.step("Скроллить к кнопке «Заказать» (нижний блок)")
    def scroll_to_order_button_second(self):
        self.scroll_to_element(MainPageOrderButtonLocators.Order_button_second)

    @allure.step("Клик на кнопку «Заказать» (нижний блок)")
    def click_on_order_button_second(self):
        self.click_element_with_wait(MainPageOrderButtonLocators.Order_button_second)

    @allure.step("Клик на логотип Яндекс")
    def click_yandex_logo(self):
        self.scroll_to_element(self.locators.Yandex_button)
        self.click_element_with_wait(self.locators.Yandex_button)

    @allure.step("Перейти на Дзен через клик по логотипу Яндекса")
    def transition_to_Dzen(self):
        self.click_and_wait_for_new_tab(locator=MainPageLocators.Yandex_button, expected_url=URLs.DZEN_URL)

    @allure.step("Проверить, что мы на главной странице")
    def check_transition_to_main_page(self):
        self.find_element_with_wait(MainPageLocators.Text_on_main_page)