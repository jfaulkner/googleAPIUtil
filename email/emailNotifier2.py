#!/usr/bin/python

import threading, feedparser, time
#import RPi_GPIO as GPIO
import urllib, pycurl, os
from time import strftime
from datetime import datetime
from time import sleep
USERNAME="piwoof"
RED_LED=14

def downloadFile(url, fileName):
  fp=open(fileName, "wb")
  curl=pycurl.Curl()
  curl.setopt(pycurl.URL, url)
  curl.setopt(pycurl.WRITEDATA, fp)
  curl.perform()
  curl.close()
  fp.close()

def getGoogleSpeechURL(phrase):
  googleTranslateURL = "http://translate.google.com/translate_tts?tl=en&"
  parameters = {'q': 'the quick brown fox jumped over the lazy dog'}
  data = urllib.urlencode(parameters)
  googleTranslateURL = "%s%s" % (googleTranslateURL,data)
  return googleTranslateURL

def speakSpeechFromText(phrase):
  googleSpeechURL = getGoogleSpeechURL(phrase)
  print googleSpeechURL
  downloadFile(googleSpeechURL,"tts.mp3")
  sleep(10)
  os.system("mplayer tts.mp3 -af extrastereo=0 &")
  sleep(10)
  os.remove("tts.mp3")

if __name__=='__main__':
  x=0
  password = ''
  homedir=os.path.expanduser('~')
  with open(os.path.abspath(homedir+'/.credentials/woof.txt')) as myfile:
    password=myfile.read().rstrip()
  while x<1:
    newmails=int(feedparser.parse("https://"+USERNAME+":"+password+"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
    mailStr = "You have", newmails, "new messages"
    print mailStr
    speakSpeechFromText(mailStr)
    time.sleep(5)
    x=x+1

