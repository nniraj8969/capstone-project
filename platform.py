#from user import *
#from advertisement import *
list1 = ['facebook', 'instagram', 'twitter']
list2 = []
class Platform(Exception):

    def platform_list(self):
        print("Listed Advertisement Platform")
        print("\n".center(50,'*'))
        print("1.Facebook")
        print('2.Instagram ')
        print('3.Twitter ')

    def select_platform(self):
        self.platform = input("Enter Your Advt. Platform: ")
        if self.platform in list1:
            print(self.platform)

        list1.append(self.platform)
        try:
            x = input("Enter your Favorite Advt. Platform")
            if x not in list1:
                raise Platform(x)
        except Platform as e:
            print("Your favourite Platform is not in our list. Please Provide values from Listed platform")

        #print(list1)


    def cost(self):
        self.facebook_cost = 400
        self.instagram_cost = 500
        self.twitter_cost = 300


    def duration(self):
        try:
            self.ad_duration = input("Enter Duration of Advt. : ")
            self.ad_duration = int(self.ad_duration)
            list2.append(self.ad_duration)
            #print(list2)
        except:
            print("Default Except: Please Provide valid input only")

    def amount(self):
        #self.duration()
        self.cost()
        #self.select_platform()




        if self.platform.lower() == 'facebook':
            if (type(self.ad_duration) == type('string')):
                print("Enter integer value only")
            # amt = math.prod(self.ad_duration * self.facebook_cost)
            else:
                print('Total Payable Amount: ',self.ad_duration * self.facebook_cost)

        elif (self.platform.lower() == 'instagram'):
            print('Total Payable Amount: ',self.ad_duration * self.instagram_cost)

        elif (self.platform.lower() == 'twitter'):
            print('Total Payable Amount: ',self.ad_duration * self.twitter_cost)

        #else:
        #   print("Choose from the Above Platform")
        # amt = math.prod(self)
        #print(self.ad_duration)

    """
    def platform1(self):
        self.ad_duration = input("Enter numner of days")
        check = True
        while (check):

            print("Welcome To Advertisement Page".center(60, '*'))
            print("\n-------------Select Your Advertisement Platform-------------------")
            print("1.Facebook")
            print("2.Instagram")
            print("3.Twitter")
            print("4.Go Back")

            choice = int(input("Press Any Option:"))
            if (choice == 1):
                print("Your selected platform for advertisement is : Facebook")
                print("Facebook cost ", self.facebook_cost)
                #advertisement = Advertisement()



            elif choice == 2:
                print("Your selected platform for advertisement is : Instagram")
                print('Instagram cost ', self.instagram_cost)
               # advertisement = Advertisement()


            elif choice == 3:
                print("Your selected platform for advertisement is : twitter")
                print('Twitter Cost ', self.twitter_cost)
                #advertisement = Advertisement()

            elif choice == 4:
                check = False
        """

platform1 = Platform()
#platform1.platform1()
#platform1.platform_list()
#platform1.select_platform()
#platform1.cost()
#platform1.duration()
#platform1.amount()
