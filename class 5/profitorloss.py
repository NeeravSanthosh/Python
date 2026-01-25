# profit or loss
cp = float(input("enter the cost price :"))
sp = float (input("enter the selling price"))
if cp < sp :
    print(f"rs.{sp-cp} is the profit")
else:
    print(f"rs.{cp-sp} is the loss")