# and or operator
a = 10
b = 12
c = 0
if a and b and c:
    print("all the variables have boolen value true")
else:
    print("atleast one of the variable have boolean value false")

    a = 2
    b = -2
    c = 0
    if a > 0 or b > 0:
        print("either of the number is greater than zero")
    else:
        print("no variables are greater than zero")