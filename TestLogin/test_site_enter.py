import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import math
import time

# Фикстура для браузера
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_argument("--ignore-certificate-errors")  # Игнорировать ошибки сертификатов
    options.add_argument("--disable-extensions")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

url = ["https://stepik.org/lesson/236897/step/1"]

@pytest.mark.parametrize('link', url)
def test_alien_feedback(browser, link):
    # Открываем страницу
    browser.get(link)
    time.sleep(20)