# numbers_list = [2,3,4,-1,33,4,-9,-3]

# postive_numbers_list = 0
# for num in numbers_list:
#     if num > 0:
#         postive_numbers_list += 1

# print("Total positive numbers are: ",postive_numbers_list)

#############################################################

# num = int(input("Please enter a number: "))

# even_num = 0

# for i in range(1, num+1):
#     if i%2 == 0:
#         even_num += 1

# print("Total even numbers are :", even_num)

#############################################################

# n = int(input("please enter the number to write a table: "))

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(n, "x", i, "=", n*i)

#############################################################
# my_name="nitin singh sen"

# print(my_name[-1::])

#############################################################

# number = 5
# factorial_number = 1
# while number > 0:
#     factorial_number *= number
#     number -= 1
    
# print("factorial is", factorial_number)
#############################################################

# while True:
#     input_str = int(input("enter a number b/w 1 to 10: "))
#     if 1 <= input_str <= 10:
#         print("thanks")
#         break
#     else:
#         print("enter a valid number")

#############################################################

fruits = ["apple", "banana", "orange", "apple", "pineapple", "banana"]

fruit_set = set()
fruit_duplicate = []

for i in fruits:
    if i in fruit_set:
        fruit_duplicate.append(i)
        
    fruit_set.add(i)
print(fruit_set)
print("fruit", fruit_duplicate, "is duplicate in the bucket")
    
#############################################################

