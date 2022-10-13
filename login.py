from registration import *

class login(email):
    def __init__(self, email="", password="", phone=""):
        super().__init__()
        self.email = email
        self.phone = phone
        self.password = password

    def set_email(self):
        while True:
            email = input("Enter email: ")
            file = open("details.txt", 'r')
            data = file.read()
            if email in data:
                self.email = email
                break
            elif email not in list:
                print("It is not a registered email or phone number ")
                break
            else:
                print("unmatched email")

    def set_phone(self):
        while True:
            phone = input("Enter your Mobile Number: ")
            file = open("details.txt", 'r')
            data = file.read()
            if phone in data:
                self.phone = phone
                break
            elif phone not in list:
                print("It is not a registered phone number ")
                break
            else:
                print("unmatched phone number")

    def set_password(self):
        while True:
            password = input("Enter password: ")
            file = open("details.txt", 'r')
            data = file.read()
            if password in data:
                self.password = password
                break
            else:
                print("unmatched password")


# call=login()

# e=email()
# call.my_func()
# call.checknum()
# call.checkpassword()
# print("\n\n")
# print("Welcome to Login_Page".center(60,'*'))
# call.set_email()
# call.set_password()
