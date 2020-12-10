# Craigslist Web Scraper

  A script that scrapes through craigslist based on your query. It will email user the results with the age of post, title, and URL. 

## Dependencies
  *  selenium
  *  bs4
  *  datetime
  *  smtplib
  *  EmailMessage
  *  decouple

## Setup

1. Edit main.py - change line 24 to equal your craigslist search.

`QUERY = 'YOUR_SEARCH'`

2. Create a .env file to fill in your email credientials. (For security purposes, it would be best to use tokens or app passwords if your email provided supports it) 

`EMAIL_USER=YOUR_EMAIL_ADDRESS`

`EMAIL_PASS=YOUR_EMAIL_PASSWODE/TOKEN`

3. Run the script. (Run according to your needs) I have personally choice to create a scheduled task on a Windows machine to run the script according to my needs. This way I do not have a server running the entire time and have the email send all results so a database is not replied upon. 

## Optional/Future Improvements

  There is definitely room to expand to have the script placed on a server that runs on a time interval. Also linking the results to a database to only send new results. For my basic needs, this was not necessary but definitely room for others to add on if they wish.
 