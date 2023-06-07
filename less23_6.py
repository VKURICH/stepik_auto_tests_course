from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value')
    x = x.text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

