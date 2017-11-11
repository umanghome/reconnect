import datetime
import calendar
import json
import sys
import os
import dotenv
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# Get number of days
today = datetime.date.today()
days_in_this_month = calendar.monthrange(today.year, today.day)[1]
today = today.day - 1

# Fetch people
people_raw = open('people.json').read()
people_parsed = json.loads(people_raw)
people_parsed = people_parsed['people']
people_parsed = [p.encode('utf-8') for p in people_parsed]

# Find people to reconnect with today
people = []
i = 0
while True:
  try:
    person = people_parsed[today + (i * days_in_this_month)]
    people.append(person)
    i = i + 1
  except IndexError:
    break

# Exit if there's no one scheduled for today
if len(people) == 0:
  sys.exit(1)

# Gather first names
first_names = [name.split(' ')[0] for name in people]

# Fetch data required to send an email
dotenv.load_dotenv('.env')
try:
  email_config = {
    'from': os.environ.get('from').encode('utf-8'),
    'to': os.environ.get('to').encode('utf-8'),
    'password': os.environ.get('password').encode('utf-8'),
    'smtp_host': os.environ.get('smtp_host').encode('utf-8'),
    'smtp_port': os.environ.get('smtp_port').encode('utf-8'),
  }
except AttributeError, err:
  print '.env is not configured correctly, aborting.'
  sys.exit(2)

# Create email
email_msg = MIMEMultipart()
email_msg['From'] = email_config['from']
email_msg['To'] = email_config['to']

subject_string = 'Reconnect - '
subject_string = subject_string + datetime.date.today().strftime('%A %b %d, %Y')
subject_string = subject_string + ' - ' + ', '.join(first_names)

email_msg['Subject'] = subject_string

email_text = 'Hi!\n\nIt is ' + datetime.date.today().strftime('%A %b %d, %Y')
email_text = email_text + ' today.\n\n'
email_text = email_text + 'You need to reconnect with '
email_text = email_text + ', '.join(people) + '.'

email_msg.attach(MIMEText(email_text, 'plain'))

# Send email
server = smtplib.SMTP(email_config['smtp_host'], email_config['smtp_port'])
server.ehlo()
server.starttls()
server.ehlo()
server.login(email_config['from'], email_config['password'])
server.sendmail(email_config['from'], email_config['to'], email_msg.as_string())
