
from Module import Manage_Modules
from StudentFeature import Logout
from Studentsss import Manage_Student
from Unit import Manage_Units
Manager = {}
Manager['admin']='admin'
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
    