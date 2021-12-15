# COOKIE !!!!!!!!!!!! +) (C) Trick2g

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


def print_test(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def opa_opa():
    opt = Options()
    opt.add_argument('start-maximized')

    driver = webdriver.Chrome(chrome_options=opt, executable_path='C:\\Program Files (X86)\\chromedriver.exe')
    driver.get('https://orteil.dashnet.org/cookieclicker/')
    time.sleep(5)
    print(driver.title)

    # MAIN MAIN
    # if input():
    i = 0
    while True:

        # let user to press button
        i += 1
        if (i % 100) == 0:
            time.sleep(1)

        # For clicking the cookie
        driver.find_element(By.ID, 'bigCookie').click()
        try:
            driver.find_element(By.CLASS_NAME, 'shimmer').click()
        except:
            pass

        # item auto buy
        if (i % 10) == 0:
            # income/price  <- the higher - the better
            try:
                for product in driver.find_element(By.ID, 'products').find_elements_by_class_name('product'):
                    price = product.find_element(By.CLASS_NAME, "price").text
                    print(price)
                    print(driver.find_element(By.ID, 'tooltip').find_element(By.CLASS_NAME, "data").find_elements(By.TAG_NAME, 'b'))
                    production = driver.find_element(By.ID, 'tooltip').find_element(By.CLASS_NAME, "data").find_elements(By.TAG_NAME, 'b')[0].text
                    print(production)
            except:
                pass

        # int(driver.find_element(By.ID, 'cookies').text.split(' ')[0].replace('.', ''))

    driver.close()


if name == 'main':
    opa_opa()

    print_test('PyCharm')