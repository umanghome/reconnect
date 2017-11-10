import datetime
import calendar
import json
import sys

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

# Send email
