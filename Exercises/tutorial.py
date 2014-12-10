# classes and objects
print('\n### classes and objects')

# define class MyClass
class MyClass:
    variable = "blah"

    def function(self):
        print "This is a message inside the class."
		
myobjectx = MyClass()
myobjectx.variable

myobjecty = MyClass()
myobjecty.variable = "yackity"

print myobjectx.variable   # This would print "blah".
print myobjecty.variable   # This would print "yackity".



# dictionaries
print('\n### dictionaries')
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

print(phonebook)

phonebook2 = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

print(phonebook2)

# iterating over dictionaries
for name, number in phonebook.iteritems():
	print('Phone number of %s is %d' %(name, number))

# use del or .pop() to remove a specific index
print('# remove john in dictionary phonebook')
del phonebook['John']
for name, number in phonebook.iteritems():
	print('Phone number of %s is %d' %(name, number))
	
	
	
# modules and packages
print('\n### modules and packages')
import urllib
dir(urllib)



# generators
print('\n### generators')

a = 1
b = 2
a, b = b, a # can switch values simultaneously
print('a = %d' % a)
print('b = %d' % b)



# list comprehensions
print('\n### list comprehensions')

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(word_lengths)


# multiple function arguments 
print('\n### multiple function arguments ')

def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print "The sum is: %d" % (first + second + third)

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print "Result: %d" % result



# exception handling
print('\n### exception handling')
def do_stuff_with_number(n):
    print n

the_list = (1, 2, 3, 4, 5)

for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
    except IndexError: # Raised when accessing a non-existing index of a list
        do_stuff_with_number(0)



# sets
print('\n### sets')

print set("my name is Eric and Eric is my name".split())

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

a.intersection(b)
b.intersection(a)



# Serialization with JSON

import json

# To encode a data structure to JSON, use the "dumps" method. This method takes an object and returns a String:
json_string = json.dumps([1, 2, 3, "a", "b", "c"])

# To load JSON back to a data structure, use the "loads" method. This method takes a string and turns it back into the json object datastructure:
print json.loads(json_string)

# Python supports a Python proprietary data serialization method called pickle (and a faster alternative called cPickle).
# You can use it exactly the same way.
import cPickle
pickled_string = cPickle.dumps([1, 2, 3, "a", "b", "c"])
print cPickle.loads(pickled_string)
