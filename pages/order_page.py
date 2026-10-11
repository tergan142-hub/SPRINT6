import random
from faker import Faker
from pages.main_page import MainPage
from locators.order_page_locators import OrderLocatorsFirst, OrderLocatorsSecond
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, timedelta
from selenium.webdriver.common.keys import Keys
from locators.main_page_locators import MainPageLocators



fake = Faker('ru_RU')

class UniqueData:
    @staticmethod
    def generate_unique_name(min_length=6):
        return fake.first_name()

    @staticmethod
    def generate_unique_last_name(min_length=6):
        return fake.last_name()

    @staticmethod
    def generate_unique_phone_number():
        digits = ''.join(random.choices('0123456789', k=10))
        phone_number = '8' + digits
        return phone_number
    

class OrderPage(MainPage):
    def name_field(self):
        name = UniqueData.generate_unique_name()
        element = self.find_element_with_wait(OrderLocatorsFirst.Name_locator)
        element.clear()
        element.send_keys(name)

    def last_name_field(self):
        last_name = UniqueData.generate_unique_last_name()
        element = self.find_element_with_wait(OrderLocatorsFirst.Last_Name_locator)
        element.clear()
        element.send_keys(last_name)

    def address_field(self):
        address_name = "ул. Какжеэтосложно, 777"
        element = self.find_element_with_wait(OrderLocatorsFirst.Address_locator)
        element.clear()
        element.send_keys(address_name)

    def metro_station(self):
        self.click_element_with_wait(OrderLocatorsFirst.Metro_station_locator)
        self.click_element_with_wait(OrderLocatorsFirst.Sokolniki_station_locator)

    def phone_number(self):
        phone_number = UniqueData.generate_unique_phone_number()
        element = self.find_element_with_wait(OrderLocatorsFirst.Phone_number_locator)
        element.clear()
        element.send_keys(phone_number)

    def next_button(self):
        self.click_element_with_wait(OrderLocatorsFirst.Next_button)

    def next_page_1(self):        
        self.wait.until(EC.visibility_of_element_located(OrderLocatorsSecond.Scooter_color_black))
        
    def date_field(self):
        date_input = self.find_element_with_wait(OrderLocatorsSecond.Date_locator)
        date_input.click()
        tomorrow = (date.today() + timedelta(days=1)).strftime("%d.%m.%Y")
        date_input.clear()
        date_input.send_keys(tomorrow)
        date_input.send_keys(Keys.ENTER)

    def date_field_second(self):
        date_input = self.find_element_with_wait(OrderLocatorsSecond.Date_locator)
        date_input.click()
        tomorrow = (date.today() + timedelta(days=5)).strftime("%d.%m.%Y")
        date_input.clear()
        date_input.send_keys(tomorrow)
        date_input.send_keys(Keys.ENTER)

    def rental_period(self):
        self.click_element_with_wait(OrderLocatorsSecond.Quantity_arrow)
        self.click_element_with_wait(OrderLocatorsSecond.Quantity_1_day)

    def rental_period_second(self):
        self.click_element_with_wait(OrderLocatorsSecond.Quantity_arrow)
        self.click_element_with_wait(OrderLocatorsSecond.Quantity_5_days)

    def color_choice(self):
        self.click_element_with_wait(OrderLocatorsSecond.Scooter_color_black)

    def color_choice_second(self):
        self.click_element_with_wait(OrderLocatorsSecond.Scooter_color_grey)

    def comment_for_courier(self):
        comment = "Обожаю эти самокаты. Особенно когда, они сами катяться!"
        element = self.find_element_with_wait(OrderLocatorsSecond.Comment_for_courier)
        element.clear()
        element.send_keys(comment)

    def order_button(self):
        self.click_element_with_wait(OrderLocatorsSecond.Order_button)

    def next_field(self):        
        self.wait.until(EC.visibility_of_element_located(OrderLocatorsSecond.Order_question))
        
    def yes_button(self):
        self.click_element_with_wait(OrderLocatorsSecond.Yes_button)

    def check_status(self):
        element = self.wait.until(EC.element_to_be_clickable(OrderLocatorsSecond.Status_button))
        return element 

    def click_on_scooter_logo(self):
        self.click_element_with_wait(MainPageLocators.Scooter_button)
        