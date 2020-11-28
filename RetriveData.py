import json

import requests


def RocketLauncherData():
    url = 'https://fdo.rocketlaunch.live/json/launches?key=2aef1609-93cc-4012-9b4f-ed5fa84174eb'
    r = requests.get(url,timeout=30)
    obj = json.loads(r.text)
    return obj




def populateDataBase(groups):
    obj=RocketLauncherData()
    for i in obj['result']:
        #Name of Event
        name=i['vehicle']['name'] + " | " + i['name']
        #Last Modified
        last_modified=i['modified']
        last_modified=last_modified[:last_modified.find('T')]
        #Company Name
        company=i['provider']['name']
        #Date And Hour
        Date=i['date_str']
        Hour=i['win_open']
        try:
            Hour=Hour[Hour.find('T')+1:]
            Hour=Hour.replace('Z','')
        except:
            Hour=""
        DateAndHour=Date+' '+Hour

        #Weather Temperature
        if i['weather_summary'] is not None:
            wind_speed=str(i['weather_summary'])
            x=wind_speed.split('\n')
            temperature=x[1]
        else:
            temperature="None"

        #Wind Speed

        if i['weather_summary'] is not None:
            wind_speed=str(i['weather_summary'])
            x=wind_speed.split('\n')
            wind_speed=x[2]
        else:
            wind_speed="None"

        #Tags



        # time = str(i['win_open'])
        # time = time.replace('T', ' ')
        # time= time.replace('Z', '')
        # location=''
        # try:
        #     location=i['pad']['location']['name'] + ' ' + i['pad']['location']['statename']
        # except:
        #     location=i['pad']['location']['name'] + ' ' + i['pad']['location']['country']
        # groups.add_item(name,column_values={"text60":time,"location_or_launchpad":location})
        print(temperature," Done")


def populateLocation(groups):
    for i in obj['result']:
        try:
            print(i['pad']['location']['name'] + ' ' + i['pad']['location']['statename'])
        except:
            print(i['pad']['location']['name'] + ' ' + i['pad']['location']['country'])


def getTime():
    for i in obj['result']:
        print()
