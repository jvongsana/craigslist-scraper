from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = '/home/vongsana/projects/web-scraper/chromedriver'
options.binary_location = '/usr/bin/google-chrome-stable'

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://vancouver.craigslist.org/d/for-sale/search/sss?sort=date&query=pokemon')
print(driver.page_source)
driver.quit()