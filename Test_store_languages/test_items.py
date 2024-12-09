import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_add_to_cart_button(browser, link, user_language):
    """
    Тест проверяет наличие кнопки "Добавить в корзину" на странице товара.
    """
    # Устанавливаем язык интерфейса через параметр `user_language`
    browser.get(f"{link}?lang={user_language}")
    
    # Устанавливаем явное ожидание появления кнопки
    try:
        add_to_cart_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#add_to_basket_form > button"))
        )
        # Проверяем, что кнопка видима
        assert add_to_cart_button.is_displayed(), "Кнопка 'Добавить в корзину' не отображается!"
    except Exception:
        pytest.fail("Кнопка 'Добавить в корзину' не найдена на странице.")
