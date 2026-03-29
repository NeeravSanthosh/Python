numbersx = [6,7,8,]
numbery = [1,2,3]
result = map(lambda x,y: x + y, numbersx,numbery)
print("addition of lists")
print(list(result))

numberz = [9,8,7,6,5,4]
def sq(nu):
    return  nu * nu
square = list(map(sq,numberz))
print("the square roots of the list are = ")
print(square)