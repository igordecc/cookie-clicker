# "COOKIE !!!!!!!!!!!!" - Trick2g
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pyquery import PyQuery
import time
import re
import os

from Config import Config
from Upgrades import Upgrades
from selenium.webdriver.support.wait import WebDriverWait


if __name__ == '__main__':
    config = Config()
    config.boot_sequence()
    upgrades = Upgrades(config.driver)
    # config.driver.close()


