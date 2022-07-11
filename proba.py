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
#browser.maximize_window()


button_search = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'l-search__button.b-btn.absolute'))
).click()
time.sleep(10)
#Ищем первое объявление для сравнения и тыкаем его
button_compare1 = browser.find_elements(By.XPATH, '//div[@class="b-courses-save__icon"]')[1].click()

# element_login = browser.find_element((By.XPATH, '//div[@class="b-courses-save__icon"]')[1])
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable(element_login))
# element_login.click()

#Ищем первое объявление для сравнения и тыкаем его
button_compare2 = browser.find_elements(By.XPATH, '//div[@class="b-courses-save__icon"]')[4].click()


time.sleep(3)
browser.close()
time.sleep(1)
browser.quit()

if __name__=='__main__':
    main()