from user import *
from login import *
from registration import *
from advertisement import *
from platform import *
from payment import *

class HomePage(User, Payment, Advertisement, Platform):
    def __init__(self):
        check = True
        while (check):
            print("-------------Welcome Back-------------------")
            print("1.User Details")
            print("2.Advertisement  Details")
           # print("3.Platform Details")
            print("3.Payment Details")
            print("4.Logout")
            choice = int(input("Press Any Option:"))
            if (choice == 1):
                user = User()
                user.get_user()
                user.get_details()

            elif choice == 2:

                advertisement = Advertisement()

                advertisement.get_advt()
                advertisement.show_advt()
                payment = Payment()
                payment.checkout()
                payment.receipt()





            elif choice == 3:
                payment = Payment()
                payment.checkout()
                payment.receipt()
            elif choice == 4:
                check = False


while True:

    print("\n 1. Signup by Mobile no:".center(50, '*'))
    print("2. Signup by email id:")
    print("3. Login by Mobile no:")
   # print("4. Login by email id:")
    inp = int(input("Choose an Option:"))
    if inp == 1:
        print("Welcome to the Registration Page")
        e = email()

        #e.my_func()
        e.checknum()
        e.checkpassword()

        while True:
            print("Welcome to Login Page:".center(60, '*'))
            call = login()
            #call.set_email()
            call.set_phone()
            call.set_password()
            homepage = HomePage()



    elif inp == 2:
        print("Welcome to the Registration Page".center(60, '*'))
        e = email()

        e.my_func()
       # e.checknum()
        e.checkpassword()

        while True:
            print("Welcome to login Page".center(60, '*'))
            call = login()
            call.set_email()
            # call.set_phone()
            call.set_password()
            homepage = HomePage()

    elif inp == 3:
        print("Welcome to login Page")
        call = login()
        call.set_phone()
        #call.set_email()
        # call.set_phone()
        call.set_password()
        homepage = HomePage()




