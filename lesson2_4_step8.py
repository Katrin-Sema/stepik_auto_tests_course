from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

button = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
button = browser.find_element(By.CSS_SELECTOR, " #book").click()

browser.execute_script("window.scrollBy(0,100);")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)

element2 = browser.find_element(By.CSS_SELECTOR,'#answer')
element2.send_keys(y)
element3 = browser.find_element(By.CSS_SELECTOR, "#solve")
element3.click()

time.sleep(20)
browser.quit()
