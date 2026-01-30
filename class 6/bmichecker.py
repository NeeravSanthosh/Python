#bmi checker
w = float(input("enter your weight in KGs :"))
h = float(input("enter your weight in meteres :"))

bmi = w/(h*h)
print("your bmi is",bmi)
if bmi <18.5:
    print("you are under weight")
elif bmi <25:
 print("you are healthy")
elif bmi <30:
 print("you are over weight")
else:
 print("you are obese")
