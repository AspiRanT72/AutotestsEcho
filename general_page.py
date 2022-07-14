#Тест не готов!!!!!

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from auth_date import  LOGIN, PASSWORD

link = "https://obrazoval.ru/"
browser = webdriver.Chrome()
browser.get(link)


button_login = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'b-btn.b-header__login_button'))
).click()
#new_window = browser.switch_to.frame(1)
print(browser.window_handles)
#alert = browser.switch_to.alert
browser.switch_to.window(browser.window_handles[0])
email_input = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div/form/div[3]/div/div/input'))
).click()
time.sleep(2)
email_input.send_keys(LOGIN)
time.sleep(2)

time.sleep(3)
browser.close()
time.sleep(1)
browser.quit()

if __name__ == '__main__':
    main()