import RetriveData as DataFetcher
import mondayConnection as Database
import json
#DataFetcher.storeData()
DataFetcher.loadJson()
#name
#DataFetcher.getName()
#location
#DataFetcher.getLocation()
#time
#DataFetcher.getTime()

print("Connecting to Monday Database")
try:
    obj=Database.connection()

except:
    print("Unable to Connect to Monday :((")


groups=obj.get_board(id=846185373).get_group(title='Pending')

item_name='Asim'
thisdict = {
  "text60": "Ford"
}
groups.add_item("test",text60="finally", location_or_launchpad='fuck')
