from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from auth_date import LOGIN_INVALID_EMAIL
link = "https://obrazoval.ru/"
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

#Нажимаем кнопку Войти
element = browser.find_element(By.XPATH, "//button[@class ='b-btn b-header__login_button' and text() = ' Войти ']")
WebDriverWait(browser, 10).until(EC.visibility_of(element))
element.click()
time.sleep(3)
#Вводим логин
element_login = browser.find_element(By.XPATH, "//input[@placeholder ='Email или телефон']")
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(element_login))
element_login.send_keys(LOGIN_INVALID_EMAIL)
#Нажимаем кнопку "Далее"
element_next = browser.find_element(By.XPATH, "//button[@class ='b-btn b-user__auth-submit']")
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(element_next))
element_next.click()
time.sleep(3)
#Вводим пароль
element_notification = browser.find_element(By.CLASS_NAME, "b-input__error")
WebDriverWait(browser, 10).until(EC.visibility_of(element_notification))
i = element_notification.text
print(i)

time.sleep(3)
browser.close()
time.sleep(1)
browser.quit()

if __name__=='__main__':
    main()