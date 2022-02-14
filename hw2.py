#? Tri Vu HW #2

#! Small

#? 1. Sum the Numbers

# while loop
# nums = [2, 3, 5, 7, 11, 13, 17]

# index = 0

# sum = 0 

# while index < len(nums):
#     sum += nums[index] 
#     index+=1

# print(sum) 


#? for loop
# nums = [2, 3, 5, 7, 11, 13, 17]

# sum = 0

# for x in nums:
#     sum += x
    
# print(sum)


#? Alternative method

# sum = sum(nums)

# print(sum)


#? 2. Largest Number

# nums = [2, 17, 3, 13, 5, 11, 7]

# nums.sort()

# print(nums[-1])


#? for loop
# nums = [2, 3, 5, 7, 11, 13, 17]

# max = nums[0]

# for x in nums:
#     if(max < x):
#         max = x

# print(max)

#? 3. Small Number

# nums = [2, 17, 3, 13, 5, 11, 7]

# nums.sort()

# print(nums[0])


#? for loop
# nums = [13, 2, 17, 3, 13, 5, 11, 7]

# min = nums[0]

# for x in nums:
#      if (min > x):
#          min = x

# print(min)


#? 4. Even Numbers

#? while loop
# nums = [2, 3, 4, 5, 6, 7, 8, 9]

# index = 0

# while index < len(nums):
#     if nums[index] % 2 == 0:
#         print(nums[index])
#     index+=1


#? for loop
# nums = [2, 3, 4, 5, 6, 7, 8, 9]

# for x in nums:
#     if x % 2 == 0:
#         print(x)

#? 5. Positive Numbers

#? whlie loop
# nums = [-1, 1, -2, 2, -3, 3, -4, 4]

# index = 0

# while index < len(nums):
#     if nums[index] > 0:
#         print(nums[index])
#     index+=1

#? for loop
# nums = [-1, 1, -2, 2, -3, 3, -4, 4]

# for x in nums:
#     if x > 0:
#         print(x)

#? 6. Positive Numbers II

#? while loop
# nums = [-1, 1, -2, 2, -3, 3, -4, 4]

# pos_nums = []

# index = 0

# while index < len(nums):
#     if nums[index] > 0:
#         pos_nums.append(nums[index])
#     index+=1

# print(pos_nums)


#? for loop
# nums = [-1, 1, -2, 2, -3, 3, -4, 4]

# pos_nums = []

# for x in nums:
#     if x > 0:
#         pos_nums.append(x)
        
# print(pos_nums)

#? 7. Multiply a list

#? while loop
# nums = [2, 3, 5, 7, 11, 13, 17]

# mult_nums = []

# factor = 3

# index = 0

# while index < len(nums):
#     mult_nums.append(nums[index] * factor)
#     index+=1

# print(nums)
# print(mult_nums)


#? for loop
# nums = [2, 3, 5, 7, 11, 13, 17]

# mult_nums = []

# factor = 3

# for x in nums:
#     mult_nums.append(x * 3)

# print(nums)
# print(mult_nums)

#? 8. Reverse a String

# word = "water"

# reverse = word[len(word)::-1]

# print(reverse)


#? for loop 
# myCity = "Atlanta"
# reverse = ""

# for char in myCity:
#     reverse = char + reverse

# print(reverse)


#! Medium

#? 1. Multiply Vectors

#? while loop
# vec1 = [2, 4, 5]
# vec2 = [2, 3, 6]

# vec3 = []

# index = 0

# while index < len(vec1):
#     vec3.append(vec1[index] * vec2[index])
#     index+=1

# print(vec3)


#? for loop
# vec1 = [2, 4, 5]
# vec2 = [2, 3, 6]

# vec3 = []

# # c_(i) = a_(i) * b_(i)

# for i in range(len(vec1)):
#     vec3.append(vec1[i] * vec2[i])
    
# print(vec3)

#? 2. Matrix Addition

# a = [[1, 3], 
#      [2, 4]]
# b = [[5, 2], 
#      [1, 0]]

# c = [[0, 0], 
#      [0, 0]]

# i = 0
# j = 0

# while i < len(a):
#     while j < len(a):
#         c[i][j] = a[i][j] + b[i][j]
#         j+=1
#     j = 0
#     i+=1
    
# print(c)


#? for loop
# a = [[1, 3], 
#      [2, 4]]
# b = [[5, 2], 
#      [1, 0]]

# c = []

# for i in range(len(a)):
#     v = []
#     for j in range(len(a)):
#         v.append(a[i][j] + b[i][j])
#     c.append(v)
        
# print(c)


#? 3. Matrix Addition II

# a = [[1, 3, 6], 
#      [2, 4, 7],
#      [5, 9, 8]]
# b = [[5, 3, 0], 
#      [4, 2, -1],
#      [1, -3, -2]]

# c = [[0, 0, 0], 
#      [0, 0, 0],
#      [0, 0, 0]]

# i = 0
# j = 0

# while i < len(a):
#     while j < len(a):
#         c[i][j] = a[i][j] + b[i][j]
#         j+=1
#     j = 0
#     i+=1
    
