def function_name():
##Any parameters that the function needs are named in the parentheses:

def function_name(parameter_name):


###

def hello_name(user_name):
    print("Hello {0}".fomrat(user_name))

#main program
my_name = input("Please enter your name: ")
hello_name(my_name)


###

def multiply(x, y):
    answer = x * y
    return answer

#main program
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
product = multiply(x, y)
print("The product of {0} and {1} is {2}".format(x, y, product))
