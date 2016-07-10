from pprint import pprint
import requests
from urllib.request import urlopen
import json
import os

APIKEY=''
ZIP='22902'

def currentWeather():
    url = 'http://api.wunderground.com/api/' + APIKEY + '/geolookup/conditions/q/VA/' + ZIP + '.json'
    f = urlopen(url)
    json_string = f.read().decode('utf-8')
    parsed_json = json.loads(json_string)
    city = parsed_json['location']['city']
    state = parsed_json['location']['state']
    weather = parsed_json['current_observation']['weather']
    temperature_string = parsed_json['current_observation']['temperature_string']
    feelslike_string = parsed_json['current_observation']['feelslike_string']
    print('Weather in ' + city + ', ' + state + ': ' + weather.lower() + '. The temperature is ' + temperature_string + ' but it feels like ' + feelslike_string + '.')
    f.close()

def forecast10day():
    url = 'http://api.wunderground.com/api/' + APIKEY + '/geolookup/forecast10day/q/' + ZIP + '.json'
    f = urlopen(url)
    json_string = f.read().decode('utf-8')
    parsed_json = json.loads(json_string)
    for day in parsed_json['forecast']['simpleforecast']['forecastday']:
    	print(day['date']['weekday'] + ' (' + day['date']['pretty'] + '):')
    	print('  Conditions: ' + day['conditions'])
    	print('  High:' + day['high']['fahrenheit'] + 'F')
    	print('  Low: ' + day['low']['fahrenheit'] + 'F')
    f.close()

def alerts():
    url = 'http://api.wunderground.com/api/0a4f528862472dcb/alerts/q/VA/' + ZIP + '.json'
    f = urlopen(url)
    json_string = f.read().decode('utf-8')
    parsed_json = json.loads(json_string)
    #print(parsed_json)
    if len(parsed_json['alerts']) == 0:
        print('No alerts received')
    else:
        for alert in parsed_json['alerts']:
            print('  Alert: ' + alert['description'] + '(' + alert['date'] + ')')
            print('  Expires: ' + alert['expires'])
            print('  ' + alert['message'].decode('utf-8'))
    f.close()


if __name__=='__main__':
    homedir=os.path.expanduser('~')
    with open(os.path.abspath(homedir+'/.credentials/weatherkey.txt')) as myfile:
      APIKEY=myfile.read().rstrip()
    currentWeather()
    forecast10day()
    alerts()
