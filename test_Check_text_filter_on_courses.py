from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://obrazoval.ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

   # button_search = browser.find_element_by_class_name('l-search__button.b-btn.absolute') --другая версия поиска
    button_search = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'l-search__button.b-btn.absolute'))
    )
    button_search.click()

    #Находим фильтры, для проверки редиректа страницы
    text_filter_elt = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/div[1]/main/div[3]/div/div[2]/div[2]/div[1]/div'))
    )

    text_filter = text_filter_elt.text
    print(text_filter + ' отображаются')
    assert 'Фильтры' == text_filter


finally:
    time.sleep(2)
    browser.close()
    time.sleep(1)
    browser.quit()