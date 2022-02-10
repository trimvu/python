#Name: Tri Vu HW #1

# SMALL

# 1. Hello You!

# name = input('What is your name? ')

# print("Hello, " + name + "!")


# 2. HELLO YOU!

# name = input('WHAT IS YOUR NAME? ')

# name.upper()

# print("HELLO, " + name.upper() + "!" )
# print("YOUR NAME HAS " + str(len(name)) + " LETTERS IN IT! AWESOME!")


# 3. Madlib

# print('Please fill in the blanks below')

# name = input('What is name? ')

# subject = input('What is subject? ')

# madlib = "{}'s favorite subject in school is {}".format(name, subject)

# print(madlib)


# 4. Day of the Week

# print('Please enter a number from 0 - 6: ')

# day = int(input('Day (0-6)? '))

# if day == 0:
#     result = "Sunday"
# elif day == 1:
#     result = "Monday"
# elif day == 2:
#     result = "Tuesday"
# elif day == 3:
#     result = "Wednesday"
# elif day == 4:
#     result = "Thursday"
# elif day == 5:
#     result = "Friday"
# elif day == 6:
#     result = "Saturday"
# else:
#     result = "This number is not an option. Please select a number from 0 - 6: "
    
# print(result)


# 5. Work or Sleep In?

# print('Please enter a number from 0 - 6: ')

# day = int(input('Day (0-6)? '))

# if day == 0 or day == 6:
#     result = "It's the weekend! Sleep in, baby!"
# elif day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
#     result = "It's the weekday! Go to work!"
# else:
#     result = "This number is not an option. Please select a number from 0 - 6: "
    
# print(result)


# 6. Celsius to Fahrenheit

# C = int(input('Please enter the temperature (a number) in Celsius to convert the value to degrees in Fahrenheit: '))

# F = (C * 9/5) + 32

# print(F, "degrees F")


# 7. Looping from 1 to 10

# count = 0

# while count != 10:
#     count+=1
#     print(count)


# 8. n to m

# print('Please enter a start number and an end number')

# start = int(input('Start from: '))
# end = int(input('End on: '))

# while start <= end:
#     print(start)
#     start+=1


# 9. Print a Square

# count = 0

# while count < 5:
#     print("*****")
#     count+=1


# 10. Print a Square II

# count = 0

# nbyn = int(input('Please enter a number to generate a squared box: '))

# while count < nbyn:
#     print(nbyn * "*")
#     count+=1
    

# MEDIUM

# 1. Tip Calculator

# bill = float(input('Total bill amount? $'))
# print("$%.2f" % bill)

# service = input("""
#                 Level of service? 
                
#                 Good
#                 Fair
#                 Bad
                
#                 """)

# # total = bill + (bill * service)

# if service.lower() == 'good':
#     tip = (bill * 0.2)
#     total = bill + tip
#     print("Tip amount: $%.2f" % tip)
#     print("Total amount: $%.2f" % total)
# elif service.lower() == 'fair':
#     tip = (bill * 0.15)
#     total = bill + tip
#     print("Tip amount: $%.2f" % tip)
#     print("Total amount: $%.2f" % total)
# elif service.lower() == 'bad':
#     tip = (bill * 0.1)
#     total = bill + tip
#     print("Tip amount: $%.2f" % tip)
#     print("Total amount: $%.2f" % total)
# else:
#     print('Please enter a valid service level ')
    

# 2. Tip Calculator 2

# bill = float(input('Total bill amount? $'))
# print("$%.2f" % bill)

# service = input("""
#                 Level of service? 
                
#                 Good
#                 Fair
#                 Bad
                
#                 """)

# split = int(input('Split how many ways? '))

# if service.lower() == 'good':
#     tip = (bill * 0.2)
#     total = bill + tip
#     per_person = total / split
#     print("Tip amount: $%.2f" % tip)
#     print("Total amount: $%.2f" % total)
#     print("Amount per person: $%.2f" % per_person)
# elif service.lower() == 'fair':
#     tip = (bill * 0.15)
#     total = bill + tip
#     per_person = total / split
#     print("Tip amount: $%.2f" % tip)
#     print("Total amount: $%.2f" % total)
#     print("Amount per person: $%.2f" % per_person)
# elif service.lower() == 'bad':
#     tip = (bill * 0.1)
#     total = bill + tip
#     per_person = total / split
#     print("Tip amount: $%.2f" % tip)
#     print("Total amount: $%.2f" % total)
#     print("Amount per person: $%.2f" % per_person)
# else:
#     print('Please enter a valid service level ')


# 3. How many coins?

# coin = 0
# answer = ''

# while answer != 'no':
#     print("You have {} coins".format(coin))
#     answer = input('Do you want another? ').lower()
#     if answer == 'yes':
#         coin+=1

# print('Bye')


# 4. Print a Box

# count = 0

# width = int(input('Width? '))
# height = int(input('Height? '))

# print(width * "*")

# while count < height - 2:
#     print("*" + ((width - 2) * " ") + "*")
#     count +=1
    
# print(width * "*")


# 5. Print a Tringle

# count = 1
# down = 3

# while count < 9:
#     print((down * " ") + (count * '*'))
#     down-=1
#     count+=2


# 6. Multiplication Table

# first = 1
# second = 1

# while first < 11:
#     while second < 11:
#         answer = first * second
#         print(first, "X", second, "=", answer)
#         second+=1
#     second = 1
#     first+=1