import random
import string
from enum import Enum, auto
class User():

    def __init__(self):
        self.user_id = random.randint(100, 1000000)
    def get_user(self):
        print("\nEnter details to generate User Information")
        print("---------------------------------------------")
    def get_details(self):

        self.user_name = input("Enter your Name: ")
        self.user_contact = input("Enter your contact number: ")
        self.user_address = input("Enter your address: ")

        print("\nBelow are user Details\n")
        print("----------------------------------")
        print('User ID: ', self.user_id)
        print('User Name: ', self.user_name)
        print('User Contact: ', self.user_contact)
        print('User Address: ', self.user_address)




user = User()
#user.get_user()

