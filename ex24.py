print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

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
print "\n\n------------"

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

print "Please enter a number between 0 and 1000000 below.\n"
n = int(raw_input('==>'))
start_point = n
#ok james, as an experiment, lets make n = startpoint. I think it will break things.
#ha! I was right! because what we did is RE-define n. 
#if you use the python interpreter and say x = 5, then do x = 7, then print x, 
#you'll get 7 because you've RE-defined x. 
#so putting it back to be correct
#n = start_point

print "\n==="
print n
print "==="

#start_point = raw_input("Choose a number between 0 and one million: ")
beans, jars, crates, = secret_formula(start_point)

print "\nWith a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "\n\nWe can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

print "\n--------------"
print "Minor victories. still confused about how to pass vars in functions. I'll try some more.\n"
 
def colors():
    red = jelly_beans * .5
    yellow = jelly_beans * .25
    green = jelly_beans * .125
    blue = jelly_beans * .125
    print "\nHmmm... looks like we have %d red jelly beans, %d yellows, %d greens, and %d blue ones." % (red, yellow, green, blue)

colors()
#eof
