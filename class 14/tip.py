# tip to the waiter

def tip_calculate(amt,tip_per):
     tip_amt = amt * tip_per/100
     t_amt = amt + tip_amt
     print("the amt is :",amt)
     print("the tip is",tip_amt)
     print("the total bill amt is",t_amt)
tip_calculate(1000,10)
