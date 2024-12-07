from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.parametrize("link", [
    "http://suninjuly.github.io/registration1.html",
    "http://suninjuly.github.io/registration2.html"
])
def test_registration(link):
    print(f"Тест выполняется для ссылки: {link}")
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
    input1.send_keys("Anastasiya")
    input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
    input2.send_keys("Begunova")
    input3 = browser.find_element(By.XPATH, "//input[@class='form-control third']")
    input3.send_keys("ABmail@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Находим элемент с текстом
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # Проверяем, что текст совпадает
    assert welcome_text == "Congratulations! You have successfully registered!"

    # Закрываем браузер после теста
    browser.quit()