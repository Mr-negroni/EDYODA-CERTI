
from Module import Modules
from Studentsss import Students
import datetime
from datetime import date

from Unit import Unit


def Student_Feature(phone):
    k =0
    while k==0:
        print("1. View Todays Schedule")
        print("2. View My Modules ")
        print("3. Update Profile ")
        print("4.Logout ")
        chose = int(input())
        if chose ==1:
            View_Todays_Schedule(phone)
        elif chose ==2:
            View_My_Modules(phone)
        elif chose ==3 :
            Update_Profile(phone)
        elif chose ==4:
            
            k=1
    
def View_Todays_Schedule(phone):
    data = Students.get(phone)
    today = datetime.date()
    datam = Modules.get(data[3])
    if today > datam[1] and today<datam[2]:
        for keys in Unit:
            info = Unit[keys]
            if info[4]==data[3]:
                print("Module Name is ",format(info[4]))
                print("Unit Type is ",format(info[0]))
                print("Unit Name is ",format(info[1]))
def View_My_Modules(phone):
    if phone in Students:
        datas = Students.get(phone)
        print("Modules Enrolled are ",format(datas[3]))
def Update_Profile(phone):
    if phone in Students:
        datass = Students.get(phone)
        datass[0] = input("Ente the name ")
        datass[1] = input("Enter the new passwords ")
        datass[2] = input("Enter the maul ID ")
        datass[3] = input("Enter the Module ID ")
def Logout():
    exit()


