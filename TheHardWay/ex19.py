def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enought for a party"
    print "Get a blanket.\n"

# gives numbers to the arguments cheese_count and boxes_of_crackers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# assigning numbers to arguments
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# assigning addition problems to arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# adding number to already assigned variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)