from selenium import webdriver
from Config import Config
import sys
from selenium.webdriver.common.keys import Keys


class Upgrades:
    all_info = {}

    def __init__(self, driver: webdriver.Chrome):
        if True in list(map(lambda ad: isinstance(driver, ad), Config.ALLOWED_DRIVERS)):
            print(driver)
        else:
            raise Exception("Exception: bad driver")

    def read(self):
        pass


if __name__ == '__main__':
    upgrades = Upgrades(Config.chrome_driver)
    Config.chrome_driver.close()
