#Operations of Queue Data structure:-
#{1.EnQueue,2.DeQueue,3.DisplayQueue,4.isEmpty(),5.isFull(),6,Delete(),7.peek()}



# # Implementing Queue with fixed size
# import sys
# class Queue:
#     def __init__(self, size):
#         self.myQueue = []
#         self.queueSize = size
#     # Check Queue is Full
#     def isFull(self):
#         return len(self.myQueue) == self.queueSize
#     # Check Queue is Empty
#     def isEmpty(self):
#         return len(self.myQueue) == 0
#     # Enqueue Operation
#     def enQueue(self, value):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.myQueue.append(value)
#             print(value, "Inserted into Queue")
#     # Display Queue
#     def display(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Queue Elements:", self.myQueue)
#     # DeQueuenOperation (Dequeue)
#     def pop(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             removed = self.myQueue.pop(0)
#             print(removed, "Deleted from Queue")
#     # Peek Operation
#     def peek(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             print("Front Element is:", self.myQueue[0])
#     # Delete Entire Queue
#     def deleteQueue(self):
#         self.myQueue.clear()
#         print("Queue Deleted Successfully")
# # Ask user for Queue size
# size = int(input("Enter the size of Queue: "))
# obj = Queue(size)
# print("Queue has been created")
# # Menu Driven Program
# while True:
#     print("\n1. Enqueue Operation")
#     print("2. Display Queue")
#     print("3. DeQueue Operation")
#     print("4. Peek Operation")
#     print("5. Delete Queue")
#     print("6. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         value = int(input("Enter element to add in Queue: "))
#         obj.enQueue(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.pop()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.deleteQueue()
#     elif choice == 6:
#         print("Exiting Program...")
#         sys.exit()
#     else:
#         print("Invalid Choice")






# Stack using list:- <>Easy to implement,<>speed problem when it grows
# stack using Linked list:- <>fast performance,<>implementation is not eassy

# Time and Space Complexity of Stack Operations
# Operation	        Time Complexity	    Space Complexity
# Create Stack	        O(1)	               O(n)
# Push	                O(1)	               O(1)
# Pop	                O(1)	               O(1)
# Peek / Top	        O(1)	               O(1)
# isEmpty	            O(1)	               O(1)
# Delete Entire Stack	O(1)	               O(1)


# Queue using list:- <>Easy to implement,<>speed problem when it grows
# Queue using Linked list:- <>fast performance,<>implementation is not eassy

# Time and Space Complexity of Queue Operations
# Operation	        Time Complexity	      Space Complexity
# Create Queue	        O(1)                   O(n)
# Enqueue	            O(1)	               O(1)
# Dequeue	            O(1)	               O(1)
# Peek / Front	        O(1)	               O(1)
# isEmpty	            O(1)	               O(1)
# Delete Entire Queue	O(1)	               O(1)






# WAP to accept student name and marks from the keyboard
# and create a dictionary.
# Also display student marks by taking student name.
# students = {}
# n = int(input("Enter number of students: "))
# # Accept student details
# for i in range(n):
#     name = input("Enter student name: ")
#     marks = int(input("Enter student marks: "))
#     students[name] = marks
# # Display dictionary
# print("\nStudent Dictionary:")
# print(students)
# # Search student marks
# search_name = input("\nEnter student name to find marks: ")
# if search_name in students:
#     print("Marks of", search_name, "are:", students[search_name])
# else:
#     print("Student not found")




# # write a program to access each character of string in forward and backward direction by using while loop?
# # input="Learning Python is very easy"  
# s = "Learning Python is very easy"
# # Forward Direction
# print("Forward Direction:")
# i = 0
# while i < len(s):
#     print(s[i], end="")
#     i = i + 1
# print("\n")
# # Backward Direction
# print("Backward Direction:")
# i = len(s) - 1
# while i >= 0:
#     print(s[i], end="")
#     i = i - 1





# # Find missing character between  strings
# s1, s2 = input().split()
# missing = "NA"
# for ch in s1:
#     if ch not in s2:
#         missing = ch
#         break
# print(missing)





# #find vowels from string
# v=['a','e','i','o','u']
# w=input("Enter the word where we will search the vowels:")
# found=[]
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('Found vowels=',found)
# print('unique vowels',len(found),'from the fiven word=',w)






# take N,start,  end as input in first line and list of the integers in second line.use basic for loop and if condition.
# Program to print numbers lying within a given range


# N, start, end = map(int, input().split())
# nums = list(map(int, input().split()))
# for i in nums:
#     if start <= i <= end:
#         print(i, end=" ")

# x,y,z=map(int,input().split())
# mylist =[]
# for i in range(x):
#     a= int(input())
#     mylist.append(a)
# for j in mylist:
#     if j>=y and j<=z:
#         print(j,end=' ')





# # datetime formatting
# import datetime
# date=datetime.datetime.now()
# print("It's now:{:%d/%m/%Y %H:%M:%S}".format(date))





# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)




# # s=[1,4,9,16,25,36,49,64,81,100]
# val=  [2**i for i in range(1,6)]
# print(val)