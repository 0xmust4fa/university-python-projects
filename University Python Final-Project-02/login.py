# username & password
USERNAME = "admin"
PASSWORD = "admin123"

def login_system():
    attempts = 0
    
    while attempts < 3:
        user = input("Enter username: ")
        pwd = input("Enter password: ")

        if user == USERNAME and pwd == PASSWORD:
            print("Login successful!")
            return True

        attempts += 1
        print("Incorrect username or password!")

    print("Too many attempts! Exiting...")
    return False
