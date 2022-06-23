from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions
options.headless = True
link = "https://obrazoval.ru/"

browser = webdriver.Chrome()
browser.get(link)
#browser.maximize_window()


try:
    button_search = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'l-search__button.b-btn.absolute'))
    )
    button_search.click()

    button_compare1 = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/div[1]/main/div[3]/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]'))
    )
    button_compare1.click()







finally:
    time.sleep(3)
    browser.close()
    time.sleep(1)
    browser.quit()

