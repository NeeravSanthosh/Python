# list comprehension for odd numbers
list = [9,22,3,4,11,92,48,20]
print('odd number from the list')
list3 = [i for i in list if i%2 == 1]
print(list3)
name = ["neerav","santhosh","niranj"]
name_list = [i.capitalize() for i in name]
print(name_list)