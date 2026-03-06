# value error
try :
    num = int(input("enter a number :"))
    print("the given number is",num)
except ValueError as ex:
    print("a error occurs",ex)