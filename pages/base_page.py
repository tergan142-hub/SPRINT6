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
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".App_CookieConsent button")))
            btn.click()
        except TimeoutException:
            pass

    def find_element_with_wait(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_element_with_wait(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def wait_for_url(self, url, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda d: d.current_url == url)

    def wait_for_new_window(self, original_handle, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        def condition(driver):
            handles = driver.window_handles
            return len(handles) > 1 and any(h != original_handle for h in handles)
        wait.until(condition)
        for h in self.driver.window_handles:
            if h != original_handle:
                return h
        raise TimeoutException("Новая вкладка не появилась")

    def scroll_to_element(self, locator):
        el = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", el)
        return el

    def get_text(self, locator):
        return self.find_element_with_wait(locator).text
    