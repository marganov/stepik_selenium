from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    x = browser.find_element(By.ID, "input_value").text

    x_input = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(x_input)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input_check = browser.find_element(By.ID, "robotCheckbox")
    input_check.click()

    input_radio = browser.find_element(By.ID, "robotsRule")
    input_radio.click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()