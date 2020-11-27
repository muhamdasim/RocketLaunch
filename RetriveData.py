import json

import requests


def RocketLauncherData():
    url = 'https://fdo.rocketlaunch.live/json/launches/next/5'
    r = requests.get(url,timeout=30)
    obj = json.loads(r.text)
    return obj

def loadJson():
    global obj
    a = open('latest.json', 'r')
    obj = json.loads(a.read())
    return obj


def populateDataBase(groups):
    for i in obj['result']:
        name=i['vehicle']['name'] + " | " + i['missions'][0]['name']+" " + i['pad']['name']
        time = str(i['win_open'])
        time = time.replace('T', ' ')
        time= time.replace('Z', '')
        location=''
        try:
            location=i['pad']['location']['name'] + ' ' + i['pad']['location']['statename']
        except:
            location=i['pad']['location']['name'] + ' ' + i['pad']['location']['country']
        groups.add_item(name,column_values={"text60":time,"location_or_launchpad":location})
        print(name," Done")


def populateLocation(groups):
    for i in obj['result']:
        try:
            print(i['pad']['location']['name'] + ' ' + i['pad']['location']['statename'])
        except:
            print(i['pad']['location']['name'] + ' ' + i['pad']['location']['country'])


def getTime():
    for i in obj['result']:
        print()
