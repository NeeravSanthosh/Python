# pass statement
for x in range(10):
    if x%10 == 0:
        print("twist")
    elif x%5 == 0:
        print("fizz")
    elif x%3 == 0:
        print("buzz")
    elif x%2 == 0: 
        pass
    else:
        print(x)   