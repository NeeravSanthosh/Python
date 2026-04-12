class parent( object ):
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print(self.name)
        print(self.id)
class employee(parent):
    def __init__(self,name,id,salary):
        self.salary = salary
        parent.__init__(self,name,id)
n = employee("Abdul",10637,1500000)
n.display()
print(n.salary)