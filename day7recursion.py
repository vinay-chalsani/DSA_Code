


# def multi_ops(arr, i):
#     # Base case
#     if i == len(arr):
#         return 0, 0  # (sum, count)

#     # 🔹 Operation 1: print element
#     print("Processing:", arr[i])

#     # Recursive call
#     sub_sum, sub_count = multi_ops(arr, i + 1)

#     # 🔹 Operation 2: sum calculation
#     total_sum = arr[i] + sub_sum

#     # 🔹 Operation 3: count elements
#     total_count = 1 + sub_count

#     return total_sum, total_count


# arr = [10, 20, 30, 40]

# s, c = multi_ops(arr, 0)

# print("Sum:", s)
# print("Count:", c)
#..............................................................................#

#_____________________________RecursiveRange Solution___________________________#
# def recursiveRrange(num):# define a function that takes a number as input
#     if num <= 0:# check if the number is less than or equal to 0
#         return 0# if the number is less than or equal to 0, return 0 as the base case for the recursion
#     return num + recursiveRrange(num - 1)# return the current number added to the result of recursively calling the function with the number decremented by 1

# print(recursiveRrange(6))# Output: 21 (6 + 5 + 4 + 3 + 2 + 1)
# #...............................................................................#

#____________________________Palindrome String Solution_________________________#
# def palindrome(string):                 # define a function that takes a string as input
#     if len(string) <= 1:                # check if the input string has a length of 1 or less
#         return True                     # if the string has a length of 1 or less, return True (base case for recursion)
#     if string[0] != string[-1]:         # check if the first and last characters of the string are not the same
#         return False                    # if the first and last characters are not the same, return False (the string is not a palindrome)
#     return palindrome(string[1:-1])     # return the result of recursively calling the function with the substring that excludes the first and last characters

# print(palindrome("racecar"))            # Output: True (the string is a palindrome)
# print(palindrome("hello"))              # Output: False (the string is not a palindrome)
# print(palindrome("a"))                  # Output: True (a single character is a palindrome)
# print(palindrome("")                   # Output: True (an empty string is a palindrome)
# print(palindrome("madam"))            # Output: True (the string is a palindrome)             
#...............................................................................#

# #______________________________SomeRecursive Solution___________________________#
# def someRecursive(arr, target):# define a function that takes an array and a target value as input
#     if len(arr) == 0:# check if the input array is empty
#         return False# if the array is empty, return False (base case for recursion)
#     if arr[0] == target:# check if the first element of the array is equal to the target value
#         return True# if the first element is equal to the target value, return True (the target value is found in the array)
#     return someRecursive(arr[1:], target)# return the result of recursively calling the function with the rest of the array (excluding the first element) and the same target value

# def isOdd(num):# define a function that takes a number as input
#     if num % 2 == 0:# check if the number is even
#         return False# if the number is even, return False (the number is not odd)
#     return True# if the number is odd, return True (the number is odd)

# print(someRecursive([1, 2, 3, 4], 3))# Output: True (the target value is found in the array)
# print(someRecursive([1, 2, 3, 4], 5))# Output: False (the target value is not found in the array)
# print(isOdd(4))# Output: False (the number is even)
# print(isOdd(7))# Output: True (the number is odd)


#=================================================================================================================================
#winning sum
#Input: 7 9 - 8 -6 -7 8 10    OUTPUT: 19

# numCards = int(input())
# cards = list(map(int, input().split()))

# max_product = cards[0] * cards[1]
# winning_sum = cards[0] + cards[1]

# for i in range(numCards):
#     for j in range(i + 1, numCards):
#         product = cards[i] * cards[j]

#         if product > max_product:
#             max_product = product
#             winning_sum = cards[i] + cards[j]

# print(winning_sum)

#============================================================================================================
#TREE - is a nonlinear data structure with heirchial relationships between its elements without having any cycle.
#The file system on a compiler.

# class Tree:
#    def __init__(self,data):
#      self.data = data
#      self.child = []

#    def addChild(self, object):
#      self.child.append(object)
#      print("Tree Node Added")

#    def __str__(self, level = 0):
#      ret =" "* level + str(self.data) + "\n"
#      for ch in self.child:
#        ret += ch.__str__(level+1)
#      return ret

# rootNode = Tree("Drinks")
# Hot = Tree("Hot")
# Cold = Tree("Cold")
# Tea = Tree("Tea")
# Coffee= Tree("Coffee")
# NonAlcoholic = Tree("NonAlcoholic")
# Alcoholic= Tree("Alcoholic")

# rootNode.addChild(Hot)  #Left
# rootNode.addChild(Cold)  #Right
# Hot.addChild(Tea)
# Cold.addChild(NonAlcoholic)
# Cold.addChild(Alcoholic)
# print(rootNode)

#==============================================================================================

# class Tree:
#    def __init__(self,data):
#      self.data = data
#      self.child = []

#    def addChild(self, object):
#      self.child.append(object)
#      print("Tree Node Added")

#    def __str__(self, level = 0):
#      ret =" "* level + str(self.data) + "\n"
#      for ch in self.child:
#        ret += ch.__str__(level+1)
#      return ret
   
# rootNode = Tree("N1")
# N2 = Tree("N2")
# N3 = Tree("N3")
# N4 = Tree("N4")
# N5 = Tree("N5")
# N6 = Tree("N6")
# N7 = Tree("N7")
# N8 = Tree("N8")

# rootNode.addChild(N2)  #Left
# rootNode.addChild(N3)  #Right
# N2.addChild(N4)
# N2.addChild(N5)
# N4.addChild(N7)
# N4.addChild(N8)
# N3.addChild(N6)
# print(rootNode)
#================================================================================================
