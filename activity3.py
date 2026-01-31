def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if "charlotte" == city:
        return 183
    elif "tampa" == city:
        return 220
    if "pittsburgh" == city:
        return 222
    elif "los angeles" == city:
        return 475

def rental_car_cost(days):
    if days >= 7:
        return 40*days - 50
    elif days >= 3:
        return 40*days - 20
    else:
        return 40*days

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days)+ plane_ride_cost(city) + spending_money

print("Cost of car rental:", rental_car_cost(5))
print("Cost of plane ride:", plane_ride_cost("Los Angeles"))
print("cost of hotel room:", hotel_cost(7))
print("Total trip cost:", trip_cost("Los Angeles", 7, 500))
print(trip_cost("Tampa", 6, 500))