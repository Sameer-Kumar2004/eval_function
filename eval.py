# SYNTAX eval(expression)

# The argument passed to eval() must follow below mentioned rules:
#  --> It must be given in the form of string.
# --> It should be valid python code or expression.

x=eval('2+3')
print(x)


x=eval('2+3*6')
print(x)



eval('print(15)')



## using eval for time conversion
x=eval('2.5')
print(x)
print(type(x))

# same example without eval
x='2.5'
print(x)
print(type(x))




## using eval for type conversion 

# ---> we can use eval() with input() function to perform automatic type conversion of values.
# --> In this way, we will not have to use type conversion functions like int(), float() or bool()


age=eval(input("Enter your age: "))
age=age+10
print("After 10 years, you will be", age,"years old")



a=eval(input("Enter a number: "))
print(a)
print(type(a)) 
# suppose user types 5 , then output <'class int'> 
# Suppose user types 3.6, then output <'class float'>
# Suppose user types [10,20,30], then output <'class list'>
# Suppose user types True, then output <'class bool'>


"""suppose user type Hello, #OUTPUT: NameError: name 'Hello is not defined."""
## To avoid this error type string in double quote("string") or in single quotes ('string').

b=eval(input("Enter something: "))
print(b)
print(type(b)) # Suppose user types “Hello", then #oOUTPUT: <'class str'>.
