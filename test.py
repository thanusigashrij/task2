import sys
from pymongo import MongoClient

# Connect to MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
    # Force a connection check
    client.admin.command('ping')
    print("Connected")
except Exception as err:
    print("Connection error:", err)
    sys.exit(1)

# Select database and collection
db = client["mydatabase"]
users_collection = db["users"]

attempt = 0

while attempt < 3:
    name = input("enter the name: ")
    password = input("enter the password: ")

    if not name.isalpha() or not password.isdigit():
        print("Invalid input, try again")
        attempt += 1
    else:
        print("correct name")
        print("correct password")
        
        # Save to database
        user_data = {"name": name, "password": password}
        users_collection.insert_one(user_data)
        print("Registered and saved to database successfully")
        print("done")
        break

if attempt == 3:
    print("register cannot be done")