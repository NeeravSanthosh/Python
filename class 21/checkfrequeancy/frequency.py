# count the frequency
dict1 = {"condingal" : 2, "best" : 2, "try":2,"god":3,"mouse":1}

k = 2
count = 0
for key in dict1:
    if dict1[key] == k:
        count+=1
print(f"the keys which has frequency {k} is {count}")