import time
from selenium import webdriver
browser = webdriver.Chrome()
def vishel():
    time.sleep(3)
    browser.close()
    time.sleep(1)
    browser.quit()

