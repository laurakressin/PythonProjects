def menu():
	# print "Hello World!"
	print "Hello Again"
	print "I like typing this."
	print "This is fun."
	print 'Yay! Printing.'
	print "I'd much rather you 'not'."
	print 'I "said" do not touch this.'
	# read()

def read():
	with open('ex1.py', 'r') as f:
		lines = f.readlines()
		print lines[1]
		
# menu()

# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

# print "I could have code like this." # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

# print "This will run."

# Line 29 describes following activity
# print "I will now count my chickens:"

# Line 32 is giving the total for Hens.  Line 33 gives total of Roosters
# print "Hens", 25 + 30 / 6
# print "Roosters", 100 - 25 * 3 % 4

# Line 36 explains what will be counted next: eggs
# print "Now I will count the eggs:"

# Gives total for eggs
# print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# Gives string that evaluates in line 45
# print "Is it true that 3 + 2 < 5 - 7?"

# Gives math problem from string to evaluate
# print 3 + 2 < 5 - 7

# Line 48 evaluates the first part of Line 45.  Line 49 evaluates the second part of line 45
# print "What is 3 + 2?", 3 + 2
# print "What is 5 - 7?", 5 - 7

# Understanding of return of Line 45
# print "Oh, that's why it's False."

# Prompts continuation of excercise
print "How about some more."

# Lines 58 - 60 give different math problems to evaluate as True or False
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

#Study Drill Calculation
print float(9)
print float(1/3)
print float(1.0/3.0)