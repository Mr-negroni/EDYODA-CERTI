import json
Students = {}
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
    with open('stud.json','r+') as fp2:
        data = json.load(fp2)
        data.update(Students)
        fp2.seek(0)
        json.dump(data,fp2,default=str)
    fp2.close()
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
    fp2 = open('stud.json')
    stu = json.load(fp2)
    if ph in stu:
        datas = stu.get(ph)
        print("Full name of Student is ",format(datas[0]))
        print("Phone Number of the Student is ",format(ph))
        print("Email ID of the Student is ",format(datas[2]))
        print("The Modules list are as follows",format(datas[3]))
    else:
        print("Phone Number not found ")
def Update_Student():
    print("Enter the Phone of The student to update ")
    chph = input()
    with open('stud.json','r+') as fp2:
        data = json.load(fp2)
    if chph in data:
        dataa = data.get(chph)
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