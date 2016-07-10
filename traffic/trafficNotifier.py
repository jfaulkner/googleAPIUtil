#!/usr/bin/python

#google.maps.TrafficLayer
#Cville 38.0293, -78.4767
from datetime import datetime
from datetime import timedelta
import time
import json
import googlemaps
import os

HOMEDIR=os.path.expanduser('~')

def commuteEstimate(client, subject, d1, d2, time_threshold):
    now = datetime.now()
    alternates=False
    routes = client.directions(d1, d2,
                               mode="driving",
                               traffic_model="best_guess",
                               departure_time=now)
    route = routes[0]
    distance_to_work=route['legs'][0]['distance']['text'].replace('mi', 'miles')
    time_to_work=route['legs'][0]['duration']['text'].replace('mins', 'minutes')
    time_int = int(float(time_to_work.split(" ")[0]))
    time_str='{0} - Approximately {1} to work. {2} total.'.format(subject, time_to_work, distance_to_work)

    if(time_int >= time_threshold):
        time_str = time_str + " Recommend you take an alternate route."
        alternates=True

    #if(len(route['warnings']) == 0):
    #    warnings='No warnings'
    #else:
    #    warnings=route['warnings']
    send_str = time_str# + " " + warnings
    voicedir = os.path.abspath(HOMEDIR + '/voices/fel')
    cmd_str = ('echo "{0}" | ' + voicedir + ' >/dev/null').format(send_str)
    print(time_str)
    os.system(cmd_str)
    if alternates:
        alternatives(client, d1, d2)

def alternatives(client, d1, d2):
    routes = client.directions(d1, d2,
                               alternatives=True)
    for route in routes:
        summary=route['summary']
        duration=route['legs'][0]['duration']['text'].replace('mins', 'minutes')
        alternatives=summary + " " + duration
        print(alternatives)

if __name__=='__main__':
    api_key=''
    with open(os.path.abspath(HOMEDIR+'/.credentials/trafficAPIKey2.txt')) as myfile:
          api_key=myfile.read().rstrip()
    client = googlemaps.Client(key=api_key)
    d1='PVCC Charlottesville, VA 22902'
    d2=''
    commuteEstimate(client, 'driver1', d1, '1954 Swanson Drive Charlottesville, VA 22901', 20)
    commuteEstimate(client, 'driver2', d1, '3263 Proffit Rd, Charlottesville, VA 22911', 30)
    

