# googleAPIUtil
Utilities for pulling data from gmail, drive, calendar, etc.
This project was written to run on Raspbian and activate LEDs through the Raspberry Pi GPIO on certain triggers - for instance, when a new email is received or there is an upcoming calendar event on the current day.

1) Upgrade to Python 3 (I upgraded to 3.5 from 2.7.9)
  backup your system using the Win32DiskImager or the linux dd command
  $sudo apt-get update
  $sudo apt-get upgrade -y
  $sudo apt-get dist-upgrade
  $ sudo apt-get install build-essential libncursesw5-dev libgdbm-dev libc6-dev 
  $ sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
  $ sudo apt-get install libssl-dev openssl
  $ mkdir ~/python && cd ~/python
  $ wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz
  $ tar -zxvf Python-3.5.0.tgz
  $ cd Python-3.5.0
  $ ./configure
  $ make
  $ sudo make install
  $ python3.5 --version
  $ cd ..
  $ wget https://bootstrap.pypa.io/get-pip.py
  $ sudo python3.5 get-pip.py
  $ pip3.5 --version

2) update your path so python 3.5 and pip are the default versions (for me, this was pip 8.1.1)
3) pip install oauth2client pyopenssl gspread google-api-python-client

4) Get service token from Google Dev Console

5) Save secret json on the system running the project in an accessible location

6) Run standalone to test or as a service
