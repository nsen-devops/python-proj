# age = int(input("Please type your age: "))
# day="ss"

# movie_ticket = 12 if age >= 18 else 8

# if day=="wednesday":
#     movie_ticket -= 2

# print(movie_ticket)
###################################################################
# color = "Yellow"
# # color = input("Please type the color of banana: ")

# if color == "Green":
#     print("Banana is unripe")
# elif color == "Yellow":
#     print("Banana is ripe")
# elif color == "Brown":
#     print("Banana is overripe")
# else:
#     print(None)

###################################################################
# age = int(input("Please enter your age: "))

# if 0 < age <= 3:
#     print("you are a toddler :)")
# elif 3 < age < 13:
#     print("you are a child")
# elif 13 <= age < 20:
#     print("you are a teenage")
# elif 20 <= age < 120:
#     print("you are a adult")
# else:
#     print("please enter the correct age number")

###################################################################

# name = "Nitin Singh Sen"

# print(len(name))

###################################################################

year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")