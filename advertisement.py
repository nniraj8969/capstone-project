import random

from platform import *
class Advertisement(Platform):

    def get_advt(self):
        print("\nWelcome User to Advertisement Page".center(60,'*'))
        print("Enter Details to Create Advertisement".center(40, '*'))
        self.ad_id= random.randint(1000, 100000)
        self.ad_title=input("Enter advertisement title")
        #self.ad_duration = input("Enter number of days")
        self.ad_desc = input("Enter description of advt.")
        self.target = input("Enter Audience Type")
        self.area = input("Enter Location for your Advt.")

    def show_advt(self):
        print("\n", "Advertisement Details".center(40, '*'))
        print("Advt. Id: ", self.ad_id)
        print('Advt. Title: ', self.ad_title)
        print('Advt. Description: ', self.ad_desc)
        print('Target Audience: ', self.target)
        print('Advt. Location: ', self.area)
        print("\n".center(60,'*'))
        self.platform_list()



advertisement = Advertisement()

#advertisement.get_advt()
#advertisement.show_advt()
#advertisement.duration()
#advertisement.amount()

