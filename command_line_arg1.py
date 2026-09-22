#  command line argument are the values, we can pass while executing our python code from command prompt or terminal.
# SYNTAX: python program_name.py <values>(can be list, number,string anything) but be careful while passing values, because it will be treated as string by default.

# example python demo.py 10 20 30


#NOTE: -
# 1} command line argument (that are actually itself a list) are stored by python in a special predefined variable called argv.

# 2} Following are important features of argv:
# a) The variable argv is a list which itself stored in a module called sys.
# b) So to use it, we must import sys module in our program.

from sys import argv
print(argv)
print(type(argv))
print(len(argv))
print(argv[1]) # it will print the first command line argument.

# if we want to access the values , we can pass the index of the list argv,
# but be careful while accessing the values because if we pass less values
#  #IndexError will occur, so we can use len() function to check the length of the list argv before accessing the values.


n=len(argv)
print("you have passed",n-1,"arguments")
print("the values are: ",argv[1:n])

"""NOTE:- by default python treats all the command line arguments as string values."""

print("First num is :",argv[2])
print("Second num is :",argv[3])
print("Their sum is :",argv[2]+argv[3])

#so, if you want to use them as integer or float values, then you have to typecast them into int or float using int() or float() function.

print("First num is :",int(argv[2]))
print("Second num is :",int(argv[3]))
print("Their sum is :",int(argv[2])+int(argv[3]))