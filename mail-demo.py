from decouple import config
import smtplib

EMAIL_ADDERSS = config('EMAIL_USER')
EMAIL_PASSWORD = config('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.ehlo()

  smtp.login()