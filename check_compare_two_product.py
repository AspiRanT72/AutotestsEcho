from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#options = webdriver.ChromeOptions
#options.headless = True
link = "https://obrazoval.ru/"

browser = webdriver.Chrome()
browser.get(link)
#browser.maximize_window()


try:
    button_search = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'l-search__button.b-btn.absolute'))
    ).click()
    #Ищем первое объявление для сравнения и тыкаем его
    button_compare1 = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/div[1]/main/div[3]/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]'))
    ).click()

    #Ищем второе объявление для сравнения и тыкаем его
    button_compare2 = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/div[1]/main/div[3]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]'))
    ).click()
    #Переходим на страницу сравнения курсов
    button_head_compare = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/header/div/div/div[4]/div/a[1]/div'))
    ).click()

    header_compare = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="q-app"]/div/div[1]/main/div[1]/h1'))
    )
    header_compare_elt = header_compare.text
    assert 'Сравнение курсов' == header_compare_elt
    print (header_compare_elt + ' is ok')





finally:
    time.sleep(3)
    browser.close()
    time.sleep(1)
    browser.quit()

