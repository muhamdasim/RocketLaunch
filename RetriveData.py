import json
import time
import requests


def RocketLauncherData():
    url = 'https://fdo.rocketlaunch.live/json/launches?key=2aef1609-93cc-4012-9b4f-ed5fa84174eb'
    r = requests.get(url, timeout=30)
    obj = json.loads(r.text)
    return obj


def updateOld(groups,id,obj,item):

    for i in obj['result']:
        if id==int(i['id']):
            id = i['id']
            # Name of Event
            name = i['vehicle']['name'] + " | " + i['name']
            # Last Modified
            last_modified = i['modified']
            last_modified = last_modified[:last_modified.find('T')]
            # Company Name
            company = str(i['provider']['name'])
            # Date And Hour
            Date = i['date_str']
            Hour = i['win_open']
            try:
                Hour = Hour[Hour.find('T') + 1:]
                Hour = Hour.replace('Z', '')
            except:
                Hour = ""
            DateAndHour = Date + ' ' + Hour

            # Weather Temperature
            if i['weather_summary'] is not None:
                wind_speed = str(i['weather_summary'])
                x = wind_speed.split('\n')
                temperature = x[1]
            else:
                temperature = "None"

            # Wind Speed

            if i['weather_summary'] is not None:
                wind_speed = str(i['weather_summary'])
                x = wind_speed.split('\n')
                wind_speed = str(x[2])
            else:
                wind_speed = "None"

            # Tags
            tags = ""
            if len(i['tags']) > 0:
                for k in i['tags']:
                    tags = tags + str(k['text']) + " "

                tags = tags[:-1]
            else:
                tags = "None"

            # LaunchPad + Name

            try:
                location = i['pad']['location']['name'] + ' ' + i['pad']['location']['statename']
            except:
                location = i['pad']['location']['name'] + ' ' + i['pad']['location']['country']

            # Filtering Wind and Temp and Name
            wind_speed = wind_speed.replace('Wind:', '')
            temperature = temperature.replace('Temp:', '')
            name = name.replace('"', '')

            print("Testing Updating Old",id)

            item.change_multiple_column_values({"text75": last_modified, "text": temperature, "numbers": id,
                                                 "text0": wind_speed, "tags": tags, "text6": company,
                                                 "text60": DateAndHour, "location_or_launchpad": location})
            print("Done Updating:", id)





def AddNew(groups,id,obj):
    for i in obj['result']:
        if id==int(i['id']):
            id = i['id']
            # Name of Event
            name = i['vehicle']['name'] + " | " + i['name']
            # Last Modified
            last_modified = i['modified']
            last_modified = last_modified[:last_modified.find('T')]
            # Company Name
            company = str(i['provider']['name'])
            # Date And Hour
            Date = i['date_str']
            Hour = i['win_open']
            try:
                Hour = Hour[Hour.find('T') + 1:]
                Hour = Hour.replace('Z', '')
            except:
                Hour = ""
            DateAndHour = Date + ' ' + Hour

            # Weather Temperature
            if i['weather_summary'] is not None:
                wind_speed = str(i['weather_summary'])
                x = wind_speed.split('\n')
                temperature = x[1]
            else:
                temperature = "None"

            # Wind Speed

            if i['weather_summary'] is not None:
                wind_speed = str(i['weather_summary'])
                x = wind_speed.split('\n')
                wind_speed = str(x[2])
            else:
                wind_speed = "None"

            # Tags
            tags = ""
            if len(i['tags']) > 0:
                for k in i['tags']:
                    tags = tags + str(k['text']) + " "

                tags = tags[:-1]
            else:
                tags = "None"

            # LaunchPad + Name

            try:
                location = i['pad']['location']['name'] + ' ' + i['pad']['location']['statename']
            except:
                location = i['pad']['location']['name'] + ' ' + i['pad']['location']['country']

            # Filtering Wind and Temp and Name
            wind_speed = wind_speed.replace('Wind:', '')
            temperature = temperature.replace('Temp:', '')
            name = name.replace('"', '')

            groups.add_item(name, column_values={"text75": last_modified, "text": temperature, "numbers": id,
                                                 "text0": wind_speed, "tags": tags, "text6": company,
                                                 "text60": DateAndHour, "location_or_launchpad": location})

            print("Done Adding New:", id)


def populateDataBase(groups,obj):

    for i in obj['result']:
        id = i['id']
        # Name of Event
        name = i['vehicle']['name'] + " | " + i['name']
        # Last Modified
        last_modified = i['modified']
        last_modified = last_modified[:last_modified.find('T')]
        # Company Name
        company = str(i['provider']['name'])
        # Date And Hour
        Date = i['date_str']
        Hour = i['win_open']
        try:
            Hour = Hour[Hour.find('T') + 1:]
            Hour = Hour.replace('Z', '')
        except:
            Hour = ""
        DateAndHour = Date + ' ' + Hour

        # Weather Temperature
        if i['weather_summary'] is not None:
            wind_speed = str(i['weather_summary'])
            x = wind_speed.split('\n')
            temperature = x[1]
        else:
            temperature = "None"

        # Wind Speed

        if i['weather_summary'] is not None:
            wind_speed = str(i['weather_summary'])
            x = wind_speed.split('\n')
            wind_speed = str(x[2])
        else:
            wind_speed = "None"

        # Tags
        tags = ""
        if len(i['tags']) > 0:
            for k in i['tags']:
                tags = tags + str(k['text']) + " "

            tags = tags[:-1]
        else:
            tags = "None"

        # LaunchPad + Name

        try:
            location = i['pad']['location']['name'] + ' ' + i['pad']['location']['statename']
        except:
            location = i['pad']['location']['name'] + ' ' + i['pad']['location']['country']


        #Filtering Wind and Temp and Name
        wind_speed=wind_speed.replace('Wind:','')
        temperature=temperature.replace('Temp:','')
        name=name.replace('"','')

        groups.add_item(name, column_values={"text75": last_modified, "text": temperature, "numbers": id,
                                             "text0": wind_speed, "tags": tags, "text6": company,
                                             "text60": DateAndHour, "location_or_launchpad": location})

        print("Done:", id)
