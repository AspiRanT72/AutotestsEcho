from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from auth_date import LOGIN_PHONE, LOGIN_EMAIL_TEST


link = 'https://obrazoval.ru/courses'
browser = webdriver.Chrome()
browser.get(link)
course = browser.find_elements(By.CLASS_NAME,
                               'ellipsis-3-lines')[1]
course.click()
time.sleep(2)
button_otzivi = browser.find_element(By.XPATH, "//a[@class ='b-btn b-btn--secondary block q-mb-xs' and text() = ' Оставить отзыв ' ]")
WebDriverWait(browser, 10).until(EC.visibility_of(button_otzivi))
button_otzivi.click()
time.sleep(2)
stars = browser.find_elements(By.CLASS_NAME, 'notranslate.material-icons.q-icon.q-rating__icon.text-gray')[4]
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(stars))
stars.click()
#Имя пользователя
input0 = browser.find_elements(By.XPATH, "//input[@class = 'b-input__field full-width']")[0]
WebDriverWait(browser, 10).until(EC.visibility_of(input0))
input0.send_keys('TestUserTest')
#номер телефона
input1 = browser.find_elements(By.XPATH, "//input[@class = 'b-input__field full-width']")[1]
WebDriverWait(browser, 10).until(EC.visibility_of(input1))
input1.send_keys(LOGIN_PHONE)
#Электронная почта
input2 = browser.find_elements(By.XPATH, "//input[@class = 'b-input__field full-width']")[2]
WebDriverWait(browser, 10).until(EC.visibility_of(input2))
input2.send_keys(LOGIN_EMAIL_TEST)
#Отзыв
input3 = browser.find_element(By.XPATH, "//textarea[@class = 'b-input__field full-width']")
WebDriverWait(browser, 10).until(EC.visibility_of(input3))
input3.send_keys('TestTestTestTestTestTestTestTestTestTest')

button_send = browser.find_element(By.XPATH, "//div[@class ='b-btn' and text() = ' Продолжить ' ]")
# actions = ActionChains(browser)
# actions.double_click(button_send)
button_send.click()


time.sleep(3)
browser.close()
time.sleep(1)
browser.quit()

if __name__ == '__main__':
    main()

