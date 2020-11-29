import RetriveData as Data
import time
import mondayConnection as Database

print("Connecting to Monday.com")
try:
    db = Database.connection()
    print("Successfully Connected to Monday.com")

except:
    "Unable to Connect to Monday.com"


def refreshDB():
    print("Connecting to Groups")
    groups = db.get_board(id='846185373').get_group(title='Pending')
    items = groups.get_items()
    current_ids = []
    print("Extraing Ids")
    for i in items:
        current_ids.append(int(i.get_column_value(id='numbers').number))

    rocketLauncherDb = Data.RocketLauncherData()

    if len(items) == 0:
        Data.populateDataBase(groups)
    else:
        for i in rocketLauncherDb['result']:
            found = False
            for k in current_ids:
                # If Record Already Available
                if k == i['id']:
                    # Update Old
                    found = True
                    print("Founded:", i['id'])
                    break
            if found:
                print("Updating OLD:", i['id'])

            else:
                print("Adding New:", i['id'])
                Data.AddNew(groups, int(i['id']))
        print("Fuck OFF")

        time.sleep(10)


starttime = time.time()
while True:
    refreshDB()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
    print("Refresher")


# Data.populateDataBase(db.get_board(id='846185373').get_group(title='Pending'))

groups = db.get_board(id='846185373').get_group(title='Pending')
