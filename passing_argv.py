#be sure to pass the user_name arg when calling the script
#
from sys import argv

script, user_name = argv
prompt = '>> '

print "Hi %s, I'm the %s script." % (user_name, script)
#print "I'd like to ask you a few questions."
print "Do you mind if I ask you a few questions?"
yon = raw_input(prompt)

print "OK %s, where do you live?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "And what sort of music do you like?"
music = raw_input(prompt)

print "Last question %s. Do you find this interesting?" % user_name
likes = raw_input(prompt)

print """
Hmmm.... well %s, you told me you live in %s and you have a %s computer.
I hope you like it. You also said you like %s music. Me too! 
I like you %s, I really like you! 
""" % (user_name, lives, computer, music, user_name)
