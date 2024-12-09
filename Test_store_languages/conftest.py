# Импортируем необходимые модули из pytest и Selenium
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Добавляем опции командной строки для pytest
def pytest_addoption(parser):
    """
    Добавляет опции командной строки '--browser_name' для выбора браузера 
    и '--language' для задания языка интерфейса.
    """
    # Опция для выбора браузера (Chrome или Firefox)
    parser.addoption(
        "--browser_name", 
        action="store", 
        default="chrome",  # Значение по умолчанию — "chrome"
        help="Choose browser: chrome or firefox"  # Подсказка для пользователя
    )
    # Опция для выбора языка
    parser.addoption(
        "--language", 
        action="store", 
        default="en",  # Значение по умолчанию — английский язык
        help="Choose language: en, ru, fr, etc."  # Подсказка для пользователя
    )

# Фикстура для языка пользователя
@pytest.fixture(scope="function")
def user_language(request):
    """
    Получает значение языка интерфейса из параметра командной строки '--language'.
    """
    return request.config.getoption("--language")

# Фикстура для инициализации и завершения работы браузера
@pytest.fixture(scope="function")
def browser(request, user_language):
    """
    Фикстура для создания экземпляра браузера с учетом выбранного языка интерфейса.
    Браузер выбирается на основе параметра '--browser_name'.
    """
    # Получаем значение параметра '--browser_name' из командной строки
    browser_name = request.config.getoption("browser_name")
    
    # Инициализируем переменную browser как None
    browser = None

    # Проверяем значение параметра и создаем соответствующий браузер
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")  # Логируем выбор браузера
        
        # Создаем объект опций для Chrome
        options = Options()
        # Добавляем настройку для языка интерфейса
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        # Создаем экземпляр Chrome с заданными опциями
        browser = webdriver.Chrome(options=options)
    
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")  # Логируем выбор браузера
        
        # Создаем профиль для Firefox
        fp = webdriver.FirefoxProfile()
        # Устанавливаем предпочитаемый язык интерфейса
        fp.set_preference("intl.accept_languages", user_language)
        # Создаем экземпляр Firefox с заданным профилем
        browser = webdriver.Firefox(firefox_profile=fp)
    
    else:
        # Если параметр указан неверно, вызываем исключение с сообщением об ошибке
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    # Передаем управление тесту, возвращая объект браузера
    yield browser

    # Завершаем работу браузера после выполнения теста
    print("\nquit browser...")
    browser.quit()
