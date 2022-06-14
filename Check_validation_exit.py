from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://obrazoval.ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Ищем кнопку "Войти" на главной странице
    button_exit = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'b-btn.b-header__login_button'))
    )
    button_exit.click()

    #Вводим значение в поле ввода
    button_enter = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'b-input__field.full-width'))
    )
    button_enter.send_keys("1231231")

    #Кликаем "Войти"
    button_enter_click = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'b-btn.b-user__auth-submit'))
    )
    button_enter_click.click()





finally:
    time.sleep(2)
    browser.close()
    time.sleep(1)
    browser.quit()