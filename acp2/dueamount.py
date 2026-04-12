# program to calculate the due amount
def due_amt(amt_paid,cost_price):
    ramt = amt_paid - cost_price
    return ramt

amt_paid = float(input("enter the amt-paid to the shop-keeper"))
cost_price = float(input("enter the costprice"))
res = due_amt(amt_paid,cost_price)
print(f"the due amount from the shopkeeper is {res}, if the amt paid is {amt_paid}")