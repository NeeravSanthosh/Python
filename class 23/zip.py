# elements
set1 = [1,2,3,4,5]
set2 = ['a','b','c','d','e']
s3 = list(zip(set1,set2))
print(s3)
ans = list(zip(set1,set2[::-1]))
print(ans)

# dictionary
s = ['infosys','reliance','tcs']
p = ['2000','2500','3000']
n_dict = {s:p for s,p in zip(s,p)}
print(n_dict)