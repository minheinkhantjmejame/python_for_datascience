full_name = 'John Smith'
age = 20
is_new = True

# name = input('What is your name? ')
# print('Hi '+name)

# name = input('What\'s your name? ')
# color = input('What\'s your fav color ')
# print(name,'likes',color)

# weight = input('Tell me your weight in pounds ')
# weight_in_kg = int(weight) * 0.4535
# print('your weight is '+ str(weight_in_kg))


# first_name = "Min Hein"
# last_name = "Khant"
# text  = f"{first_name} {last_name} " + "is " + "[fuckin] " + "billionaire"
# print(text)

# course = "Python for Beginners"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.find('o'))
# print(course.replace('for','of'))
# print('of' in course)

#BODMAS RULES
# cal = (2 // 3) * (2+4*5) % 5
# print(cal)

# if statement
# total_price_of_house = 1000000
# # good_credit = True
# good_credit = False 
# down_payment_price = 0
# if good_credit:
#     down_payment_price += total_price_of_house * 0.1
# else:
#     down_payment_price += total_price_of_house * 0.2
# print(f'your down payment price is {down_payment_price}')

# ***************************************************

# logical operators 

# and / or 
# has_high_income = False
# has_good_credit = True

# if has_high_income or has_good_credit:
#     print("Eligible for loan")

# not

# has_good_credit = True 
# has_criminal_record = False

# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")

# *******************************************************

#comparison_operators 

# type_name = input("Type your name please!")

# if len(type_name) < 3:
#     print("Name must be at least 3 characters")
# elif len(type_name) > 50:
#     print("name can be maximum of 50 characters")
# else:
#     print(f"Nice! {type_name}. Your name looks good")

# project(1)
# weight = float(input('weight'))
# lbs_or_kilos = input('(L)bs or (K)g :')

# if lbs_or_kilos == 'l' or 'L':
#     print('your weight in pounds is ',(weight*2.2))
# elif lbs_or_kilos == 'k' or 'K':
#     print('your weight in kilograms ', (weight*0.45))
# else:
#     print('Please type that you want to change l in pounds or k in kilos')


# ******************************************************

# while loop 

#projectone 
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print('you won!')
#         break 
# else:
#     print('sorry, you lose!')

# project two (car game) 

# mycode
# start_the_program = True
# out_the_program = 'quit'
# started = False

# while start_the_program:
#     user_input = input('>').lower()
#     if user_input == 'help': 
#         print('To start the engine, type "start"')
#         print('To stop the engine, type "stop"')
#         print('To quit the program, type "quit"')
#     elif user_input == 'start':
#         if started:
#             print("the card is already started")
#         else:
#             started = True
#             print('Car started...Ready to go')
#     elif user_input == 'stop':
#         if not started:
#             print('the car is already stopped')
#         else:
#             started = False
#             print('Car Stopped')
#     elif user_input == out_the_program:
#         start_the_program = False
        
#     else:
#         print("I don't understand that...")



#*******************************************************

# For loop 

# prices = [10,20,30]
# total = 0
# for price in prices:
#     total += price 

# print(total)


#*******************************************************

# Nested loop 
# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

# exercise (1) 

# method (1)
# numbers = [5,2,5,2,2]
# for number in numbers:
#     print(number*"x")

# method(2) 
# numbers = [5,2,5,2,2]
# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#         output = output + 'x'
#     print(output)
# print(1+'x')

#*******************************************************
# Lists 

# exercise one : find the largest number 
# method (1) 
# numbers = [2,45,54,443,34343,334303,30303,300]
# print(max(numbers))
# print(min(numbers))

# method(2) 
# numbers = [2,45,54,443,34343,334303,30303,300]
# max = numbers[0]
# for number in numbers: 
#     if number > max:
#         max = number 
#         # number = max 
# print(max)


#*******************************************************
# 2D lists 

# matrix  = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)

#*******************************************************
# list methods  
# numbers = [5,2,1,7,4]
# numbers.append(20)
# numbers.insert(2,200)
# numbers.remove(5)
# numbers.clear()
# numbers.pop()
# print(numbers.index(5))
# print(50 in numbers)
# print(numbers.count(3))
# numbers.sort()
# numbers.reverse()
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers)
# print(numbers2)


# exercise one 
# wirte a program to remove the duplicates in a list 
# numbers = [2,5,5,5,65,43,2,4,77,3,2]
# # numbers.sort()
# # print(numbers)
# # print(numbers.count(2))
# print(numbers)
# for number in numbers:
#     if numbers.count(number) > 1:
#         numbers.remove(number)
# # print(numbers)
# # numbers.sort()
# print(numbers)
# my solution is wrong. Because loop is skipped the index that it is already counted

#mosh's solution
# numbers = [2,2,4,6,3,4,6,1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         print(uniques)
#         uniques.append(number)


#*******************************************************
# tuple 
# coordinates = (1,2,3) #tuples
# # coordinates = [1,2,3] list
# x,y,z = coordinates 
# print(y)

#*******************************************************

#dictionary 
# customer = {
#     "name":"John Smith",
#     "age":30,
#     "is_verified":True
# }

# customer['name'] = 'Jack Smith'
# print(customer['name'])
# #print(customer.get('name'))
# print(customer.get('birthdate','2004-03-23'))
# print(customer) 

# exercise 
ph_number = input('Phone: ')
num_name = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
output = ""
for ch in ph_number:
    output += num_name.get(int(ch))
print(output)

#*******************************************************