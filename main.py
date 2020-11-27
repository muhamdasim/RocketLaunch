import RetriveData as DataFetcher
import time
import mondayConnection as Database

print("Connecting to Monday.com")
try:
    db=Database.connection()
    print("Successfully Connected to Monday.com")

except:
    "Unable to Connect to Monday.com"


def refreshDB():
    print("Connecting to Groups")
    groups=db.get_board(id='846185373').get_group(title='Pending')
    items=groups.get_items()
    for i in items:
        if i.get_column_value(id='numbers').number==1234:
            print("Found")
        else:
            print("Not Found")



starttime = time.time()
while True:
     refreshDB()
     time.sleep(10.0 - ((time.time() - starttime) % 10.0))
     print("Refresher")