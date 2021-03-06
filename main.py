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
        try:
            print("Connecting to Groups")
            groups = db.get_board(id='846185373').get_group(title='Pending')
            items =db.get_board(id='846185373').get_items()
            current_ids = []
            item_pointer=[]
            if len(items)>0:
                print("Extraing Ids")

                for i in items:
                        current_ids.append(int(i.get_column_value(id='numbers').number))
                        item_pointer.append(i)




            rocketLauncherDb = Data.RocketLauncherData()

            if len(items) == 0:
                #Pending Group Always;
                Data.populateDataBase(groups,rocketLauncherDb)
            else:
                id_to_update=None
                item_to_update=None
                for i in rocketLauncherDb['result']:
                    found = False
                    for k in current_ids:
                        # If Record Already Available
                        if k == i['id']:
                            # Update Old
                            found = True
                            id_to_update=k
                            item_to_update=item_pointer[current_ids.index(id_to_update)]
                            break
                    if found:
                        Data.updateOld(groups, id_to_update, rocketLauncherDb,item_to_update)

                    else:
                        print("Adding New:", i['id'])
                        Data.AddNew(groups, int(i['id']),rocketLauncherDb)
                print("All Done")

                time.sleep(10)
        except:
            time.sleep(60)
            refreshDB()


starttime = time.time()
while True:
    refreshDB()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
    print("Refresher")



