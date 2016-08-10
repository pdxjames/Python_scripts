# >> Mad_lib #1 <<
#So I made a madlib based on this modified nursery rhyme:    
#Jack and Jill went up the hill to fetch a pail of water.
#Jack fell down and broke his crown,
#And Jill was a smartie pants and said,
#"You dork. You don't go up hill to get water!"

#from example12.py
#age = raw_input("How old are you? ")
#height = raw_input("How tall are you? ")
#weight = raw_input("How much do you weigh? ")

#print "So, you're %r old, %r tall and %r heavy." % (
#   age, height, weight)
   
print "Lets have some fun. Here we go!" 
print ""    
name1 = raw_input("Name a boy: ")
name2 = raw_input("Name a girl: ")
noun = raw_input("Name a geographical feature: ")
liquid = raw_input("Name something you drink: ")
head = raw_input("Name something you wear: ")  
compliment = raw_input("An adjective used to describe someone smart: ")
insult = raw_input("An insulting name. ")
print "~~~" * 10
print "A Story about %s and %s" % (name1, name2)
print "----" * 4
print "%s and %s went up the %s to fetch a pail of %s." % (name1, name2, noun, liquid)
print "%s fell down and broke his %s," % (name1, head)
print "And %s was a %s and said," % (name2, compliment)
print "'You %s. You don't go up the %s to get %s!'" % (insult, noun, liquid)
