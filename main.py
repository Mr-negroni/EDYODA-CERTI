import random
import datetime
from datetime import date
import json
def create_random_ID():
    return random.randint(1000,50000)
Modules = {}
Manager = {}
Students = {}
Unit = {}
Manager['admin']='admin'
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
def Manager_Feature ():
    k =0
    while k == 0:
        print("1. Manage Modules ")
        print("2. Manage Units ")
        print("3. Manage Students ")
        print("4. Exit ")
        choice = int(input())
        if choice == 1:
            Manage_Modules()
        elif choice ==2:
            Manage_Units()
        elif choice ==3:
            Manage_Student()
        elif choice ==4:
            
            k =1
    login()
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
    login()
def View_Todays_Schedule(phone):
    data = Students.get(phone)
    today = date.today()
    datam = Modules.get(data[3])
    if today<datam[2]:
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
    login()
def Create_students():
    print("Enter the Full Name ")
    st_name = input()
    print("Enter the Phone Number ")
    st_phone = input()
    print("Enter the Mail ID ")
    st_email = input()
    print("Enter the Password ")
    st_pwd = input()
    print("Please enter the MOdule ID ")
    st_mid = input()
    Students[st_phone] = [st_name,st_pwd,st_email,st_mid]
    
def Manage_Student():
    print("1. Create a new Student ")
    print("2. View Student Details ")
    print("3. Update Student ")
    print("4. Delete Unit ")
    x = int(input())
    if x ==1:
        Create_students()
    elif x ==2:
        View_student_details()
    elif x==3:
        Update_Student()
    elif x==4:
        Delete_unit()
def View_student_details():
    print("Enter the Phone number of a Student ")
    ph = input()
    if ph in Students:
        datas = Students.get(ph)
        print("Full name of Student is ",format(datas[0]))
        print("Phone Number of the Student is ",format(ph))
        print("Email ID of the Student is ",format(datas[2]))
        print("The Modules list are as follows",format(datas[3]))
    else:
        print("Phone Number not found ")
def Update_Student():
    print("Enter the Phone of The student to update ")
    chph = input()
    
    if chph in Students:
        dataa = Students.get(chph)
        dataa[0] = input("Enter the name of the Student ")
        dataa[2] = input("Enter the mail ID of the Student ")
        dataa[3] = input("Enter the Module List ")
    else:
        print("Given PHone number not Found")
def Delete_unit():
    delph = input("Enter the Phone number of Student whose data needs to be deleted ")
    if delph in Students:
        del Students[delph]
    else:
        print("Given PHone Number not Found")

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
def login():
    print("1. Student")
    print("2. Manager")
    y = int(input())
    if y==1 :
        print("Enter the Name ")
        name = input()
        print("Enter the password ")
        pwd = input()
        print("Enter the Phone Number ")
        pho = input()
        if pho in Students:
            Student_Feature(pho)
        else:
            print('Wrong password, Phone Numbe Combination')
            login()
    elif y==2:
        print("Enter the name ")
        mname = input()
        print("Enter the Password ")
        mpwd = input()
        if mpwd in Manager:
            if mname == Manager[mpwd]:
                Manager_Feature()
    else:
        print('Please the right Correct password and Name COmbination ')
        login() 

print("1. Login")
print("2. Registration")
x = int(input())
if(x==1):
    login()
    
elif(x==2):
    pass
else:
    print("Please enter the Right Choice !")