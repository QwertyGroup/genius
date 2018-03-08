from selenium import webdriver
from definitions import chromedriver_path
import time


def get_driver(headless=False, no_images=False):

    chrome_options = webdriver.ChromeOptions()

    if headless:
        chrome_options.add_argument("--headless")
    if no_images:
        chrome_options.add_argument('--blink-settings=imagesEnabled=false')

    chrome_options.add_argument('--window-size=1600,900')
    return webdriver.Chrome(chromedriver_path, chrome_options=chrome_options)


print('Getting driver...')
driver = get_driver()
print('Done')

driver.get('https://genius.com/Vince-staples-big-fish-lyrics')
time.sleep(5)
driver.get('https://genius.com/Pharaoh-champagne-squirt-lyrics')