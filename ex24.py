print "\n\nLet's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

print "\n\nHere's some text. \nHere's some text on a newline. \n\tHere's some text on a newline and indented with a tab.\n\n" 

poem = """      
\tThe lovely world
with logic so firmly planted
cannot discern \n the seeds of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five
print "\n--------------"

#received my email from PyMOTW 3, which discussed the pydoc test module. Cool!
#so looked at the examples there and thought I'd try it here.
#putting this broken code in to test it
seven = 10 - 4 + 39
print "This should be eight: %s" % seven
print "\n--------------"

#yeah, I get it, we're defining the function 'secret formula' here AND passing the var called 'started'
#this took me a bit. vars are usually called x or y, but I suppose abc, or a134, or starabc, or started
#will work too.

#what's confusing is that the var 'started' is NOT defined.
#well, after breaking it by subbing xyz for started, I see that started is used below, doh!

def secret_formula(xyz):
    jelly_beans = xyz * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

#======================================

print "Please enter a positive whole number between 0 and 1 million below.\n"
n = int(raw_input('==>'))
start_point = n
#ok james, as an experiment, lets make n = startpoint. I think it will break things.
#ha! I was right! because what we did is RE-define n. 
#if you use the python interpreter and say x = 5, then do x = 7, then print x, 
#you'll get 7 because you've RE-defined x. 
#so putting it back to be correct
#n = start_point

#this is for trouble-shooting
#print "\n==="
#print n
#print "==="

#start_point = raw_input("Enter a positive whole number between 0 and 1 million: ")
beans, jars, crates, = secret_formula(start_point)

print "\nWith a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "\n\nWe can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

print "\n--------------"
print "And here's the color breakdown:" 

def colors():
    red = jelly_beans * 43.5
    yellow = jelly_beans * 27.8
    green = jelly_beans * 16.3
    blue = jelly_beans * 12.4
    print "\nHmmm... looks like we have %d red jelly beans, %d yellows, %d greens, and %d blue ones.\n\n" % (red, yellow, green, blue)

print "Yo! This is the right version."

jelly_beans = start_point
#print start_point   #used for trouble-shooting
#print jelly_beans   #used for trouble-shooting

colors()

#adding doctest for practice

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#eof
