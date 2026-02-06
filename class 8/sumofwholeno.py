# sum of whole numbers
n = int(input("enter the numbers :"))
sum = 0
for i in range(0,n+1):
    sum = sum + i
print(f"the sum of whole number up to {n} is {sum}")