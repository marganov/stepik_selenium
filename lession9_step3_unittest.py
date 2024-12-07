from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestRegistration(unittest.TestCase):
    def test_registration_1(self):
        print("Тест 1 выполняется")
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
            input1.send_keys("Anastasiya")
            input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
            input2.send_keys("Begunova")
            input3 = browser.find_element(By.XPATH, "//input[@class='form-control third']")
            input3.send_keys("ABmail@mail.ru")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error login")

        finally:
            browser.quit()

    def test_registration_2(self):
        print("Тест 2 выполняется")
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.XPATH, "//input[@class='form-control first' and @required]")
            input1.send_keys("Anastasiya")
            input2 = browser.find_element(By.XPATH, "//input[@class='form-control second' and @required]")
            input2.send_keys("Begunova")
            input3 = browser.find_element(By.XPATH, "//input[@class='form-control third']")
            input3.send_keys("ABmail@mail.ru")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Error login")

        finally:
            browser.quit()

if __name__ == "__main__":
    unittest.main()