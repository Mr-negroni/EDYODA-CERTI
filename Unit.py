from Module import Modules, create_random_ID
import datetime
from datetime import date
import json

Unit = {}
def create_Unit():
    U_ID = create_random_ID()
    if U_ID in Unit:
        create_Unit()
    else:
        pass
    print("Enter the Unit Type ")
    U_type = input()
    print("Please the Unit Title ")
    U_title = input()
    print("Enter the Starting Date of Unit in YYYY-MM-DD format ")
    SU_year,SU_month,SU_date = map(int,input().split('-'))
    US_date = datetime.date(SU_year,SU_month,SU_date)
    print("Enter the Ending Date of Unit in YYYY-MM-DD format ")
    EU_year,EU_month,EU_date = map(int,input().split('-'))
    UE_date = datetime.date(EU_year,EU_month,EU_date)
    print("Please enter the Module ID ")
    MU_id = input()
    Unit[U_ID]= [U_type,U_title,US_date,UE_date,MU_id]

def Manage_Units():
    print("1. Create a new Unit ")
    print("2. View All unit ")
    print("3. View Unit Details ")
    print("4.Update unit ")
    print("5. Delete unit")
    ch_u = int(input())
    if ch_u==1:
        create_Unit()
    elif ch_u==2:
        View_All_units()
    elif ch_u==3:
        View_unit_details()
    elif ch_u==4:
        update_units()
    elif ch_u == 5:
        delete_units()
def View_All_units():
    for keys in Unit:
        data = Unit.get(keys)
        print("The Unit ID is ",format(keys))
        print("The Unit name is ",format(data[1]))
        print("The Unit Type is",format(data[0]))
        for key in Modules:
            if data[4]== key:
                data1 = Modules[key]
                print("The Module Name is ",format(data1[0]))
def  View_unit_details():
    for keys in Unit:
        data4 = Unit[keys]
        print("Unit ID is ",format(keys))
        print("Unit Type is ",format(data4[0]))
        print("Unit name is ",format(data4[1]))
        print("Unit Start date is ",format(data4[2]))
        print("Unit Ending Date is ",format(data4[3]))
        for key in Modules:
            if data4[4]== key:
                data1 = Modules[key]
                print("The Module Name is ",format(data1[0]))
            today =  date.today()
            if today<data4[3]:
                print(" Status : ONGOING ")
            elif today > data4[3]:
                print("Status : COMPLETED ")
            elif today<data4[2]:
                print("Status : UPCOMING ")
def update_units():
    print("Enter the Unit ID ")
    xuid = input()
    if xuid in Unit:
        datau = Unit.get(xuid)
        print("Enter the Type of Unit ")
        datau[0]=input()
        print("Enter the Title of unit ")
        datau[1] = input()
        print("Enter the Start date of Unit ")
        E_year,E_month,E_date = map(int,input().split('-'))
        datau[2] = datetime.date(E_year,E_month,E_date)
        print("Enter the End date of Unit")
        E_year,E_month,E_date = map(int,input().split('-'))
        datau[3] = datetime.date(E_year,E_month,E_date)
        print("Enter the Module ID ")
        datau[4] = input()
    else:
        print("Module not FOund ")
def delete_units():
    print("Enter the Unit ID to delete the Unit ")
    delu = input()
    if delu in Unit:
        del Unit[delu]
    else:
        print("Unit not Found ")
