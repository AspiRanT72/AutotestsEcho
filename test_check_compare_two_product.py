from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from closed import vishel


#options = webdriver.ChromeOptions
#options.headless = True
link = "https://obrazoval.ru/"

browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()
browser.delete_all_cookies()


button_search = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'l-search__button.b-btn.absolute'))
).click()
#Ищем первое объявление для сравнения и тыкаем его
time.sleep(8)
button_compare1 = browser.find_elements(By.XPATH, '//div[@class="b-courses-save__icon"]')[1].click()
time.sleep(1)
#Ищем первое объявление для сравнения и тыкаем его
button_compare2 = browser.find_elements(By.XPATH, '//div[@class="b-courses-save__icon"]')[3].click()
time.sleep(1)
#Переходим на страницу сравнения курсов
button_head_compare = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/header/div/div/div[4]/div/a[1]/div'))
).click()
time.sleep(3)
#Проверяем h1 тег на странице
header_compare = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="q-app"]/div/div[1]/main/div[1]/h1'))
)
header_compare_elt = header_compare.text
assert 'Сравнение курсов' == header_compare_elt
print (header_compare_elt + ' is ok')

#Проверяем наличие тега "Курсы" и кликабельность ссылок
course = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="q-app"]/div/div[1]/main/div[1]/div/div[1]/div[1]/div'))
)
course1 = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/div[1]/main/div[1]/div/div[1]/div[2]'))
)
course2 = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/div[1]/main/div[1]/div/div[1]/div[2]'))
)
print("Курсы присутствуют и кликабельны")

#Проверяем тег название и клики ссылок
name = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="q-app"]/div/div[1]/main/div[1]/div/div[2]/div[1]/div'))
)
name1 = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/div[1]/main/div[1]/div/div[2]/div[2]/div/a'))
)
name2 = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="q-app"]/div/div[1]/main/div[1]/div/div[3]/div[3]/div/div'))
)
print("название курсов есть и кликабельны")

time.sleep(3)
browser.close()
time.sleep(1)
browser.quit()

if __name__=='__main__':
    main()

