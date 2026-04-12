shop = input("do you want to buy 5 dollar item y/n")
wallet = 50
def shop12():

    if shop == "y":
        print(wallet-5)
    elif shop == "n":
        print("thanks bye")
    else:
        print("ok")
shop12()