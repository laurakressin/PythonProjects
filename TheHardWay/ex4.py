# total number of cars
cars = 100

# total square foot of space in individual car
space_in_a_car = 4

# total number of drivers
drivers = 30

# total number of passengers
passengers = 90

# number of cars not currently being driven
cars_not_driven = cars - drivers

# number of cars that are being driven
cars_driven = drivers

# gives total square foot area available for carpool
carpool_capacity = cars_driven * space_in_a_car

# calculates average number of passengers per car
average_passengers_per_car = passengers / cars_driven

# prints results
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

