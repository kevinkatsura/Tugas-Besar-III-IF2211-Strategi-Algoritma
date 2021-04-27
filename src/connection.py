import pyrebase


class Connection:
    def __init__(self):
        # DATABASE CONFIGURATION
        firebaseConfig = {
            "apiKey": "AIzaSyBfFabmoRfOV0MG5_FRjmXbtt_3tY38acQ",
            "authDomain": "easy-travel-7a9e7.firebaseapp.com",
            "databaseURL": "https://easy-travel-7a9e7-default-rtdb.firebaseio.com",
            "projectId": "easy-travel-7a9e7",
            "storageBucket": "easy-travel-7a9e7.appspot.com",
            "messagingSenderId": "585987761614",
            "appId": "1:585987761614:web:94de4acd5324708753379f",
            "measurementId": "G-J529MZBL7M"
        }

        # DATABASE INITIAL CONNECTION
        conn = pyrebase.initialize_app(firebaseConfig)
        self.db = conn.database()
