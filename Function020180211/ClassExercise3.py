# Let's use functions to calculate your trip's costs:


# Define a function called hotelCost with one argument nights as input. The hotel costs $140 per night.
# So, the function hotel_cost should return 140 * nights.
def hotelCost(day):
    return 140 * day

# Define a function called planeCost that takes a string, city, as input.
# The function should return a different price depending on the location, similar to the code example above.
# Below are the valid destinations and their corresponding round-trip prices.
# "Charlotte": 183
# "Tampa": 220
# "Pittsburgh": 222
# "Los Angeles": 475
def planeCost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475

# Define a function called rentalCarCost with an argument called days.
# Calculate the cost of renting the car: Every day you rent the car costs $40.(cost=40*days)
# if you rent the car for 7 or more days, you get $50 off your total(cost-=50).
# Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total.
# You cannot get both of the abaove discounts. Return that cost.
def rentalCost(day):
    if day < 3:
        return 40 * day
    elif day >= 7:
        return 40 * day - 50
    else:
        return 40 * day - 20


# Define a function called trip_cost that takes two arguments, city and days.
# Like the example above, have your function return the sum of
# calling the rentalCost(days), hotelCost(days), and planeCost(city) functions.

def tripCost(numOfDays, city):
    totalCost = rentalCost(numOfDays) + planeCost(city) + hotelCost(numOfDays)
    return totalCost

print(tripCost(10, 'Tampa'))
