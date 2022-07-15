from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re
link = 'https://obrazoval.ru/courses'
browser = webdriver.Chrome()
browser.get(link)
rating = browser.find_elements(By.CLASS_NAME, 'inline-md-block.cursor-pointer.l-sort__item.q-mr-xs.q-mr-lg-sm')[2]
rating.click()
time.sleep(2)
rating.click()
time.sleep(2)
x1 = browser.find_elements(By.XPATH, '//div[@class ="b-title__custom l-course__price"]')[1]
x2 = browser.find_elements(By.XPATH, '//div[@class ="b-title__custom l-course__price"]')[2]
x3 = browser.find_elements(By.XPATH, '//div[@class ="b-title__custom l-course__price"]')[3]
x4 = browser.find_elements(By.XPATH, '//div[@class ="b-title__custom l-course__price"]')[4]
q = x1.text
w = x2.text
e = x3.text
r = x4.text
actions = ActionChains(browser)
actions.move_to_element(x4)
actions.perform()
# q1 = (q[:-1]).isalnum()
q1 = re.sub(r'[^\d,.]', '', q)
w2 = re.sub(r'[^\d,.]', '', w)
e3 = re.sub(r'[^\d,.]', '', e)
r4 = re.sub(r'[^\d,.]', '', r)
q12 = int(q1)
w12 = int(w2)
e12 = int(e3)
r12 = int(r4)
# for d in x1.replace('' , ''):
#     n = int(d[:-1])
#     print(n)

# print(q1, w2, e3, r4)
print(q12, w12, e12, r12)
if q12 >= w12 >= e12 >= r12:
    print('Цена от большего к меньшему считается корректно')
else:
    print('Цена считается не корректно')

time.sleep(3)
browser.close()
time.sleep(1)
browser.quit()

if __name__ == '__main__':
    main()

