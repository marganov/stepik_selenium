from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")

    x_element_attrib = x_element.get_attribute("valuex")

    answer_is = calc(x_element_attrib)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(answer_is)

    input_2 = browser.find_element(By.ID, "robotCheckbox")
    input_2.click()

    input_3 = browser.find_element(By.ID, "robotsRule")
    input_3.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
