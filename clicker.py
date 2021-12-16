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
        elif production_unrefined.__contains__("nonillion"):
            production_unrefined = production_unrefined.replace("nonillion", "")
            production_unrefined = float(production_unrefined) * 10 ** 21
        elif production_unrefined.__contains__("decillion"):
            production_unrefined = production_unrefined.replace("decillion", "")
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
    opt = Options()
    opt.add_argument('start-maximized')

    driver = webdriver.Chrome(chrome_options=opt, executable_path='C:\\Program Files (X86)\\chromedriver.exe')
    driver.get('https://orteil.dashnet.org/cookieclicker/')
    driver.minimize_window()
    time.sleep(2)
    print(driver.title)

    # Locate latest save
    list_saves = os.listdir(f"C:\\Users\\{os.getlogin()}\\Downloads\\")
    list_saves_ref = list(filter(lambda x : re.search(r"McSpaghettiBakery \([0-9]*\)\.txt", x), list_saves))
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
        return production

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
            driver.find_element(By.CLASS_NAME, 'shimmer').click()
        except:
            pass

        # item auto buy
        if (i % 100) == 0:
            # income/price  <- the higher - the better
            try:
                products = driver.find_element(By.ID, 'products').find_elements_by_class_name('product')
                title = [product.find_element(By.CLASS_NAME, "title").text for product in products]
                price = [convert_zeroes(product.find_element(By.CLASS_NAME, "price").text) for product in products]
                status = ["enabled" if product.get_attribute("class").__contains__("enabled") else "disabled" for product in products]
                production = get_production_from_popup(products)

                kpd = [i[0]/i[1] if i[0]!=0 and i[1]!=0 else 0 for i in zip(production, price)]

                status_for_kpd = []
                if len(status)>len(kpd):
                    status_for_kpd = status[:len(kpd)]
                else:
                    print("kpd len status error")
                    print("kpd len: "+str(len(kpd)))
                    print("status len: "+str(len(status)))

                if status_for_kpd[kpd.index(max(kpd))] == "enabled":
                    kpd_enabled = [kpd_i[0] if kpd_i[1] == "enabled" else 0 for kpd_i in zip(kpd, status_for_kpd)]
                    product_element_to_buy = driver.find_element(By.XPATH, fr"//div[@id='product{kpd.index(max(kpd_enabled))}' and @class='product unlocked enabled']")

                    # driver.implicitly_wait(1)
                    ActionChains(driver).move_to_element(product_element_to_buy).click(product_element_to_buy).perform()

            except Exception as e:
                print(e)

                [
                    '<div style="min-width:350px;padding:8px;">'
                    '   <div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:0px 0px;">'
                    '       </div><div style="float:right;text-align:right;"><span class="price">4.671 billion</span></div>'
                    '           <div class="name">Cursor</div><small>[owned : 140</small>]<div class="line"></div><div class="description">Autoclicks once every 10 seconds.</div><div class="line"></div>'
                    '           <div class="data">&bull; each cursor produces <b>25,500</b> cookies per second<br>&bull; 140 cursors producing <b>3.57 million</b> cookies per second (<b>0%</b> of total CpS)<br>&bull; <b>207.973 billion</b> cookies clicked so far</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-48px 0px;"></div><div style="float:right;text-align:right;"><span class="price">31.141 billion</span></div><div class="name">Grandma</div><small>[owned : 140</small>]<div class="line"></div><div class="description">A nice grandma to bake more cookies.</div><div class="line"></div><div class="data">&bull; each grandma produces <b>240,746</b> cookies per second<br>&bull; 140 grandmas producing <b>33.705 million</b> cookies per second (<b>0.1%</b> of total CpS)<br>&bull; ...also boosting some other buildings : farms +140%, mines +70%, factories +46.7%, shipments +20%, alchemy labs +17.5%, portals +15.6%, banks +35%, temples +28%, wizard towers +23.3% - all combined, these boosts account for <b>1.769 billion</b> cookies per second (<b>3.3%</b> of total CpS)<br>&bull; <b>834.69 billion</b> cookies baked so far</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-96px 0px;"></div><div style="float:right;text-align:right;"><span class="price">4.499 billion</span></div><div class="name">Farm</div><small>[owned : 109</small>]<div class="line"></div><div class="description">Grows cookie plants from cookie seeds.</div><div class="line"></div><div class="data">&bull; each farm produces <b>4,514</b> cookies per second<br>&bull; 109 farms producing <b>492,025</b> cookies per second (<b>0%</b> of total CpS)<br>&bull; <b>26.273 billion</b> cookies harvested so far</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-144px 0px;"></div><div style="float:right;text-align:right;"><span class="price">5.245 billion</span></div><div class="name">Mine</div><small>[owned : 93</small>]<div class="line"></div><div class="description">Mines out cookie dough and chocolate chips.</div><div class="line"></div><div class="data">&bull; each mine produces <b>9,392</b> cookies per second<br>&bull; 93 mines producing <b>873,493</b> cookies per second (<b>0%</b> of total CpS)<br>&bull; <b>55.815 billion</b> cookies mined so far</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-192px 0px;"></div><div style="float:right;text-align:right;"><span class="price">18.574 billion</span></div><div class="name">Factory</div><small>[owned : 85</small>]<div class="line"></div><div class="description">Produces large quantities of cookies.</div><div class="line"></div><div class="data">&bull; each factory produces <b>44,826</b> cookies per second<br>&bull; 85 factories producing <b>3.81 million</b> cookies per second (<b>0%</b> of total CpS)<br>&bull; <b>210.563 billion</b> cookies mass-produced so far</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-720px 0px;"></div><div style="float:right;text-align:right;"><span class="price">14.055 billion</span></div><div class="name">Bank</div><small>[owned : 66</small>]<div class="line"></div><div class="description">Generates cookies from interest.</div><div class="line"></div><div class="data">&bull; each bank produces <b>222,173</b> cookies per second<br>&bull; 66 banks producing <b>14.663 million</b> cookies per second (<b>0%</b> of total CpS)<br>&bull; <b>852.307 billion</b> cookies banked so far</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-768px 0px;"></div><div style="float:right;text-align:right;"><span class="price">28.376 billion</span></div><div class="name">Temple</div><small>[owned : 52</small>]<div class="line"></div><div class="description">Full of precious, ancient chocolate.</div><div class="line"></div><div class="data">&bull; each temple produces <b>1.174 million</b> cookies per second<br>&bull; 52 temples producing <b>61.029 million</b> cookies per second (<b>0.1%</b> of total CpS)<br>&bull; <b>3.253 trillion</b> cookies discovered so far</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-816px 0px;"></div><div style="float:right;text-align:right;"><span class="price">115.733 billion</span></div><div class="name">Wizard tower</div><small>[owned : 42</small>]<div class="line"></div><div class="description">Summons cookies with magic spells.</div><div class="line"></div><div class="data">&bull; each wizard tower produces <b>3.19 million</b> cookies per second<br>&bull; 42 wizard towers producing <b>133.962 million</b> cookies per second (<b>0.2%</b> of total CpS)<br>&bull; <b>8.661 trillion</b> cookies summoned so far</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-240px 0px;"></div><div style="float:right;text-align:right;"><span class="price">584.698 billion</span></div><div class="name">Shipment</div><small>[owned : 34</small>]<div class="line"></div><div class="description">Brings in fresh cookies from the cookie planet.</div><div class="line"></div><div class="data">&bull; each shipment produces <b>18.521 million</b> cookies per second<br>&bull; 34 shipments producing <b>629.731 million</b> cookies per second (<b>1.2%</b> of total CpS)<br>&bull; <b>34.012 trillion</b> cookies shipped so far</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-288px 0px;"></div><div style="float:right;text-align:right;"><span class="price disabled">4.275 trillion</span></div><div class="name">Alchemy lab</div><small>[owned : 29</small>]<div class="line"></div><div class="description">Turns gold into cookies!</div><div class="line"></div><div class="data">&bull; each alchemy lab produces <b>110.499 million</b> cookies per second<br>&bull; 29 alchemy labs producing <b>3.204 billion</b> cookies per second (<b>5.9%</b> of total CpS)<br>&bull; <b>156.868 trillion</b> cookies transmuted so far</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-336px 0px;"></div><div style="float:right;text-align:right;"><span class="price disabled">32.59 trillion</span></div><div class="name">Portal</div><small>[owned : 25</small>]<div class="line"></div><div class="description">Opens a door to the Cookieverse.</div><div class="line"></div><div class="data">&bull; each portal produces <b>339.595 million</b> cookies per second<br>&bull; 25 portals producing <b>8.49 billion</b> cookies per second (<b>15.8%</b> of total CpS)<br>&bull; <b>277.493 trillion</b> cookies retrieved so far</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-384px 0px;"></div><div style="float:right;text-align:right;"><span class="price disabled">112.78 trillion</span></div><div class="name">Time machine</div><small>[owned : 15</small>]<div class="line"></div><div class="description">Brings cookies from the past, before they were even eaten.</div><div class="line"></div><div class="data">&bull; each time machine produces <b>1.91 billion</b> cookies per second<br>&bull; 15 time machines producing <b>28.653 billion</b> cookies per second (<b>53.2%</b> of total CpS)<br>&bull; <b>536.008 trillion</b> cookies recovered so far</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-624px 0px;"></div><div style="float:right;text-align:right;"><span class="price disabled">294.358 trillion</span></div><div class="name">Antimatter condenser</div><small>[owned : 4</small>]<div class="line"></div><div class="description">Condenses the antimatter in the universe into cookies.</div><div class="line"></div><div class="data">&bull; each antimatter condenser produces <b>3.159 billion</b> cookies per second<br>&bull; 4 antimatter condensers producing <b>12.637 billion</b> cookies per second (<b>23.5%</b> of total CpS)<br>&bull; <b>104.731 trillion</b> cookies condensed so far</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:-672px 0px;"></div><div style="float:right;text-align:right;"><span class="price disabled">2.079 quadrillion</span></div><div class="name">Prism</div><small>[owned : 0</small>]<div class="line"></div><div class="description">Converts light itself into cookies.</div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:0px -336px;"></div><div style="float:right;text-align:right;"><span class="price disabled">25.74 quadrillion</span></div><div class="name">???</div><small>[owned : 0</small>]<div class="line"></div><div class="description"></div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:0px -336px;"></div><div style="float:right;text-align:right;"><span class="price disabled">306.9 quadrillion</span></div><div class="name">???</div><small>[owned : 0</small>]<div class="line"></div><div class="description"></div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:0px -336px;"></div><div style="float:right;text-align:right;"><span class="price disabled">70.29 quintillion</span></div><div class="name">???</div><small>[owned : 0</small>]<div class="line"></div><div class="description"></div></div>',
                    '<div style="min-width:350px;padding:8px;"><div class="icon" style="float:left;margin-left:-8px;margin-top:-8px;background-position:0px -336px;"></div><div style="float:right;text-align:right;"><span class="price disabled">11.88 sextillion</span></div><div class="name">???</div><small>[owned : 0</small>]<div class="line"></div><div class="description"></div></div>']

        # Auto-save
        if (i % 10**4) == 0 and (i>10**4):
            try:
                driver.find_element(By.ID, "prefsButton").click()
                save_button = driver.find_element(By.XPATH, fr"//a[text()='Save to file']")
                print(save_button.get_attribute("innerHTML"))
                driver.find_element(By.XPATH, fr"//a[text()='Save to file']").click()
                driver.find_element(By.CLASS_NAME, "menuClose").click()
                print("!!!")
            except:
                print("Unsuccessful save :^(")



    driver.close()


if __name__ == '__main__':
    opa_opa()