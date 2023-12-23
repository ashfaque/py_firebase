
# * Fetching/Listening data from a specific uuid4 from realtime database.

import firebase_admin
from firebase_admin import db, credentials


# authenticate to firebase
cred = credentials.Certificate("synclocation-f73d3-firebase-adminsdk-eg74q-6268812486.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://synclocation-f73d3-default-rtdb.asia-southeast1.firebasedatabase.app/"})


# Get a reference to the database service
ref = db.reference("/3b7b36aa-f686-4c42-8ca0-776da7e3893c")

# Function to handle data changes in real-time.
def handle_data_change(event):
    print('Fetched Data: ', event.data)
    print(event.path)
    print(event.event_type)
    print('-------')

# Listen the changes on the reference node
ref.listen(handle_data_change)

