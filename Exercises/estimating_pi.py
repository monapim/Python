# need to import random
# need to call random.random() to make the random thing to work


def sample(p):
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0

# use the pre-defined variable 'sc' instead of 'spark' 
count = spark.parallelize(xrange(0, NUM_SAMPLES)).map(sample) \
             .reduce(lambda a, b: a + b)
print "Pi is roughly %f" % (4.0 * count / NUM_SAMPLES)