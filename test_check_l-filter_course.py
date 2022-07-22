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
time.sleep(2)
x1 = browser.find_element(By.XPATH, "//a[@class ='l-filter__seo-link' and text() = 'Творчество' ]")

# By.XPATH, "//button[@class ='b-btn b-header__login_button' and text() = ' Войти ']")
actions = ActionChains(browser)
actions.move_to_element(x1)
actions.perform()
x1.click()
print(__name__ + 'Gotov')
time.sleep(3)
browser.close()
time.sleep(1)
browser.quit()

if __name__ == '__main__':
    main()

