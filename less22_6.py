from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)

    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    input3 = browser.find_element(By.ID, 'robotsRule')
    input3.click()
    #browser.execute_script("window.scrollBy(0, 100);")

    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()