num = int(input("enter the number"))
count = 0
temp = num
while temp > 0:
    count +=1
    temp = temp//10
print(count)