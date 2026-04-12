# define a function called trip cost with argument day, money and city
def trip_cost(city, day , spending_money , hotel_cost , plane_ride_cost , rental_car_cost):
    return rental_car_cost(day) + hotel_cost(day) + plane_ride_cost(city) + spending_money
print("the total trip cost to tampa is", trip_cost("tampa",6,500))