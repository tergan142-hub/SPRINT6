import allure
from datetime import date, timedelta
from selenium.webdriver.common.keys import Keys
from pages.main_page import MainPage
from locators.order_page_locators import OrderLocatorsFirst, OrderLocatorsSecond
from data_generators import generate_unique_name, generate_unique_last_name, generate_unique_phone_number, generate_address

class OrderPage(MainPage):

    @allure.step("Поиск и заполнение поля Имя") 
    def fill_name(self, name=None):
        name = name or generate_unique_name()
        el = self.find_element_with_wait(OrderLocatorsFirst.Name_locator)
        el.clear()
        el.send_keys(name)

    @allure.step("Поиск и заполенение поля Фамилия") 
    def fill_last_name(self, last_name=None):
        last_name = last_name or generate_unique_last_name()
        el = self.find_element_with_wait(OrderLocatorsFirst.Last_Name_locator)
        el.clear()
        el.send_keys(last_name)

    @allure.step("Поиск и заполенение поля Адрес") 
    def fill_address(self, address=None):
        address = address or generate_address()
        el = self.find_element_with_wait(OrderLocatorsFirst.Address_locator)
        el.clear()
        el.send_keys(address)

    @allure.step("Поиск и заполнение поля Станция Метро") 
    def select_metro_station(self, station_locator=OrderLocatorsFirst.Sokolniki_station_locator):
        self.click_element_with_wait(OrderLocatorsFirst.Metro_station_locator)
        self.click_element_with_wait(station_locator)

    @allure.step("Поис и заполенение поля Номер Сотового") 
    def fill_phone(self, phone=None):
        phone = phone or generate_unique_phone_number()
        el = self.find_element_with_wait(OrderLocatorsFirst.Phone_number_locator)
        el.clear()
        el.send_keys(phone)

    @allure.step("Нажатие на кнопку") 
    def click_next_button(self):
        self.click_element_with_wait(OrderLocatorsFirst.Next_button)

    @allure.step("Поиск и заполнение поля Выбор Даты") 
    def set_rental_date(self, days_offset=1):
        el = self.find_element_with_wait(OrderLocatorsSecond.Date_locator)
        el.click()
        target_date = (date.today() + timedelta(days=days_offset)).strftime("%d.%m.%Y")
        el.clear()
        el.send_keys(target_date)
        el.send_keys(Keys.ENTER)

    @allure.step("Поиск и заполнение поля Срок Аренды") 
    def set_rental_period(self, option_locator=OrderLocatorsSecond.Quantity_1_day):
        self.click_element_with_wait(OrderLocatorsSecond.Quantity_arrow)
        self.click_element_with_wait(option_locator)

    @allure.step("Поиск и заполнение поля Цвет Самоката") 
    def select_scooter_color(self, color_locator=OrderLocatorsSecond.Scooter_color_black):
        self.click_element_with_wait(color_locator)

    @allure.step("Поиск и заполнение поля Комментарий") 
    def fill_comment(self, comment="Тестовый комментарий для курьера"):
        el = self.find_element_with_wait(OrderLocatorsSecond.Comment_for_courier)
        el.clear()
        el.send_keys(comment)

    @allure.step("Нажатие кнопки") 
    def submit_order(self):
        self.click_element_with_wait(OrderLocatorsSecond.Order_button)

    @allure.step("Подтверждение заказа") 
    def confirm_order(self):
        self.find_element_with_wait(OrderLocatorsSecond.Order_question)
        self.click_element_with_wait(OrderLocatorsSecond.Yes_button)

    @allure.step("Проверить, что кнопка статуса заказа видна")
    def verify_status_button_visible(self):
            self.find_element_with_wait(self.locators.Status_button)
            return True 

    @allure.step("Нахождение номера заказа") 
    def verify_order_number_present(self):
        self.find_element_with_wait(OrderLocatorsSecond.Order_number)