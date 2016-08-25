from sys import argv  

script, input_file = argv #I'm calling blah.txt for this example
							# $ python ex20.py blah.txt
							
def print_all(f):
    print f.read()  # reading the WHOLE file here. see ex20, student Question #1
        
def rewind(f): 
    f.seek(0)   # seeking line 0. ie. go to the beginning of the file
       
def print_a_line(line_count, f):	# defining a function called print_a_line that acts with the vars 'line_count' and the file
    print line_count, f.readline()  # I have no idea. it's magic. Is this a built-in??
    
current_file = open(input_file)  # hmm... his example shows open as a command acting on input_file
    
print "First let's print the whole file:\n"

print_all(current_file)	# print all the lines in the file

print "Now let's rewind, kind of like with a tape."

rewind(current_file)	# call the script rewind which 'seeks line zero' on the file we supplied /blah.txt/

print "Let's print three lines:"

current_line = 1							
	# we're saying the current line is line 1
	# it changes the line number BUT NOT the text it reads.
																					
print_a_line(current_line, current_file)	# calling the function print_a_line AND passing line # on the file we use


current_line = current_line + 1					# adding one to the current line
print_a_line(current_line, current_file)

current_line = current_line + 1					# adding one to the NEW current line
print_a_line(current_line, current_file)

#=======

en
conf t
hostname CHANGEME



