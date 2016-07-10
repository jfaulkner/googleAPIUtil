#!/usr/bin/python

import threading, feedparser, time
import os
#import RPi_GPIO as GPIO
from time import strftime
from datetime import datetime
from time import sleep
USERNAME="piwoof"
RED_LED=14

if __name__=='__main__':
  x=0
  password = ''
  homedir=os.path.expanduser('~')
  with open(os.path.abspath(homedir+'/.credentials/woof.txt')) as myfile:
    password=myfile.read().rstrip()
  while x<5:
    newmails=int(feedparser.parse("https://"+USERNAME+":"+password+"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
    mail_str='You have {0} new messages'.format(newmails)
    cmd_str = 'espeak -ven-us+f3 "{0}" >/dev/null'.format(mail_str)
    print mail_str
    os.system(cmd_str)
    time.sleep(5)
    x=x+1

