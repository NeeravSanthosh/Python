# multiple exception
try:
    num1 , num2 = eval(input("enter 2 numbers separated by commas :"))
    res = num1 / num2
    print("the answer is ",res)
except SyntaxError as ex:
    print("the numbers to be separated by commas",ex)
except ZeroDivisionError as ex:
    print("number is divided by zero",ex)
except:
    print("an error occured")
else:
    print("no error")
finally:
    print("whatever happens this will  get printed")