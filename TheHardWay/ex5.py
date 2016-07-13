name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# in centimeters/kilograms
height_cent = height * 2.54
weight_kilo = weight * .45

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "Or %i centimeters." % height_cent
print "He's %d pounds heavy." % weight
print "Or %i kilograms." % weight_kilo
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)