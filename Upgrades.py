from selenium import webdriver
from selenium.webdriver.common.by import By
from Config import Config
import sys
import re
from selenium.webdriver.common.keys import Keys


class Upgrades:
    all_info = {}

    def __init__(self, driver):
        if True in list(map(lambda ad: isinstance(driver, ad), Config.ALLOWED_DRIVERS)):
            self.driver = driver
        else:
            raise Exception("Exception: bad driver")

    def read(self) -> all_info:
        # populate all_info with fresh data!
        upgrades = self.driver.find_elements(By.XPATH, r"//div[@class='crate upgrade' or @class='crate upgrade enabled']")
        print(upgrades)





        # return upgrades, upgrades_description
        return self.all_info


if __name__ == '__main__':
    upgrades = Upgrades(Config.chrome_driver)
    upgrades.read()
