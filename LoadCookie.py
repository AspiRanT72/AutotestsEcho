from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from closed import vishel
from auth_date import LOGIN_EMAIL, PASSWORD
import pickle

link = "https://obrazoval.ru/"
browser = webdriver.Chrome()
browser.get(link)
browser.delete_all_cookies()
for cookie in pickle.load(open(f'{LOGIN_EMAIL}_cookies', 'rb')):
    browser.add_cookie(cookie)
time.sleep(10)
browser.refresh()
time.sleep(10)

time.sleep(3)
browser.close()
time.sleep(1)
browser.quit()

if __name__=='__main__':
    main()