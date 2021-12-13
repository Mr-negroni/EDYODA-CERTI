import random
import datetime
from datetime import date
import json
def create_random_ID():
    return random.randint(1000,50000)
Modules = {}
def Create_Module():
    M_ID = create_random_ID()
    if M_ID in Modules:
        Create_Module()
    else:
        pass
    print("Please Enter the Module Name ")
    M_name = input()
    print("Module Starting Date :")
    print("Enter the Year ")
    S_Year = int(input())
    print("Enter the Month ")
    S_Month = int(input())
    print("Enter the Day ")
    S_Date = int(input())
    Start_Date = datetime.date(S_Year,S_Month,S_Date)
    print("Please Enter the End date in YYYY-MM-DD format ")
    E_year,E_month,E_date = map(int,input().split('-'))
    End_Date = datetime.date(E_year,E_month,E_date)
    print("Please enter the Units in it")
    M_units = input().split(' ')
    Modules[M_ID]= [M_name,Start_Date,End_Date,M_units]
    
def Manage_Modules():
    print("1. Create a new Module ")
    print("2. View All Modules ")
    print("3. View Modules Details ")
    print("4. Update Modules ")
    print("5. Delete Modules ")
    ch1 = int(input())
    if ch1 ==1:
        Create_Module()
    elif ch1==2 :
        View_all_Modules()
    elif ch1 == 3 :
        View_Modules_Details()
    elif ch1 == 4:
        Update_Module()
    elif ch1 ==5:
        delete_Module()
def View_all_Modules():
    for keys in Modules:
        data = Modules[keys]
        print('Module ID is {}',format(keys))
        print("Module Name is {}",format(data[0]))
        today =  date.today()
        if today<data[2]:
            print(" Status : ONGOING ")
        elif today > data[2]:
            print("Status : COMPLETED ")
        elif today<data[1]:
            print("Status : UPCOMING ")
def View_Modules_Details():
    for keys in Modules:
        data = Modules[keys]
        print("Modules ID is {}",format(keys))
        print("Module Name is {}",format(data[0]))
        print("Module Start Date is ",format(data[1]))
        print("Module End date is ",format(data[2]))
        today =  date.today()
        str(today)
        if today<data[2]:
            print(" Status : ONGOING ")
        elif today > data[2]:
            print("Status : COMPLETED ")
        elif today<data[1]:
            print("Status : UPCOMING ")
        print("Modules Unit are ",format(data[3]))
    
def Update_Module():
    print("Enter the Module ID to Update ")
    Ch_mid = input()
    fp = open('Mod.json')
    Modu = json.load(fp)
    if Ch_mid in Modu:
        data = Modu.get(Ch_mid)
        print("Please Enter the Module Name ")
        data[0] = input()
        print("Module Starting Date :")
        print("Enter the Year ")
        S_Year = int(input())
        print("Enter the Month ")
        S_Month = int(input())
        print("Enter the Day ")
        S_Date = int(input())
        data[1] = datetime.date(S_Year,S_Month,S_Date)
        print("Please Enter the End date in YYYY-MM-DD format ")
        E_year,E_month,E_date = map(int,input().split('-'))
        data[2] = datetime.date(E_year,E_month,E_date)
        print("Please enter the Units in it")
        data[3] = input().split(' ')
    else:
        print("Module ID not Found")
def delete_Module():
    print("enter the Module ID ")
    del_id = input()
    if del_id in Modules:
        del Modules[del_id]
    else:
        print("Module ID not Found")
