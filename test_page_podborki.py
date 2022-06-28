#Тест не готов!!!!!

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

link = "https://obrazoval.ru/"
browser = webdriver.Chrome()
browser.get(link)

try:
    button_service = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'b-header-menu__btn.q-mr-md.text-center.cursor-pointer'))
    ).click()
    alert = browser.switch_to.
    button_compilations = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'b-ui-dropdown-menu__description'))
    ).click()
    time.sleep(3)



finally:
    time.sleep(3)
    browser.close()
    time.sleep(1)
    browser.quit()