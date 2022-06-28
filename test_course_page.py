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
    button_course = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/header/div/div/div[2]/button/span'))
    ).click()
    time.sleep(5)
    button_compilations = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div[1]/a/span/span[2]'))
    ).click()

    time.sleep(3)



finally:
    time.sleep(3)
    browser.close()
    time.sleep(1)
    browser.quit()