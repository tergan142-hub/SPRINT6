import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import QuestionLocators, AnswerLocators

Questions_Answers = [
    (QuestionLocators.Question_1, AnswerLocators.Answer_1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (QuestionLocators.Question_2, AnswerLocators.Answer_2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (QuestionLocators.Question_3, AnswerLocators.Answer_3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (QuestionLocators.Question_4, AnswerLocators.Answer_4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (QuestionLocators.Question_5, AnswerLocators.Answer_5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (QuestionLocators.Question_6, AnswerLocators.Answer_6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (QuestionLocators.Question_7, AnswerLocators.Answer_7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (QuestionLocators.Question_8, AnswerLocators.Answer_8, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
]

@allure.title("При клике на вопрос должен отобразиться корректный ответ")
@allure.story("Раскрытие вопроса и проверка текста ответа")
@allure.feature("Вопросы и ответы")
class TestQuestionAnswer:
    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", Questions_Answers, ids=[f'question_{i}' for i in range(1, 9)])
    def test_question_opens_correct_answer(self, driver, question_locator, answer_locator, expected_text):
        main_page = MainPage(driver)
        with allure.step("Шаг 1. Открыть вопрос на главной странице и получить текст ответа"):
            actual_text = main_page.open_question_and_get_answer(question_locator, answer_locator)
        with allure.step(f"Шаг 2. Проверить, что ответ совпадает с ожидаемым текстом"):
            assert actual_text == expected_text
            