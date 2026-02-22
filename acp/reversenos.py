# reverse the string
str1 = input("enter the number :")
rev = ''
for i in str1:
    rev = i + rev
print(f"the reverse of {str1} is {rev}")