class Employe:
    def __init__(self):
        print("employe created")
    def __del__(self):
        print("destructor called")
obj = Employe()
del obj