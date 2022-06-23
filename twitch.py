from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "https://www.twitch.tv/ilame"

browser = webdriver.Chrome()
browser.get(link)
#browser.maximize_window()


try:
    button_search = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/nav/div/div[1]/a[1]/div/figure/svg/g/polygon[2]'))
    )
    button_search.click()








finally:
    time.sleep(3)
    browser.close()
    time.sleep(1)
    browser.quit()

