from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим элемент, содержащий значение x, и считываем его текст
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text  # Читаем значение x как строку

    # Вычисляем результат функции calc
    result = calc(x)
    
    #ищем и заполняем поле с примером
    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(result)

    input_2 = browser.find_element(By.ID, "robotCheckbox")
    input_2.click()

    input_3 = browser.find_element(By.ID, "robotsRule")
    input_3.click()

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    


finally:
    time.sleep(10)
    browser.quit()