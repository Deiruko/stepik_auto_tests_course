from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    new_x = x_element.text
    x = new_x
    y = calc(x)
    print(new_x)
    input1 = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
    option1.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    option2 = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

