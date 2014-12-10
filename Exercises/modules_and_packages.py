# Modules in Python are simply Python files with the .py extension, 
# which implement a set of functions. 
# Modules are imported from other modules using the import command.

# import the module re 
import re

#  print an alphabetically sorted list of all functions in the re module,
# print(sorted(dir(re)))
sorted_re = sorted(dir(re))
for x in sorted_re:
	print(x)