from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
link = 'https://obrazoval.ru/courses'
browser = webdriver.Chrome()
browser.get(link)
rating = browser.find_elements(By.CLASS_NAME,
                               'inline-md-block.cursor-pointer.l-sort__item.q-mr-xs.q-mr-lg-sm')[3]
rating.click()
time.sleep(2)
x1 = browser.find_elements(By.XPATH, '//span[@class ="b-reviews-count"]')[1].text
x2 = browser.find_elements(By.XPATH, '//span[@class ="b-reviews-count"]')[2].text
x3 = browser.find_elements(By.XPATH, '//span[@class ="b-reviews-count"]')[3].text
x4 = browser.find_elements(By.XPATH, '//span[@class ="b-reviews-count"]')[4]
i=x4.text
actions = ActionChains(browser)
actions.move_to_element(x4)
actions.perform()
q = re.sub(r'[^\d,.]', '', x1)
w = re.sub(r'[^\d,.]', '', x2)
e = re.sub(r'[^\d,.]', '', x3)
r = re.sub(r'[^\d,.]', '', i)
q12 = int(q)
w12 = int(w)
e12 = int(e)
r12 = int(r)


print(q12, w12, e12, r12)
if q12 >= w12 >= e12 >= r12:
    print('Отзывы от меньшего к большему считаются корректно')
else:
    print('Отзывы считаются не корректно')

time.sleep(3)
browser.close()
time.sleep(1)
browser.quit()

if __name__ == '__main__':
    main()

