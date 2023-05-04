# Creating an automated Parking lott
import warnings
import datetime
import math
import dateparser

warnings.filterwarnings(action="ignore")


class Two_wheeler:
    def __init__(self, plate):
        """

        :rtype: object
        """
        self.enterTime = datetime.datetime.now()
        self.plate = plate

    def display(self):
        print(self.plate)


class Four_wheeler:
    def __init__(self, plate):
        self.enterTime = datetime.datetime.now()
        self.plate = plate

    def display(self):
        print(self.plate)


class Membership:
    def __init__(self, name, Subscription_type, Subscription_Registration_date, Subscription_Expiry_date):
        self.Name = name
        self.Subscription_type = Subscription_type
        self.Registration_date = datetime.date.today()
        tdelta = datetime.timedelta(days=365)
        self.Subscription_Expiry_date = self.Registration_date + tdelta


def print_bill():
    if type == 1:
        rs = 15 * total_hours + 5
        print(f'Rate : {rs}/- ')

    elif type == 2:
        if service == 1 and a.lower() == 'y':
            rs = (50 * total_hours - 10) + 35
            print(f'Rate : {rs}/- ')

        elif service == 1 and a.lower() == 'n' and c.lower() == 'y':
            rs = (50 * total_hours - 10) + 35
            print(f'Rate : {rs}/- ')

        elif service == 1 and a.lower() == 'n' and c.lower() == 'n':
            rs = (50 * total_hours - 10) + 80
            print(f'Rate : {rs}/- ')

        elif service == 2:
            rs = (50 * total_hours - 10)
            print(f'Rate : {rs}/- ')
    return rs


service = ""
a = ""
b =""
c =""

def valet_parking():
    global service
    global a
    global b
    global c
    print("Valet Parking is available for cars")
    print('To avail the service press 1')
    print('To reject the service press 2')
    service = int(input())

    if service == 1:
        a = input("Are you a member : Y / N  ")

        if a.lower() == 'y':
            b = input("Choose Membership type : Classic or Premium ")
            if b.lower() not in ('premium', 'classic'):
                print("Invalid entry")
                exit()
            print(f"Membership type : {b}")
            print("Total Bill for Valet Parking is 35/-")

        elif a.lower() == 'n':
            print("Membership option available")
            c = input("Enroll in membership? : Y / N \n")
            if c.lower() == 'y':
                name = input("Enter your name: ")  #########________registration code starts here
                while not name:
                    name = input("Enter a name: ")
                choice = input('Choose the type of Membership : Classic or Premium ')

                if choice.lower() not in ('premium', 'classic'):
                    print("Invalid entry")
                    exit()

                cus_2 = Membership(name, choice, datetime.date.today,
                                   datetime.date.today() + datetime.timedelta(days=365))

                print(f"Name:  {cus_2.Name}")
                print(f"Membership Type: {choice}")
                print(f"Registration date: {cus_2.Registration_date}")
                print(f"Expiry date: {cus_2.Subscription_Expiry_date}\n")
                #print("Total bill for Valet Parking is 35/-\n")
                #print('********Thank you visit again*********')
                return
            elif c.lower() == 'n':
                print("Total bill for Valet Parking is 80/-\n")
                # print('********Thank you visit again*********')
                return
        else:
            print("Invalid entry")
            exit()

    elif service == 2:
        print('Try next time :)')
        return


total_two_wheelers = int(input("Enter the total number of two wheelers parked- "))
total_four_wheelers = int(input("Enter the total number of four wheelers parked- "))

if total_two_wheelers == 500 or total_two_wheelers > 475:
    print("Sorry for inconvinience, you cannot park your two wheeler now!\n")
    exit()

if total_four_wheelers == 100 or total_four_wheelers > 90:
    print("Sorry for inconvenience, you cannot park your four wheeler vehicle now!\n")
    exit()

print("You are warmly welcome:)\n")


go = "yes"
total_hours = 0
total_time = 0
while go == "yes":
    print("Enter the type of vehicle")
    print("Press 1 for Two_wheeler")
    print("Press 2 for Four_wheeler")

    type = int(input("Enter the type of the vehicle to be parked-"))

    if type == 1:
        print("Enter the Plate Number: ")
        new = input()
        tw = Two_wheeler(new)
        print("Time of Entry: ", str(tw.enterTime))

        leave_time = dateparser.parse(input('Enter the leaving time: '), settings={'PREFER_DATES_FROM': 'future'})
        print(leave_time)
        leave_time_diff = leave_time - tw.enterTime
        print(leave_time_diff)
        print(f"time difference = {leave_time_diff} ")

        total_time = leave_time - tw.enterTime
        total_hours = math.ceil(total_time.total_seconds() / 3600) # here? yes where is total hours missing from

    elif type == 2:
        print("Enter the Plate Number")
        new = input()
        fw: Four_wheeler = Four_wheeler(new)
        # valet
        valet_parking()
        print("Time of Entry: ", str(fw.enterTime))

        leave_time = dateparser.parse(input('Enter the leaving time: '), settings={'PREFER_DATES_FROM': 'future'})
        print(leave_time)
        leave_time_diff = leave_time - tw.enterTime
        print(leave_time_diff)
        print(f"time difference = {leave_time_diff} ")

        total_time = leave_time - fw.enterTime
        total_hours = math.ceil(total_time.total_seconds() / 3600)

    else:
        print("Entry Restricted!")
        exit()

    Rs = print_bill()
    print("Type yes to enter another entry, else E to exit: ")
    go = input()

print("*****Displaying_Details*****\n")

if type == 1:
    try:
        print("Two-wheeler number plate: ", tw.plate)
        print("Time of Entry: ", str(tw.enterTime))
    except NameError:
        print("No four-wheeler entered")

elif type == 2:
    try:
        print("Four-wheeler number plate: ", fw.plate)
        print("Time of Entry: ", str(fw.enterTime))
        print("Total bill for Valet Parking is 35/-\n")
    except NameError:
        print("No two-wheeler entered")


