import allure
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Закрыть баннер cookie-согласия")
    def close_cookie_banner(self):
        try:
            btn = self.wait.until(EC.element_to_be_clickable((MainPageLocators.Cookie_banner)))
            btn.click()
        except TimeoutException:
            pass

    def find_element_with_wait(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_element_with_wait(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ждать, пока URL станет равным ожидаемому")
    def wait_for_url(self, expected_url, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda d: d.current_url == expected_url)

    @allure.step("Перейти по URL и ждать загрузки")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Дождаться появления новой вкладки и вернуть её handle")
    def wait_for_new_window(self, original_handle, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        def condition(d):
            handles = d.window_handles
            return len(handles) > 1 and any(h != original_handle for h in handles)
        wait.until(condition)
        for h in self.driver.window_handles:
            if h != original_handle:
                return h
        raise TimeoutException("Новая вкладка не появилась")

    @allure.step("Переключиться на вкладку по handle")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    def scroll_to_element(self, locator):
        el = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", el)
        return el

    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step("Кликнуть, дождаться новой вкладки, переключиться и проверить URL")
    def click_and_wait_for_new_tab(self, locator, expected_url):
        original_handle = self.driver.current_window_handle
        self.click_element_with_wait(locator)
        new_handle = self.wait_for_new_window(original_handle)
        self.switch_to_window(new_handle)
        self.wait_for_url(expected_url)