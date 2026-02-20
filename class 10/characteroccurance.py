# cehck character in a string
str1 = input("enter the phrase :")
char1 = input("enter the character to count :")
count = 0
i = 0
while(i < len(str1)):
    if str1[i] == char1:
        count +=1
    i+=1
print(f"the no. of character {char1} in {str1} is {count} ")
