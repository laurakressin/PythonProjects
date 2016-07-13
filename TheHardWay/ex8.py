# variable that will bring in 4 format characters
formatter = "%r %r %r %r"

# prints var formatter with four number variables
print formatter % (1, 2, 3, 4)
# prints var formatter with four number strings
print formatter % ("one", "two", "three", "four")
# prints var formatter with four booleans 
print formatter % (True, False, False, True)
# prints formatter with four more var formatters
print formatter % (formatter, formatter, formatter, formatter)
# prints formatter with four strings from a poem
print formatter % ("I had this thing.", "That you could type up right.", "But it didn't sing.", "So I said goodnight.")