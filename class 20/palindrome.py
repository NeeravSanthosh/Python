# palindrome
def palindrome(tupel1):
    s = 0
    e = len(tuple1)-1
    while(s < e):
        if tuple1[s] != tuple1[e]:
            return False
        s+=1
        e-=1
    return True

tuple1 = (1,2,12,12,2,1)
print(tuple1) 
if palindrome(tuple1) :
    print("the given tuple is palindrome") 
else:
    print("the given tuple is not palindrome")         