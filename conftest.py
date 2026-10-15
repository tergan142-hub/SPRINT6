import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import URLs
from locators.main_page_locators import QuestionLocators


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(URLs.BASE_URL)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(QuestionLocators.Question_1))
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Автоматически прикладывает скриншот к упавшим тестам."""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = getattr(item, "_request", None)
        if driver is not None:
            driver = driver.getfixturevalue("driver")
        else:
            try:
                driver = item.funcargs["driver"] if hasattr(item, "funcargs") else None
            except Exception:
                driver = None
        if driver is not None:
            try:
                png = driver.get_screenshot_as_png()
                allure.attach(png, name=f"screenshot_{item.name}", attachment_type=allure.attachment_type.PNG,)
            except Exception:
                pass
            