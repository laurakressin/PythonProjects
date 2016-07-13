# Introduction of game
import string
room = 0
while room == 0: 
	print("---------------------------------------------------------")
	print("---------------------------------------------------------")
	print("Welcome to In the Night!")
	print("---------------------------------------------------------")
	print("---------------------------------------------------------")
	#asks for users name
	name = raw_input("What is your name? ")
	#asks for gender
	gender = raw_input("Do you prefer to be called a he, she, or they? ")
	
	#adds verb with name
	verbName = name + " is"
	#capitalizes pronoun
	capGender = gender.capitalize()
	#applies correct verb to pronoun
	if gender == "they":
		verbGender = gender + " are"
		verbCapGender = capGender + " are"
		verbEnding = ""
	else:
		verbGender = gender + " is"
		verbCapGender = capGender + " is"
		verbEnding = "s"

	print("---------------------------------------------------------")
	print("---------------------------------------------------------")
	print "%s sits up in bed, wide awake, as if aroused by a loud noise...but the house is completely silent." % (name)
	print "\t%s decide%s to go investigate." % (capGender, verbEnding)
	print "%s get%s out of bed and walk%s into the hallway" % (capGender, verbEnding, verbEnding)
	print "There are two doors(1 and 2) on the left side, two doors(3 and 4) on the right side, and one door(5) at the end of the hall"
	print("---------------------------------------------------------")
	#Goes into hallway loop
	room = 6
	
#Choice Number 1
while room == 6:
	num1 = raw_input("Which door should you open: 1, 2, 3, 4 or 5? ")
	if num1 == "1":
		room = 1
	if num1 == 2:
		room = 2
	if num1 == 3:
		room = 3
	if num1 == 4:
		room = 4
	if num1 == 5:
		room = 5
	else:
		print("---------------------------------------------------------")
		print "\tSorry, but you have to type 1, 2, 3, 4, or 5."
		print("---------------------------------------------------------")

		
#Room Number 1
while room == 1:
	print("---------------------------------------------------------")
	print("---------------------------------------------------------")
	# Room 1 Description
	print "%s enters the first room" % (name)
	print """
The room appears to be a study.  
The walls are covered with shelves of books.
There's a large wooden desk towards the back of the room, covered with in papers, folders and books
A computer sits on top.  The screen appears to be black.
A fire place sits to the right of door.  
The mantel above the fire place is covered with pictures, knick knacks and a lone card.
	"""
	inRoom = True

	while inRoom == True:
		print("---------------------------------------------------------")
		rm1Item = raw_input("What item would you like to examine?: desk, mantel, bookshelf, computer or card?  If you want to exit the room, type 'none'. ")
		if rm1Item.lower() == "desk":
			print "the desk"
		if rm1Item.lower() == "mantel":
			print "the mantel"
		if rm1Item.lower() == "bookshelf":
			print "the bookshelf"
		if rm1Item.lower() == "computer":
			print "the computer"
		if rm1Item.lower() == "card":
			print "the card"
		if rm1Item.lower() == "none":
			print "%s returns to the hallway" % (name)
			inRoom = False
			room = 6
		else:
			print("---------------------------------------------------------")
			print "\tSorry, but you have to type desk, mantel, bookshelf, computer, card or none."
			print("---------------------------------------------------------")
	
#Room Number 2
while room == 2:
	print("---------------------------------------------------------")
	print("---------------------------------------------------------")
	print "%s enters the second room" % (name)
	print("---------------------------------------------------------")
	
#Room Number 3
while room == 3:
	print("---------------------------------------------------------")
	print("---------------------------------------------------------")
	print "%s enters the third room" % (name)
	print("---------------------------------------------------------")
	
#Room Number 4
while room == 4:
	print("---------------------------------------------------------")
	print("---------------------------------------------------------")
	print "%s enters the fourth room" % (name)
	print("---------------------------------------------------------")
	
#Room Number 5
while room == 5:
	print("---------------------------------------------------------")
	print("---------------------------------------------------------")
	print "The door at the end of the hall appears to be locked from the other side"
	print("---------------------------------------------------------")
	
	
	
