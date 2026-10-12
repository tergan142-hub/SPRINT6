import allure
from selenium.webdriver.common.by import By

class QuestionLocators:
    Question_1 = [By.XPATH, "//div[@id='accordion__heading-0']"]
    Question_2 = [By.XPATH, "//div[@id='accordion__heading-1']"]
    Question_3 = [By.XPATH, "//div[@id='accordion__heading-2']"]
    Question_4 = [By.XPATH, "//div[@id='accordion__heading-3']"]
    Question_5 = [By.XPATH, "//div[@id='accordion__heading-4']"]
    Question_6 = [By.XPATH, "//div[@id='accordion__heading-5']"]
    Question_7 = [By.XPATH, "//div[@id='accordion__heading-6']"]
    Question_8 = [By.XPATH, "//div[@id='accordion__heading-7']"]

class AnswerLocators:
    Answer_1 = [By.XPATH, "//div[@id='accordion__panel-0']"]
    Answer_2 = [By.XPATH, "//div[@id='accordion__panel-1']"]
    Answer_3 = [By.XPATH, "//div[@id='accordion__panel-2']"]
    Answer_4 = [By.XPATH, "//div[@id='accordion__panel-3']"]
    Answer_5 = [By.XPATH, "//div[@id='accordion__panel-4']"]
    Answer_6 = [By.XPATH, "//div[@id='accordion__panel-5']"]
    Answer_7 = [By.XPATH, "//div[@id='accordion__panel-6']"]
    Answer_8 = [By.XPATH, "//div[@id='accordion__panel-7']"]

class OrderButton:
    Order_button_first = [By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']"]
    Order_button_second = [By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']"]


class MainPageLocators:
    Scooter_button = [By.XPATH, "//img[@alt='Scooter']"]
    Yandex_button = [By.XPATH, "//img[@alt='Yandex']"]
    Text_on_main_page = [By.XPATH, "//div[contains(@class, 'Home_Header')]"]
