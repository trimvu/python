#? Tri Vu HW #2

#! Small

#? 1. Sum the Numbers

# nums = [2, 3, 5, 7, 11, 13, 17]

# index = 0

# sum = 0 

# while index < len(nums):
#     sum += nums[index] 
#     index+=1

# print(sum) 

# Alternative method

# sum = sum(nums)

# print(sum)


#? 2. Largest Number

# nums = [2, 17, 3, 13, 5, 11, 7]

# nums.sort()

# print(nums[-1])


#? 3. Small Number

# nums = [2, 17, 3, 13, 5, 11, 7]

# nums.sort()

# print(nums[0])


#? 4. Even Numbers

# nums = [2, 3, 4, 5, 6, 7, 8, 9]

# index = 0

# while index < len(nums):
#     if nums[index] % 2 == 0:
#         print(nums[index])
#     index+=1

#? 5. Positive Numbers

# nums = [-1, 1, -2, 2, -3, 3, -4, 4]

# index = 0

# while index < len(nums):
#     if nums[index] > 0:
#         print(nums[index])
#     index+=1

#? 6. Positive Numbers II

# nums = [-1, 1, -2, 2, -3, 3, -4, 4]

# pos_nums = []

# index = 0

# while index < len(nums):
#     if nums[index] > 0:
#         pos_nums.append(nums[index])
#     index+=1

# print(pos_nums)


#? 7. Multiply a list

# nums = [2, 3, 5, 7, 11, 13, 17]

# mult_nums = []

# factor = 3

# index = 0

# while index < len(nums):
#     mult_nums.append(nums[index] * factor)
#     index+=1

# print(nums)
# print(mult_nums)


#? 8. Reverse a String

word = "water"

reverse = word[len(word)::-1]

print(reverse)


#! Medium

#? Multiply Vectors

# vec1 = [2, 4, 5]
# vec2 = [2, 3, 6]

# vec3 = []

# index = 0

# while index < len(vec1):
#     vec3.append(vec1[index] * vec2[index])
#     index+=1

# print(vec3)


#? Matrix Addition

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


#? Matrix Addition II

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



