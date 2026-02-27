# recursion

def recurse(x):
    '''recursion factorial'''

    if x == 1:
        return 1
    else:
        return x * recurse(x-1)
print(recurse.__doc__)
print("the factorial of the number 5 is :",recurse(5))