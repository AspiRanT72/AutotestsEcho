from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
link = 'https://obrazoval.ru/courses'
browser = webdriver.Chrome()
browser.get(link)
rating = browser.find_elements(By.CLASS_NAME, 'inline-md-block.cursor-pointer.l-sort__item.q-mr-xs.q-mr-lg-sm')[1].click()
time.sleep(2)
x1 = browser.find_elements(By.XPATH, '//div[@class ="text-h4 q-mr-xs"]')[1].text
x2 = browser.find_elements(By.XPATH, '//div[@class ="text-h4 q-mr-xs"]')[2].text
x3 = browser.find_elements(By.XPATH, '//div[@class ="text-h4 q-mr-xs"]')[3].text
x4 = browser.find_elements(By.XPATH, '//div[@class ="text-h4 q-mr-xs"]')[4]
i=x4.text
actions = ActionChains(browser)
actions.move_to_element(x4)
actions.perform()
print(x1, x2, x3, i)
if x1 >= x2 >= x3 >= i:
    print('Рейтинг от большего к меньшему считается корректно')
else:
    print('Рейтинг считается не корректно')

time.sleep(3)
browser.close()
time.sleep(1)
browser.quit()

if __name__ == '__main__':
    main()

