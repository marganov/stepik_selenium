from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'my.txt')

try:
    input_firstName = browser.find_element(By.NAME, "firstname")
    input_firstName.send_keys("Boroda")

    input_lastName = browser.find_element(By.NAME, "lastname")
    input_lastName.send_keys("Lee")

    input_mail = browser.find_element(By.NAME, "email")
    input_mail.send_keys("boroda@mail.ru")

    file_upload = browser.find_element(By.ID, "file")
    file_upload.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()


finally:
    time.sleep(10)
    browser.quit()