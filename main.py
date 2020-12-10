from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
from decouple import config
import smtplib
from email.message import EmailMessage

# make chrome headless
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")

# chrome v87
options.binary_location = '/usr/bin/google-chrome-stable'

# chromedriver v87
DRIVER_PATH = '/home/vongsana/projects/web-scraper/chromedriver'

# run chrome and get craigslist page
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

BASE_URL = 'https://vancouver.craigslist.org'
QUERY = 'pokemon'

#all results on all pages
allPosts = []


def startSearch(pageLink):
  driver.get(BASE_URL + pageLink)
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  allPosts.extend(soup.find_all('li', 'result-row'))
  nextButton = soup.find('a', class_='next')
  if nextButton is None: return allPosts
  startSearch(nextButton.get('href'))

def formatSearch(posts):
  postForEmail = ''
  for i, post in enumerate(posts):
    postTime = post.find('time').get('datetime')
    postTimeFormatted = datetime.strptime(postTime, '%Y-%m-%d %H:%M')
    ellapsedTime = (datetime.now() - postTimeFormatted)
    postTitle = post.find('a', class_='result-title').get_text()
    postURL = post.find('a', class_='result-title')['href']

    postForEmail += f'{i} - {ellapsedTime}:    {postTitle} - {postURL} \n'
  return postForEmail

startSearch(f'/d/for-sale/search/sss?sort=date&query={QUERY}')

EMAIL_ADDRESS = config('EMAIL_USER')
EMAIL_PASSWORD = config('EMAIL_PASS')
msg = EmailMessage()
msg['Subject'] = 'Craigslist scrape'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content(formatSearch(allPosts))

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

  smtp.send_message(msg)

driver.quit()