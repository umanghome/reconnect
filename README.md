# Reconnect

_Reconnect with people on a daily basis, once every month._

## Concept

The number of people I know and I'd like to keep in touch with keeps on increasing as I grow older. I often feel I should once in a while drop a text as simple as
> Hi, what's up? How have you been?

But when do I send this message to which person? That got confusing, so I thought of a system that would remind me to _reconnect_ with people every day. I should ideally be texting each person once a month, just to catch up.

#### Current Stste

At this point, the system is just a basic Python script which should be ran once every day (CRON job or whatever), and it will send an email to yourself reminding you to reconnect with X[, Y, and Z].

In `people.json`, you put in the names of the people you would like to reconnect with.

In `.env`, you set your email settings.

#### Enhancements

Instead of being something that spams your email inbox every day, this system could be something like a full-fledged app. It would send a notification each day. However, at this point, a script that sends an email works just fine. Here are a list of things I'd like to build:

* Mobile app that sends notifications instead of emails.
* Syncs with your address-book.
* Identifies birthdays of the people you wish to reconnect with, and puts them in slots accordingly. Example: If X's birthday is on 5th, the system should not suggest you to reconnect with X on 2nd or 3rd.


## Contributing

Feel free to suggest features that the system should have. Submit a PR adding the feature(s) to this README.

Also, feel free to build upon the features mentioned above. Raise an Issue and we'll start dicussing.