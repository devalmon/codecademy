import sys

def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if (city == "Charlotte"):
        return 183
    elif (city == "Tampa"):
        return 220
    elif (city == "Pittsburgh"):
        return 222
    elif (city == "Los Angeles"):
        return 475
        
def rental_car_cost(days):
    cost = 40 * days
    if (days >= 7):
        return cost - 50
    elif (days >= 3 and days < 7):
        return cost - 20
    else:
        return cost
        
def trip_cost(city, days):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days)

print trip_cost(sys.argv[1], int(sys.argv[2]))