from selenium import webdriver


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
            "executable_path": 'C:\\Program Files (X86)\\chromedriver.exe',
        })






