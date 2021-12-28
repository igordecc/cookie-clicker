from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import re
import os


def chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_experimental_option("detach", True)
    return options


class Config:
    ALLOWED_DRIVERS = [
        webdriver.Firefox,
        webdriver.FirefoxProfile,
        webdriver.Chrome,
        webdriver.ChromeOptions,
        webdriver.Ie,
        webdriver.Opera,
        webdriver.Remote,
        webdriver.DesiredCapabilities,
        webdriver.ActionChains,
        webdriver.TouchActions,
        webdriver.Proxy,
    ]

    chrome_driver = webdriver.Chrome(**{
            "chrome_options": chrome_options(),
            "executable_path": "C:\\Program Files (X86)\\chromedriver.exe",
        })
    
    driver = chrome_driver
    
    cookie_clicker_website = "https://orteil.dashnet.org/cookieclicker/"
    boot_time_sleep = 1
    list_saves = os.listdir(f"C:\\Users\\{os.getlogin()}\\Downloads\\")
    bakery_name = "McSpaghettiBakery"
        
    def boot_sequence(self):
        self.driver.get(self.cookie_clicker_website)
        self.driver.minimize_window()
        time.sleep(self.boot_time_sleep)

        # find latest file in save directory
        saves_refs = list(filter(lambda x: re.search(rf"{self.bakery_name} \([0-9]*\)\.txt", x), self.list_saves))
        list_saves_nums = [int(re.sub(r'[a-zA-Z|\s\.\(\)]', '', _str)) for _str in saves_refs]
        latest_save_file = saves_refs[list_saves_nums.index(max(list_saves_nums))]

        # Load latest save
        self.driver.find_element(By.ID, "prefsButton").click()
        self.driver.find_element(By.ID, "FileLoadInput").send_keys(
            f"C:\\Users\\{os.getlogin()}\\Downloads\\{latest_save_file}")
        self.driver.find_element(By.CLASS_NAME, "menuClose").click()






