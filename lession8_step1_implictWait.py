'''
.implicitly_wait() метод, который позволяет задать ожидание, задаётся
при инициализации драйвера, применяется ко вем тестам в скрипте


from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

NoSuchElementException - элемент не найден
StaleElementReferenceException - э.найден, но был скрыт скриптом
ElementNotVisibleException. - э.найден, но пользователь не сможет с ним
взаимодействовать
'''
