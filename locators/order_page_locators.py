import allure
from selenium.webdriver.common.by import By

@allure.step("Создаем локаторы на странице заказа самоката")
class OrderLocatorsFirst:
    Name_locator = [By.XPATH, "//input[@placeholder='* Имя']"]
    Last_Name_locator = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    Address_locator = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    Metro_station_locator = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    Sokolniki_station_locator = [By.XPATH, "//div[text()='Сокольники' and @class='Order_Text__2broi']"]
    Komsomolskya_station_locator = [By.XPATH, "//div[text()='Комсомольская' and @class='Order_Text__2broi']"]
    Phone_number_locator = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    Next_button = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

class OrderLocatorsSecond:
    Date_locator = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    Quantity_arrow = [By.XPATH, "//span[@class='Dropdown-arrow']"]
    Quantity_1_day = [By.XPATH, "//div[text()='сутки' and @class='Dropdown-option']"]
    Quantity_5_days = [By.XPATH, "//div[text()='пятеро суток' and @class='Dropdown-option']"]
    Scooter_color_black = [By.XPATH, "//label[.//input[@id='black']]"]
    Scooter_color_grey = [By.XPATH, "//label[.//input[@id='grey']]"]
    Comment_for_courier = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    Order_button = [By.XPATH, "//button[text()='Заказать' and @class='Button_Button__ra12g Button_Middle__1CSJM']"]
    Order_question = [By.XPATH, "//div[text()='Хотите оформить заказ?' and @class='Order_ModalHeader__3FDaJ']"]
    Yes_button = [By.XPATH, "//button[text()='Да' and @class='Button_Button__ra12g Button_Middle__1CSJM']"]
    Status_button = [By.XPATH, "//button[text()='Посмотреть статус' and @class='Button_Button__ra12g Button_Middle__1CSJM']"]
    Order_cancellation_button = [By.XPATH, "//button[normalize-space()='Отменить заказ']"]
    Order_number = [By.XPATH, "//div[contains(text(), 'Номер заказа') and @class='Order_Text__2broi']"]
    View_the_status_button = [By.XPATH, "//button[text()='Посмотреть статус' and @class='Button_Button__ra12g Button_Middle__1CSJM']"]