import random
import string

from enum import Enum, auto
#from advertisement import *


#from advertisement import *
from platform import *

class Payment(Platform):

    def __init__(self):
        self.Transaction_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(15)])
        #self.platform = {'Facebook': '500', 'Instagram':'400','Twitter':'300'}

    def receipt(self):
        print("\nPayment Details")
        print("--------------------------------")
        print("Transaction Id: ", self.Transaction_id)
        print("Choosen Platform: ", list1[0])
        print("Duration of Advt. ", list2[0])
        self.amount()
        #print('Total Payable Amount')
        #print(self.ad_duration * self.facebook_cost)
        print("Payment Status : Successfull")
        print("==========================")

    def checkout(self):
        print("Welcome to payment page".center(40, '*'))

        self.select_platform()
        self.duration()
        self.amount()

        while True:

            print("1.Go For Payment")
            print('2.Go Back to HomePage')
            choice = int(input("Enter Any option: "))
            if choice == 1:
                while True:
                    print("1.Card Payment")
                    print("2.upi Payment")
                    print("3.Print Receipt")
                    print("4.Go To Home")
                    choice = int(input("Select option: "))
                    if choice == 1:
                        details = int(input("\nEnter your Card number: "))
                        details1 = int(input("Enter your Secret Pin : "))
                        print('Payment done successfully')
                    elif choice ==2:
                        upi = input("\nEnter your upi number: ")
                        print("Redirected to Mobile App open and accept Payment")

                        print("Payment Completed")
                        payment = Payment()
                        #self.checkout()

                    elif choice == 3:
                        print("\nPrint Receipt : ")
                        self.receipt()

                    elif choice == 4:
                        break


            elif choice ==2:

                print("Do Payment later from HomePage")
                break

payment = Payment()
#payment.checkout()
#payment.get_payment()
#payment.receipt()