# print(c)


#? for loop

# a = [[1, 3, 6], 
#      [2, 4, 7],
#      [5, 9, 8]]
# b = [[5, 3, 0], 
#      [4, 2, -1],
#      [1, -3, -2]]

# c = []

# for i in range(len(a)):
#     v = []
#     for j in range(len(a)):
#         v.append(a[i][j] + b[i][j])
#     c.append(v)

# print(c)


#? 4. De-dup

# nums = [2, 2, 3, 3, 5, 5, 7, 7]

# de_dup = []

# for x in nums:
#     if x not in de_dup:
#         de_dup.append(x)

# print(de_dup)


#? 5. Leetspeak

# leet = str(input('Enter a word or phrase to translate to "L337" speak: ')).lower()

# print(leet)

# alphabet = list(leet)

# print(alphabet)

# index = 0

# # a = 4, e = 3, g = 6, i = 1, o = 0, s = 5, t = 7

# while index < len(alphabet):
#     if alphabet[index] == 'a':
#         alphabet[index] = '4'
#     elif alphabet[index] == 'e':
#         alphabet[index] = '3'
#     elif alphabet[index] == 'g':
#         alphabet[index] = '6'
#     elif alphabet[index] == 'i':
#         alphabet[index] = '1'
#     elif alphabet[index] == 'o':
#         alphabet[index] = '0'
#     elif alphabet[index] == 's':
#         alphabet[index] = '5'
#     elif alphabet[index] == 't':
#         alphabet[index] = '7'
#     index+=1
        
# print(alphabet)

# to_leet = "".join(alphabet)

# print(to_leet)


#? for loop
# leetbet = []


#? 6. Long-long Vowels

#? If there is only ONE word with a double vowel 
# long_long = str(input("Enter a word or phrase: "))

# print(long_long)

# index = 0

# while index < len(long_long):
#     if long_long[index:index+2] == 'aa':
#         new_long = long_long[:index] + 'aaa' + long_long[index:]
#     elif long_long[index:index+2] == 'ee':
#         new_long = long_long[:index] + 'eee' + long_long[index:]
#     elif long_long[index:index+2] == 'ii':
#         new_long = long_long[:index] + 'iii' + long_long[index:]
#     elif long_long[index:index+2] == 'oo':
#         new_long = long_long[:index] + 'ooo' + long_long[index:]
#     elif long_long[index:index+2] == 'uu':
#         new_long = long_long[:index] + 'uuu' + long_long[index:]
#     elif long_long[index:index+2] == 'yy':
#         new_long = long_long[:index] + 'yyy' + long_long[index:]
#     index+=1

# print(new_long)
    

#? If there are MORE THAN TWO words with a double vowel

# long_long = str(input("Enter a word or phrase: ")).lower()

# print(long_long)

# list_long = list(long_long)

# print(list_long)

# index = 0

# while index < len(list_long):
#     if list_long[index:index+2] == ['a', 'a']:
#         list_long.insert(index+1, 'aaa')
#         index+=1
#     elif list_long[index:index+2] == ['e', 'e']:
#         list_long.insert(index+1, 'eee')
#         index+=1
#     elif list_long[index:index+2] == ['i', 'i']:
#         list_long.insert(index+1, 'iii')
#         index+=1
#     elif list_long[index:index+2] == ['o', 'o']:
#         list_long.insert(index+1, 'ooo')
#         index+=1
#     elif list_long[index:index+2] == ['u', 'u']:
#         list_long.insert(index+1, 'uuu')
#         index+=1
#     elif list_long[index:index+2] == ['y', 'y']:
#         list_long.insert(index+1, 'yyy')
#         index+=1
#     index+=1

# print(list_long)

# to_long = "".join(list_long)

# print(to_long)

#? 7. Caesar Cypher

# choice = ''

# while choice not in ['1', '2']:
#     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
#     print("Please enter the number option to either encrypt or decrypt a message from ROT13: ")

#     choice = str(input("""
                    
#     1. Encrypt
#     2. Decrypt
#     3. Enter any other key to end
                    
#                     """))
        
#     encrypt = []
#     decrypt = []
    
#     if choice not in ['1', '2']:
#         break
#     entered = str(input("Please enter the message: "))
#     list_entered = list(entered)

#     if choice == '1':
        
#         for i in range(len(list_entered)):
#             for j in range(len(alphabet)):
#                 if list_entered[i] == alphabet[j]:
#                     encrypt.append(alphabet[(j + 13) % 26])
#                 elif list_entered[i] == ' ':
#                     encrypt.append(' ')
#                     break
#         join_encrypt = "".join(encrypt)
#         print(join_encrypt)

#     elif choice == '2':
        
#         for i in range(len(list_entered)):
#             for j in range(len(alphabet)):
#                 if list_entered[i] == alphabet[j]:
#                     decrypt.append(alphabet[(j - 13) % 26])
#                 elif list_entered[i] == ' ':
#                     decrypt.append(' ')
#                     break
#         join_decrypt = "".join(decrypt)
#         print (join_decrypt)

#     else:
#         break