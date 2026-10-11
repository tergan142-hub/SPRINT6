import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Закрыть баннер cookie-согласия")
    def close_cookie_banner(self):
        locator = (By.CSS_SELECTOR, ".App_CookieConsent__1yUIN")
        try:
            close_btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".App_CookieConsent__1yUIN button"))
            )
            close_btn.click()
        except Exception:
            self.wait.until(EC.invisibility_of_element_located(locator))

    def find_element_with_wait(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_element_with_wait(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def is_url_opened(self, url):
        try:
            self.wait.until(EC.url_to_be(url))
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_text(self, locator):
        return self.find_element_with_wait(locator).text
    