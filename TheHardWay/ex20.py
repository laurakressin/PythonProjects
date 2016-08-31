from sys import argv

script, input_file = argv

# reads off the lines in a file
def print_all(f):
    print f.read()

# sets reference point to the beginning of the file
def rewind(f):
    f.seek(0)

# prints the line number before reading out each line in the file
def print_a_line(line_count, f):
    print line_count, f.readline()

# sets var current_file to the second input in the argv
current_file = open(input_file)

# activating the defs
print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# setting variable current_line
current_line = 1
print_a_line(current_line, current_file)

# incrementing variable current_line
current_line = current_line + 1
print_a_line(current_line, current_file)

# again incrementing variable current_line
current_line = current_line + 1
print_a_line(current_line, current_file)