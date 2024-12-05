from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")  # Поле ввода имени
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")  # Поле ввода фамилии
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")  # Поле ввода города
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")  # Поле ввода страны
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")  # Кнопка отправки формы
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()
