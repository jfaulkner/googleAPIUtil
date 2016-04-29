# googleAPIUtil
Utilities for pulling data from gmail, drive, calendar, etc.
This project was written to run on Raspbian and activate LEDs through the Raspberry Pi GPIO on certain triggers - for instance, when a new email is received or there is an upcoming calendar event on the current day.

1) Upgrade to Python 3 (I upgraded to 3.5)

2) sudo apt-get install pip

3) pip install oauth2client pyopenssl gspread google-api-python-client

4) Get service token from Google Dev Console

5) Save secret json on the system running the project in an accessible location

6) Run standalone to test or as a service
