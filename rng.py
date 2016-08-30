#random number generator
#figured there was a rng module but built my own. 
#YES, I know this really isn't an rng but it was fun to build something.

print ""
print "Welcome to my random number generator."
print "-----------"*3
print ""
x = int(raw_input("Enter a number between 0 and 10:  "))
y = int(raw_input("Now enter a number between 5 and 10:  "))
name = raw_input("So by the way, what's your name? ")

r = (x*20)/(y+17) + 4
print "Well", name, "your random number is:"
print r
