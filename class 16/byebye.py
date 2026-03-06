# bye bye
try:
    valid = False
    while not valid:
        n = int(input("enter the number"))
        while n%2 == 0:
            print("bye")
        print(n,"the number is odd")
        valid = True
except ValueError as ex:
    print('the value is entered is wrong')