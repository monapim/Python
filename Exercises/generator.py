# fill in this function
def fib():
	# pass <- this is a null statement which does nothing when executed, useful as a placeholder.
	
	# initialize the last two numbers
	a = 0
	b = 1	
	
	for i in xrange(100):
		sum = a + b
		yield sum
		a, b = b, sum
	
	
# testing code
import types
if type(fib()) == types.GeneratorType:
    print "Good, The fib function is a generator."

    counter = 0
    for n in fib():
        print n
        counter += 1
        if counter == 10:
            break