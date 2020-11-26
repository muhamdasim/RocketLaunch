import RetriveData as DataFetcher
import mondayConnection as Database
import json
#DataFetcher.storeData()
k=DataFetcher.loadJson()

print("Connecting to Monday Database")
try:
    obj=Database.connection()

except:
    print("Unable to Connect to Monday :((")


groups=obj.get_board(id=639957484).get_group(title='Pending')

print("Don")

