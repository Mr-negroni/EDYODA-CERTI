from ManFeature import Manager, Manager_Feature
from StudentFeature import Student_Feature
from Studentsss import Students
import json


print("1. Login")
print("2. Registration")
x = int(input())
if(x==1):
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
        fp2 = open('stud.json')
        stu = json.load(fp2)
        if pho in stu:
            Student_Feature(pho)
        else:
            print('Wrong password, Phone Numbe Combination')
        fp2.close()
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

    
elif(x==2):
    pass
else:
    print("Please enter the Right Choice !")