# by default python treat all the command line argument as string, so if we want to use them as integer or float then we have to typecast them into int or float.

from sys import argv 
print("First num is",argv[1])
print("second num is",argv[2])
print("Their sum is",argv[1]+argv[2])


from sys import argv
a=eval(argv[1])
b=eval(argv[2])
print("First num is",a)
print("Second num is",b)
print("Their sum is",a+b) #

import sys

# Print all command-line arguments
print("Number of arguments:", len(sys.argv))
print("Arguments list:", sys.argv)




from sys import argv 
print("Hello",argv[1]) #Eecution: python cmd_arg2.py sameer kumar
# OUTPUT:For Python Sameer and kumar are 2 separatearguments , so argv[1] receives Sameer and argv[2] receives kumar

#Execution: python cmdarg.py “Sachin Kapoor” ## OUTPUT: Hello sachin kapoor


# Execution: python cmdarg.py 'sameer kumar' ## OUTPUT: hello sameer kumar