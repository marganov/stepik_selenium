from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

def calculate_sum(x, y):
    return x + y

number_1 = int(browser.find_element(By.ID, "num1").text)
number_2 = int(browser.find_element(By.ID, "num2").text)

answer = calculate_sum(number_1, number_2)

select = Select(browser.find_element(By.TAG_NAME, "select"))

input = select.select_by_value(str(answer))

button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

time.sleep(10)
browser.quit()