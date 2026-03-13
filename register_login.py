from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")

# database
db = client["user_database"]

# collection
users = db["users"]


def register():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    user = {
        "username": username,
        "password": password
    }

    users.insert_one(user)

    print("User Registered Successfully")


def login():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    user = users.find_one({
        "username": username,
        "password": password
    })

    if user:
        print("Login Successful")

    else:
        print("Invalid Username or Password")


while True:

    print("\n1 Register")
    print("2 Login")
    print("3 Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        register()

    elif choice == 2:
        login()

    elif choice == 3:
        break
