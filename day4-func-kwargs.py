# def addition(x,y):
#     sum = x + y
#     return sum

# print(addition(4,5))

#############################

# def multiplication(numOne, numTwo):
#     return numOne * numTwo

# print(multiplication("nitin", 4))

##########################################################

# import math
# user_input = int(input("please enter the radius of a circle: "))

# def circle_stats(radius):
#     area = math.pi * (radius ** 2)
#     circumference = 2 * math.pi * radius
#     return area, circumference

# a, c = circle_stats(user_input)

# print("'area of circle is:'", a, "'circumference of circle is:'", c)

##########################################################

## CLOUSURES

# def func1(x):
#     def func2(y):
#         return x ** y
#     return func2

# function1 = func1(3)

# print(function1(5))

##########################################################

def greet(fandooprog):
    def wrapper(*arguments, **keywords):
        print("hello sir, namaste. Below is the users list:\n")
        fandooprog(*arguments, **keywords)
        print("\nbye!!")
    return wrapper

@greet
def rand(*args, **kwargs):

    for i in args:
        print(i)
    for k, v in kwargs.items():
        print(f"{k} is a {v}")

user_list = ["nitin", "ritesh", "kriti", "ram"]
desg = {"nitin":"Soldier", "ritesh":"civil engineer", "kriti":"developer"}

rand(*user_list, **desg)
