# print("Python Programming")
# print('x' * 10)
# name = input('Whats your name?')
# print('Hello ' + name)
# print('Lets get your age')
# Birth_year = input('Input your birth year?')
# age = 2025 - int(Birth_year)
# print(age)
# weight_lbs = input('What`s your weight in lbs?')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)
# print(name[0])

# #Python Calls
# name = 'Favour'
# print(name.find('our'))
# newName = name.replace('Favour','John')
#
# print(newName)

# #Check
# is_hot = False
#
# if is_hot:
#     print('It`s a hot day')
#     print('Get a cold drink')
#     print('Enjoy your day')
# else:
#     print('It`s a cold day')
#     print('Get a hot coffee')
#     print('Enjoy your day')

# #Weather check 2
# is_hot = False
# is_cold = True
#
# if is_hot:
#     print('Its hot today')
#     print('Dress casually')
# elif is_cold:
#     print('Its cold today')
#     print('Wear a warm cloth')
# else:
#     print('Its a cool day')
#
#     print('Enjoy your day')

# #Rent Eligibility check
# house_Price = 100000000
# ten_percent = 0.10 * house_Price
# twenty_percent = 0.20 * house_Price
# good_credit = True
#
# if good_credit:
#     print(f"Buyer is to pay: {ten_percent}")
# else:
#     print(f"Buyer is to pay: {twenty_percent}")

# #Eligibility check 2
# high_income = False
# good_credit = True
#
# if high_income and good_credit:
#     print("Buyer is eligible for loan")
# elif high_income and not good_credit:
#     print("Buyer is not eligible for loan")
# elif good_credit and not high_income:
#     print('Buyer still not eligible for loan')


# #Temperature checker
# Temperature = 30
#
# if Temperature > 30:
#     print('It is hot today')
# elif Temperature < 10:
#     print('It is cold today')
# else:
#     print('It is neither hot nor cold')


# #Length Checker
# name = "Jeremiah"
# if len(name) < 3:
#     print('Name is too short')
# elif len(name) > 10:
#     print('Name is too long')
# else:
#     print('Name is cool')


# #Weight Converter
# weight = input('Enter your Weight: ')
# value = int(weight)
# unit = input('(L)bs or (K)g: ')
#
# if unit.lower() == 'l':
#     result = value * 0.45
# elif unit.lower() == 'k':
#     result = value / 0.45
# else:
#     print('Type must be L or K')
#
# print(result)


# #looping
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1
# print('Done')


# #guessing program
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#      guess = int(input('Guess: '))
#      guess_count += 1
#      if guess == secret_number:
#          print('You won!')
#          break
#      else:
#          print('You lost!')

# #Mind game
# A = input('Lets play a little guess game, guess a number and respond ok: ')
# a = input('add 2 to the number and reply done: ')
# b = input('add 8 to the number and reply done: ')
# c = input('add 16 to the number and reply done: ')
# d = input('add 32 to the number and reply done: ')
# input('Subtract the number you thought of and reply done: ')
# result = 2+8+16+32
# print(f"The answer is: {result}")



# #Robot control
# command = ""
# while command.lower() != "quit":
#     command = input("> ")
#     if command.upper() == "START":
#         print("Robot Running")
#         break
#     elif command.upper() == "STOP":
#         print('Robot Stopped')
#         break
#     elif command.upper() == "HELP":
#         print("""
#         press start to start the robot
#         press stop to stop the robot
#         press quit to exit the program""")
#     elif command.upper() == "QUIT":
#         print('Program terminated')
#         break
#     else:
#         print('sorry, I don\'t understand that')

# #Robot control improved

#robot control container
# command = ""

# #robot state container
# started = False
#
# #Set it as always active to take command
# while True:
#     #command request
#     command = input("> ").lower()

#     #Roobot decision as per request response
#     if command == "start":
#         print('Robot Started')
#         #deal with user`s start command when robot has already started
#         if started == True:
#             print('Robot has already started')
#     elif command == "stop":
#         if started == False:
#             print('Robot has not started yet')
#         else:
#                  print('Robot Stopped')
#     elif command == "help":
#         print("""
# Type 'start' to start the robot
# Type 'stop' to stop the robot
# Type 'quit' to exit the program""")
#     elif command == "quit":
#         print('Program terminated')
#         break
#     else:
#         print('I don`t understand this')


# nested loop
# for x in range (3):
#     for y in range (3):
#         print(f'({x},{y})')


#nested loop to draw F shape
# for x in ("xx", "xx"):
#     for y in ("xxx", "", ""):
#         print(f'{x}{y}')

# F shape improved
# for i in [5,2,5,2,2]:
#     i = '*' * i
#     print(i)

# #check highest value in an array
# numbers = (1455, 1012, 3024, 10000, 0, 6, 100, 3024, 302)
# maxi = numbers[0]
# for number in numbers:
#     if number > maxi:
#         maxi = number
# print(f'Maximum number is {number}')


# #2 dimensions list
#
# matrix = [
#     [1, 2, 3],
#     [3, 4, 5],
#     [6, 7, 8]
# ]
#
# print(matrix[1][0])
# for row in matrix:
#     print(row)
#     for number in row:
#         print(number)\


# #removing duplicates in number arrays
# numbers = [1, 2, 10, 3, 4, 4, 3, 2, 5, 6, 7, 8, 9, 6, 6, 10]
# unique = []
# for number in numbers:
#     numbers.sort()
#     if number not in unique:
#         unique.append(number)
# print(unique)


# #removing duplicates in mixed array
# values = [1, 'g', 3, 'f', 2, 5, 5, 'b', 'd', 2, 9, 'a', 0, 'c', 10, 6, 'h', 4, 7, 8, 'e']
# uniques = []
# for value in values:
#     if value not in uniques:
#         uniques.append(value)
# print(uniques)


#Dictionary
customer_details = {
    'name' : 'john doe',
    'date_of_birth' : '2000-1-1',
    'email' : 'Johndoe@gmail.com',
    'password' : '12048HHsn*@',
    'department' : 'software engineering',
    'is_verified' : True
}

print(customer_details["name"])
print(customer_details.get("password"))
print(customer_details.get("Email", "samuelsetemijp@gmail.com"))