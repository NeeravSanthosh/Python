# simple calculator
def add(a,b):
    return a + b

def sub(a,b):
    return  a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a/b

print("1.Addition \n2. Subtraction \n3. Multiplication \n4.Division \nEnter your chioce")
ch = input()
a = int(input("enter the first number :"))
b = int(input("enter the second number :"))
if ch == '1':
    print(f"{a} + {b} = {add(a,b)}")
elif ch == '2':
    print(f"{a} - {b} = {sub(a,b)}")
elif ch == '3':
    print(f"{a} * {b} = {mul(a,b)}")
elif ch == '4':
    print(f"{a} / {b} = {div(a,b)}")
else:
    print('invalid input')