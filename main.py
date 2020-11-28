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

    # Fetching the RocketLauncherObject
    print("Fetching RocketLauncherDB")
    rocketLauncerDb = Data.RocketLauncherData()
    if len(items)==0:
        Data.populateDataBase()
    else:
        for i in rocketLauncerDb['result']:
            for k in items:
                # If Record Already Available
                if k.get_column_value(id='numbers').number == i['id']:
                    # Update Old
                    print("Update Old")
                # If Record not Available
                else:
                    # Add New
                    print("Add New")

        time.sleep(10)

#
# starttime = time.time()
# while True:
#     refreshDB()
#     time.sleep(60.0 - ((time.time() - starttime) % 60.0))
#     print("Refresher")

Data.populateDataBase(db.get_board(id='846185373').get_group(title='Pending'))