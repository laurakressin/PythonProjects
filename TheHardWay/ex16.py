# importing argv
from sys import argv

# assigning script and filename to argv
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# continues if user hits enter, otherwise exits program
raw_input("?")

# open the file to writes
print "Opening the file..."
target = open(filename, 'w')

# empties the file
print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

# User inputs three different lines
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# writes the three lines into the file with a line break between lines
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# closes the file
print "And finally, we close it."
target.close()