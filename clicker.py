# COOKIE !!!!!!!!!!!! +) (C) Trick2g
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

from selenium.webdriver.support.wait import WebDriverWait


def print_test(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def convert_zeroes(production_unrefined):
    production_unrefined = production_unrefined.replace(",", "")
    production_unrefined = production_unrefined.replace(" ", "")
    try:
        if production_unrefined.__contains__("million"):
            production_unrefined = production_unrefined.replace("million", "")
            production_unrefined = float(production_unrefined) * 10 ** 6
        elif production_unrefined.__contains__("billion"):
            production_unrefined = production_unrefined.replace("billion", "")
            production_unrefined = float(production_unrefined) * 10 ** 9
        elif production_unrefined.__contains__("trillion"):
            production_unrefined = production_unrefined.replace("trillion", "")
            production_unrefined = float(production_unrefined) * 10 ** 12
        elif production_unrefined.__contains__("quadrillion"):
            production_unrefined = production_unrefined.replace("quadrillion", "")
            production_unrefined = float(production_unrefined) * 10 ** 15
        elif production_unrefined.__contains__("quadrillion"):
            production_unrefined = production_unrefined.replace("quadrillion", "")
            production_unrefined = float(production_unrefined) * 10 ** 18
        elif production_unrefined.__contains__("quintillion"):
            production_unrefined = production_unrefined.replace("quintillion", "")
            production_unrefined = float(production_unrefined) * 10 ** 21
        elif production_unrefined.__contains__("sextillion"):
            production_unrefined = production_unrefined.replace("sextillion", "")
            production_unrefined = float(production_unrefined) * 10 ** 24
        elif production_unrefined.__contains__("googol"):
            production_unrefined = production_unrefined.replace("googol", "")
            production_unrefined = float(production_unrefined) * 10 ** 27
        elif production_unrefined == "":
            production_unrefined = 0
        else:
            production_unrefined = float(production_unrefined)
    except:
        pass
    return production_unrefined


def opa_opa():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(chrome_options=options, executable_path='C:\\Program Files (X86)\\chromedriver.exe')
    driver.get('https://orteil.dashnet.org/cookieclicker/')
    driver.minimize_window()
    time.sleep(1)

    print(driver.title)

    # Locate latest save
    list_saves = os.listdir(f"C:\\Users\\{os.getlogin()}\\Downloads\\")
    list_saves_ref = list(filter(lambda x : re.search(r"McSpaghettiBakery \([0-9]*\)\.txt", x), list_saves))
    # list_saves_ref = list(filter(lambda x : re.search(r"RoyalPuppetBakery \([0-9]*\)\.txt", x), list_saves))
    list_saves_nums = [re.sub(r'[a-zA-Z|\s\.\(\)]', '', _str) for _str in list_saves_ref]
    list_saves_nums = [int(_str) for _str in list_saves_nums]
    latest_save_file = list_saves_ref[list_saves_nums.index(max(list_saves_nums))]

    # Load latest save
    driver.find_element(By.ID, "prefsButton").click()
    driver.find_element(By.ID, "FileLoadInput").send_keys(f"C:\\Users\\{os.getlogin()}\\Downloads\\{latest_save_file}")
    driver.find_element(By.CLASS_NAME, "menuClose").click()

    def get_production_from_popup(products):
        production_str = [driver.execute_script(f"return Game.ObjectsById[{i}].tooltip();") for i in
                          range(len(products))]
        production = []
        for j in production_str:
            production_unrefined = re.findall(r"(?<=<b>)([0-9a-zA-Z|,\.\s]*)(?=<\/b>)", j)
            if len(production_unrefined) > 0:
                production_unrefined = production_unrefined[0]
                production_unrefined = convert_zeroes(production_unrefined)
                if production_unrefined:
                    production.append(production_unrefined)
                else:
                    production.append(0)
            else:
                production.append(0)
        return production

    # def get_upgrades_from_popup(upgrades, popup_script):


    # MAIN MAIN
    # if input():
    i = 0
    while True:

        # let user to press button
        i += 1
        if (i % 100) == 0:
            time.sleep(1)

        # For clicking the cookie
        try:
            driver.find_element(By.ID, 'bigCookie').click()
            shimmers = driver.find_elements(By.CLASS_NAME, 'shimmer')
            for shimmer in shimmers:
                if shimmer.get_attribute("alt") != "Wrath cookie":
                    shimmer.click()
        except:
            pass

        # item auto buy
        if (i % 100) == 0:
            # income/price  <- the higher - the better
            try:
                # Products
                def get_products_info():
                    try:
                        products = driver.find_element(By.ID, 'products').find_elements_by_class_name('product')
                        prod_price = [convert_zeroes(product.find_element(By.CLASS_NAME, "price").text) for product in products]
                        prod_production = get_production_from_popup(products)
                        prod_kpd = [i[0]/i[1] if i[0]!=0 and i[1]!=0 else 0 for i in zip(prod_production, prod_price)]
                        prod_kpd[1] = -1    # keck grandmas
                        prod_status = [
                            "enabled" if product.get_attribute("class").__contains__("enabled") else "disabled" for
                            product in products]
                        # cut the ??? products
                        if len(prod_status)>len(prod_kpd):
                            prod_status = prod_status[:len(prod_kpd)]

                        prod_titles = [product.text for product in driver.find_elements(By.XPATH, "//div[@class='content']/div[@class='title']")]
                        prod_owned = [product.text for product in driver.find_elements(By.XPATH, "//div[@class='content']/div[@class='title owned']")]

                        # make to buy undiscovered products
                        for _price_i in range(1, len(prod_price)):
                            if prod_kpd[_price_i]==0 and prod_price[_price_i-1]*4>prod_price[_price_i]:
                                prod_kpd[_price_i] = 2**32
                                break
                            elif  prod_kpd[_price_i]==0:
                                break

                        # print(prod_kpd)
                        # print(prod_price)
                        # print(prod_status)
                        # print(prod_titles)
                        # print(prod_owned)

                        # find max obtainable product
                        # if product if fresh (0 of this product) and product price criteria -> biggest product price== 3*(biggest-1)product : then
                        # biggest product price product kpd = 999

                        return prod_kpd, prod_status, prod_titles, prod_owned
                    except Exception as e:
                        print("!get_products_info error! : " + str(e))

                # Upgrades
                def get_upgrades_info():
                    try:
                        upgrades = driver.find_elements(By.XPATH, r"//div[@class='crate upgrade' or @class='crate upgrade enabled']")
                        # print(upgrades)
                        upgrades_box = driver.find_element(By.XPATH, r"//div[@id='upgrades' and @class='storeSection upgradeBox']")
                        # print("upgrades_box: " + str(upgrades_box))
                        # print("upgrades_box: " + str(upgrades_box.get_attribute("innerHTML")))

                        innerHTMLs = [upgrade.get_attribute("outerHTML") for upgrade in upgrades]

                        description_script = [ _inf[0] if _inf else "" for _inf in
                                               [re.findall(r"(?<=\sfunction\(\)\{)([0-9a-zA-Z|,\.\s\=\[\]\;\(\)\{\}\'\\]*)(?=\}\()",
                                                     upgrade.get_attribute("outerHTML")) for upgrade in upgrades]
                                               ]

                        # press anything, that isn't a cookie multiplier
                        upgrades_production_str = [driver.execute_script(_scr) for _scr in description_script]
                        for _up_i in range(len(upgrades_production_str)):
                            _upgrades_prod = upgrades_production_str[_up_i]

                            # upgrade_name = re.findall(r"[a-zA-Z\s]*(?= are <b>twice</b> as efficient)", _upgrades_prod)
                            # print(upgrade_name)
                            if not re.findall(r"Cookie production multiplier", _upgrades_prod):
                                upgrades[_up_i].click()
                        return upgrades_production_str

                            # TODO extract x2 upgrade names from description
                            # TODO extract upgrade prices
                            # TODO calculate kpd based on overall production of prods
                            #r'<div style="padding:8px 4px;min-width:350px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-96px -432px;"></div><div style="float:right;text-align:right;"><span class="price">3.8 quadrillion</span></div><div class="name">Ritual rolling pins</div><div class="tag" style="color:#36a4ff;">[Tech]</div><div class="line"></div><div class="description">Grandmas are <b>twice</b> as efficient.<q>The result of years of scientific research!</q></div></div><div class="line"></div><div style="font-size:10px;font-weight:bold;color:#999;text-align:center;padding-bottom:4px;line-height:100%;">Click to research.</div>'

                    except Exception as e:
                        print("!get_upgrades_info error! : " + str(e))

                get_upgrades_info()
                prod_kpd, status_for_kpd, prod_title, prod_owned = get_products_info()

                # Pressing and judging
                global_kpd = prod_kpd
                global_status = status_for_kpd
                xpath_codes = [lambda num: fr"//div[@id='product{num}' and @class='product unlocked enabled']" for _code in range(len(prod_kpd))]

                if global_status[global_kpd.index(max(global_kpd))] == "enabled":
                    max_kpd_element_index = global_kpd.index(max(global_kpd))
                    product_element_to_buy = driver.find_element(By.XPATH, xpath_codes[max_kpd_element_index](max_kpd_element_index) )

                    # driver.implicitly_wait(1)
                    ActionChains(driver).move_to_element(product_element_to_buy).click(product_element_to_buy).perform()

            except Exception as e:
                print(e)


        # Auto-save
        if (i % 10**4) == 0 and (i>10**4):
            try:
                driver.find_element(By.ID, "prefsButton").click()
                driver.find_element(By.XPATH, fr"//a[text()='Save to file']").click()
                driver.find_element(By.CLASS_NAME, "menuClose").click()
                print("Saved!!!")
            except:
                print("Unsuccessful save :^(")
    driver.close()


if __name__ == '__main__':
    while True:
        opa_opa()