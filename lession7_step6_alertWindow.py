'''Для alert с одним OK
alert = browser.switch_to.alert
alert.accept()

Получить текст из alert, свойство text объекта alert:
alert = browser.switch_to.alert
alert_text = alert.text

alert с выбором
confirm = browser.switch_to.alert
что бы принять:
confirm.accept()
что бы отказаться:
confirm.dismiss()

alert с полем для ввода
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    button_first = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button_first.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value").text

    x_input = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(x_input)

    button_second = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button_second.click()

finally:
    time.sleep(10)
    browser.quit()