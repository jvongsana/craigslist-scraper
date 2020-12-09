from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# make chrome headless
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")

# chrome v87
options.binary_location = '/usr/bin/google-chrome-stable'

# chromedriver v87
DRIVER_PATH = '/home/vongsana/projects/web-scraper/chromedriver'
BASE_URL = 'https://vancouver.craigslist.org'

# run chrome and get craigslist page
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://vancouver.craigslist.org/d/for-sale/search/sss?sort=date&query=pokemon')

#parse html
soup = BeautifulSoup(driver.page_source, 'html.parser')

#all results for page



def nextPage(pageLink):
  driver.get(BASE_URL + pageLink)
  soup = BeautifulSoup(driver.page_source, 'html.parser')

  for post in soup.find_all('a', class_='result-title'):
    print(post.text + ' - ' + post['href'])
    
  nextButton = soup.find('a', class_='next')
  if nextButton is None: return
  nextPage(nextButton.get('href'))

nextPage('/d/for-sale/search/sss?sort=date&query=pokemon')


driver.quit()