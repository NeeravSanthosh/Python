# exam eligibility check
mc = input("enter the student has medical cause (y/n) :")
if mc.lower() == 'y':
    print("the student is allowed to write the exam")
elif mc.lower() == 'n':
    att = int(input("enter the attendance :"))
    if att >=75:
        print("the student is allowed to write the exam")
    else:
        print("the student is not allowed to write the exam")
else:
     nprint("invalid input")