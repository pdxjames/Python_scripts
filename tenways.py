# This is study drill number 3. #

print """

Write a function and do it TEN different ways. REALLY.

We just covered THREE ways in ex19 and they are: 

1) Write the arguments straight into your script directly
2) Or use argv
3) Or ask for user input via raw_input()
4) Define variables and put them inside the script 
	(YES, this is different from the from the first method)
	>> Make sure you understand the difference between these two methods. <<
	
I really prefer prompting the user for input. Thus, the user is defining your variables.
Then insert the user supplied variables into your function and print out the results. 

Remember...if I want to ask the user for the numbers of cheese and crackers,
then I'll need to use int() to convert what I get from raw_input().

5) You can define the variables (say with a 0, if you like)
		and then prompt the user for more info
		and then ADD that number to what you've already defined.
		
6) Call a totally different function to supply some arguments.
7)
8)
9)
10)
"""

print "Way #1: write the function arguments into the script."
print """It looks like this:
def myfunc1(a1, a2):
    print "You told me argument 1 was %r, and argument 2 was %r." % (a1, a2)
myfunc1("Switches", "AccessPoints")"""

def myfunc1(a1, a2):
    print "You told me argument 1 was %r, and argument 2 was %r." % (a1, a2)
myfunc1("Switches", "AccessPoints")

raw_input("Hit enter to continue.")
print ""
print "vvvvvv_Continue Below_vvvvv"
print ""

print ""
print """WAY NUMBER 2: Use the argv statement and supply the arguments when calling the script.
It would look like this:

$ from sys import argv
$ script, arg1, arg2 = argv    
$ print "You told me argument 1 was %r, and argument 2 was %r." % (arg1, arg2)     
and the call would be like 
$ python script.py myscript Switches AccessPoints
"""

raw_input("Hit enter to continue.")
print ""
print "vvvvvv_Continue Below_vvvvv"
print ""

print "Way #3: Ask for user input via raw_input(), as in example 14."
prompt = '>> ' #you *have* to define the prompt
print "Hi. What's your name?"
name = raw_input(prompt)
print "What sort of music do you like?"
music = raw_input(prompt)
def muzak(name, music):
    print "Hi %s, it's good to meet you. I like %s too!" % (name, music)
muzak(name, music)
print ""

print "METHOD NUMBER 4: Define variables and put them inside the script."
arg3 = "_Room_"
arg4 = "_Deployed_Gear_"
def some_function(arg3, arg4):
    print arg3, "           ", arg4
some_function(arg3, arg4)

print ""
print "vvvvvv_Continue Below_vvvvv"
print ""

print """METHOD NUMBER 5 would be to define each variable inside the script, 
and then have the script do the math, the formatting, etc,
and then just spit out the results. Like this below.

"""
pi = 3
ti = 2
pu = 4
tu = 0
phones = pi + pu
tablets = ti + tu
def periphs(phones, tablets):
	periph = phones + tablets
	print "It looks like we have %d peripherials." % (periph)
periphs(phones, tablets)

print ""
print "vvvvvv_Continue Below_vvvvv"
print ""

print """METHOD #6: Use a different function to define the variables that you call
in a fixed script. Say...
def nam():
    print "What room name?"
    room_name = raw_input(prompt)
    print "What gear are we deploying?"
    we_dep = raw_input(prompt)
    print room_name, "     ", we_dep
    
nam()

"""
# this is #6
def nam():
    print "What room name?"
    room_name = raw_input(prompt)
    print "What gear are we deploying?"
    we_dep = raw_input(prompt)
    print room_name, "     ", we_dep
    
nam()

print "" * 2
print "The End." * 4
    
    
    
    
    
    
    
    
    