'''
для переключения на вкладку
browser.switch_to.window(window_name)

window_handles вернет массив с вкладками
выбираем вторую вкладку
new_window = browser.window_handles[1]

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    button_first = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    button_first.click()

    my_window = browser.window_handles[1]
    browser.switch_to.window(my_window)

    x = browser.find_element(By.ID, "input_value").text

    x_input = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(x_input)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()