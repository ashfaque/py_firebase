# import required modules
import firebase_admin
from firebase_admin import db, credentials


# authenticate to firebase
cred = credentials.Certificate("synclocation-f73d3-firebase-adminsdk-eg74q-6268812486.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://synclocation-f73d3-default-rtdb.asia-southeast1.firebasedatabase.app/"})



# creating reference to root node, setting path of working node.
ref = db.reference("/")


"""

# retrieving data from root node
_ = ref.get()
print(_)


# retrieve data from the node named "name" in the root node.
_ = db.reference("/name").get()
print(_)


# set operation
db.reference("/videos").set(3)
_ = ref.get()
print(_)


# update operation (update existing value)
db.reference("/").update({"language": "python"})
_ = ref.get()
print(_)


# update operation (add new key value)
db.reference("/").update({"subscribed": True})
_ = ref.get()
print(_)


# push operation, appends new value in the list of a node
db.reference("/titles").push().set("create modern ui in python")
_ = ref.get()
print(_)


# transaction, realtime data update without conflict
def increment_transaction(current_val):
    return current_val + 1

db.reference("/title_count").transaction(increment_transaction)
_ = ref.get()
print(_)


# Deletes a node from the database
db.reference("/node_name").delete()


print(ref.key)

"""


# * Pushing cooridnates in a specific uuid4.

import uuid    # str(uuid.uuid4())
import random
from time import sleep

dummy_coordinates_list = ['22.570791, 89.371220', '23.570791, 90.371220', '24.570791, 91.371220', '25.570791, 92.371220', '26.570791, 93.371220']

def increment_transaction(current_val):
    return random.choice(dummy_coordinates_list)

for i in range(5):    # Loop to simulate realtime coordinates being update every 3 seconds with random coordinates in a specific uuid4.
    db.reference("/3b7b36aa-f686-4c42-8ca0-776da7e3893c").transaction(increment_transaction)
    _ = ref.get()
    print(_)
    sleep(3)



# TODO: Fetching data from a specific uuid4 from realtime database.





# ? https://firebase.google.com/static/docs/reference/admin/python/firebase_admin.db?hl=en



