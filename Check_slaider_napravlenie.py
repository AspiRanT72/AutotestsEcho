from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "https://obrazoval.ru/"

browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

try:


   # button_search = browser.find_element_by_class_name('l-search__button.b-btn.absolute') --другая версия поиска
    button_search = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'l-search__button.b-btn.absolute'))
    )
    button_search.click()

    # проверяем наличие слайдера с "Программирование"
    programmirovanie_elt = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="q-app"]/div/div[1]/main/div[2]/div/div/div/div[1]/div/span/a'))
    )
    programmirovanie = programmirovanie_elt.text
    assert 'Программирование' == programmirovanie
    print(programmirovanie + ' is ok')



    # Проверяем наличие слайдера с "Управление"
    upravlenie_elt = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="q-app"]/div/div[1]/main/div[2]/div/div/div/div[2]/div/span/a'))
    )
    upravlenie = upravlenie_elt.text
    assert 'Управление' == upravlenie
    print(upravlenie + ' is ok')


    # Проверяем наличие слайдера с "Маркетинг"
    marketing_elt = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="q-app"]/div/div[1]/main/div[2]/div/div/div/div[3]/div/span'))
    )
    marketing = marketing_elt.text
    assert 'Маркетинг' == marketing
    print(marketing + ' is ok')


    # Проверяем наличие слайдера с "Дизайн и создание контента"
    dick_elt = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="q-app"]/div/div[1]/main/div[2]/div/div/div/div[4]/div/span/a'))
    )
    dick = dick_elt.text
    assert 'Дизайн и создание контента' == dick
    print(dick + ' is ok')

    # Проверяем наличие слайдера с "Аналитика"
    analytics_elt = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="q-app"]/div/div[1]/main/div[2]/div/div/div/div[5]/div/span/a'))
    )
    analytics = analytics_elt.text
    assert 'Аналитика' == analytics
    print(analytics + ' is ok')

    #Листаем слайдер и проверяем кнопки
    swiper_button_next = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="q-app"]/div/div[1]/main/div[1]/div[3]/div[2]/div[2]'))
    )
    swiper_button_next.click()


    # Проверяем наличие слайдера с "Общие навыки"
    skils_elt = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="q-app"]/div/div[1]/main/div[2]/div/div/div/div[6]/div/span/a'))
    )
    skils = skils_elt.text
    assert 'Общие навыки' == skils
    print(skils + ' is ok')

    # Проверяем наличие слайдера с "Творчество"
    creation_elt = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="q-app"]/div/div[1]/main/div[2]/div/div/div/div[7]/div/span/a'))
    )
    creation = creation_elt.text
    assert 'Творчество' == creation
    print(creation + ' is ok')

    # Проверяем наличие слайдера с "Профессиональное"
    proffi_elt = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="q-app"]/div/div[1]/main/div[2]/div/div/div/div[8]/div/span/a'))
    )
    proffi = proffi_elt.text
    assert 'Профессиональное' == proffi
    print(proffi + ' is ok')

    # Проверяем наличие слайдера с "Профессиональное"
    anylang_elt = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="q-app"]/div/div[1]/main/div[2]/div/div/div/div[9]/div/span/a'))
    )
    anylang = anylang_elt.text
    assert 'Иностранные языки' == anylang
    print(anylang + ' is ok')





finally:
    time.sleep(3)
    browser.close()
    time.sleep(1)
    browser.quit()