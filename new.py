from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
link = "https://obrazoval.ru/"
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()
try:
    element = browser.find_element(By.XPATH, "//button[@class ='b-btn b-header__login_button' and text() = ' Войти ']")
    WebDriverWait(browser, 10).until(EC.visibility_of(element))
    element.click()
    time.sleep(3)
    element_login = browser.find_element(By.XPATH, "//input[@placeholder ='Email или телефон']")
    WebDriverWait(browser, 10).until(EC.visibility_of(element_login))
    element_login.send_keys('123')
finally:
    time.sleep(3)
    browser.close()
    time.sleep(1)
    browser.quit()