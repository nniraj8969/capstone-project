import re

list = []
file = open("details.txt", 'a')

# print("1.Registration or Signup")
# print("2.Login")

class email:

    # def __init__(self):
    #      print("Welcome to the Registration Page".center(60,'*'))

    def my_func(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        while True:
            e_mail = input("Enter email id: ")
            if (re.fullmatch(regex, e_mail)):
                list.append(e_mail)
                file = open("details.txt", 'a')
                file.write(e_mail)
                file.write("\n")
                print("Email saved")
                break
            else:
                print("Not a valid email")

    def checknum(self):

        while True:
            phone = input("Enter phone no: ")
            r = re.fullmatch('[6-9][0-9]{9}', phone)
            if r != None:
                list.append(phone)
                file = open("details.txt", 'a')
                file.write(phone)
                file.write("\n")
                print('Number saved')
                break
            else:
                print('Not a valid number')

    # atleast 1 letter is from [a-z]
    # atleast 1 letter is from [A-Z]
    # atleast 1character is from [$#@]
    # atleast  1 number from [0-9]
    # Minimum 6,max 12 character
    def checkpassword(self):
        print("password format:\n   atleast 1  [a-z], 1 [A-Z],1 [!%*$#@],1 [0-9]\n   Minimum 6,max 12 character")
        while True:
            password = input("Enter password: ")
            length = True if len(password) > 6 and len(password) < 13 else False
            spec_char = ['@', '#', '$', '%', '!', '*']
            digit = any(char.isdigit() for char in password)
            is_upper = any(char.isupper() for char in password)
            is_lower = any(char.islower() for char in password)
            is_spec_char = any(char in spec_char for char in password)
            isValid = all([length, digit, is_upper, is_lower, is_spec_char])
            if isValid:
                list.append(password)
                file = open("details.txt", 'a')
                file.write(password)
                file.write("\n")

                print("Password saved")
                break
            else:
                print("Enter according to the format")
"""
e = email()
e.my_func()
e.checkpassword()
e.checknum()
"""


