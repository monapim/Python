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
