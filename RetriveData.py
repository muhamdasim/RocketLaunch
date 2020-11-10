import json

import requests


def storeData():
    url = 'https://fdo.rocketlaunch.live/json/launches?key=2aef1609-93cc-4012-9b4f-ed5fa84174eb'
    r = requests.get(url)
    a = open('latest.json', 'w')
    a.write(r.text)
    a.close()


def loadJson():
    global obj
    a = open('latest.json', 'r')
    obj = json.loads(a.read())


def getName():
    for i in obj['result']:
        print(i['vehicle']['name'] + " | " + i['missions'][0]['name'], " ", i['pad']['name'])


def getLocation():
    for i in obj['result']:
        print(i['pad']['location']['name'], ' ', i['pad']['location']['statename'])


def getTime():
    for i in obj['result']:
        k = str(i['win_open'])
        k = k.replace('T', ' ')
        k = k.replace('Z', '')
        print(k)
