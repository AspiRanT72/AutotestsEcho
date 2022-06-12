from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

link = "https://obrazoval.ru/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

   # button_search = browser.find_element_by_class_name('l-search__button.b-btn.absolute') --другая версия поиска
    button_search = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'l-search__button.b-btn.absolute'))
    )
    button_search.click()

    new_link = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'https://obrazoval.ru/courses'))
    )

    print('new_link')
    assert 'Link is good' == new_link

    text_filter_elt = browser.find_element_by_class_name('flex.items-center')
    text_filter =  text_filter_elt.text
    print('text_filter')
    assert 'Фильтры1' == text_filter


finally:
    time.sleep(5)
    browser.close()
    time.sleep(1)
    browser.quit()