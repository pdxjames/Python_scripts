def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
    
print "\nLets do some math with functions."

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
print "--------------------------------------------"

#extra credit puzzle
print "\nHere is a puzzle for you:"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# 'what' is the function of add (with the vars 'age' as the first var, and the second var inside add
# as the function called multiply. Now... 'multiply' is also a function, and we pass it a var
# along with a function as the second variable. cool! :)

print "That becomes: ", what, "Can you do it by hand?"

#================================

print "--------------------------------------------"
def myfunc(x, y):
    print x - y
        
myfunc(2016, 1967)

#======================

print "--------------------------------------------"
def f2(m, n):
    print "I'm guessing you're", years, "years old."

m = int(raw_input("What year is it now? "))
n = int(raw_input("In what year were you born? ")) 
years = m - n
f2(m,n)

#eof
    

