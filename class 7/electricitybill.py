# Electricity bill
units = int(input("enter the units consumed :"))
if units < 50:
    amt = units * 2.60 + 25
elif units < 100:
    amt = units * 3.25 + 35
elif units < 200:
    amt = units * 5.26 + 45
else:
    amt = units * 8.45 + 75
print("the electricity bill is rs.",round(amt,2))