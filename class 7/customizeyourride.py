# selection of ride
choice = input("enter your choice \n1.bike \n2.car")
if choice == "1":
    ch = input("enter you bike \n1.Yamaha \n2. Bullet")
    if ch == "1":
        print("you have selected yamaha for your ride")
    elif ch == "2":
        print("you have selected bullet for your ride")
    else:
        print("invalid")
elif choice == "2":
     ch = input("enter you car \n1.Porche \n2.BMW")
     if ch == "1":
        print("you have selected Porche for your ride")
     elif ch == "2":
        print("you have selected BMW for your ride")
     else:
       print("invalid")
else:
       print("invalid")

