from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
import time
import os
from math import sin,log

def f(x):
    return log(abs(12*sin((x))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100"))

browser.find_element(By.ID, 'book').click()

x_el = browser.find_element(By.ID, 'input_value')
x = float(x_el.text)

browser.find_element(By.ID, 'answer').send_keys(str(f(x)))
browser.find_element(By.ID, "solve").click()

print(browser.switch_to.alert.text)

browser.quit()
