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
print(argv[0]) # it will print the name of the program which is executed from command prompt or terminal.
# if we want to access the values , we can pass the index of the list argv,
# but be careful while accessing the values because if we pass less values
#  #IndexError will occur, so we can use len() function to check the length of the list argv before accessing the values.