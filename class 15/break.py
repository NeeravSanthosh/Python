# check 'a' is present or not
str1 = input("enter a phrase : ")
for i in str1:
    if i.lower() == 'a':
        print("A is present in",str1)
        break
else:
    print("ai is not present is ",str1)