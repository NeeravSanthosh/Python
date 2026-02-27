# cube of the cube
def cube(x):
    return x * x * x
def divisible_by_three(x):
    if x%3 == 0:
        return cube(x)
    else:
        return False
print("the cube of the 6 is",divisible_by_three(6))
print("the 7 is divisible by 3",divisible_by_three(7))