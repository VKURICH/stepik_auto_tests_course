from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element(By.ID, 'book')
    button.click()


    x = browser.find_element(By.ID, 'input_value')
    x = x.text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

