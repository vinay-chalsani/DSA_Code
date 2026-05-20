# #program to reverse each word in a string
# #logic:-split string into words, reverse eachword and join them back together
# #input:-"Hello world"
# text = "Hello world"
# words = text.split()
# reversed_words = [word[::-1] for word in words]
# result = " ".join(reversed_words)
# print(result)





# #program to check if a string contain parenthesis is valid
# #logic:-use stack to keep track of open and close parentheses
# #input:-"{{{{}}}}"
# text = "{{{{}}}}"
# stack = []
# pairs = {
#     ')': '(',
#     '}': '{',
#     ']': '['
# }
# for char in text:
#     if char in "({[":
#         stack.append(char)
#     elif char in ")}]":
#         if not stack or stack[-1] != pairs[char]:
#             print("Invalid Parentheses")
#             break
#         stack.pop()
# else:
#     if not stack:
#         print("Valid Parentheses")
#     else:
#         print("Invalid Parentheses")





# #insertion sort
# arr = [3, 5, 8, 6, 2]
# for i in range(1, len(arr)):
#     key = arr[i]
#     j = i - 1
#     while j >= 0 and arr[j] > key:
#         arr[j + 1] = arr[j]
#         j -= 1
#     arr[j + 1] = key
# print("Sorted array:", arr)





# #selection sort
# arr = [20, 12, 10, 15, 2]
# print("Initial Array:", arr)
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]
#     print(f"After swapping index {i} and {min_index}: {arr}")
# print("Sorted Array:", arr)






# #write a function to sort a dictionary by keys or values in accending or decending order
# # input:- "C":3,"B":2,"A":1) 
# def sort_dict(data, by="key", order="asc"):
#     reverse = order == "desc"

#     if by == "key":
#         return dict(sorted(data.items(), key=lambda item: item[0], reverse=reverse))
#     elif by == "value":
#         return dict(sorted(data.items(), key=lambda item: item[1], reverse=reverse))
#     else:
#         raise ValueError("by must be 'key' or 'value'")

# data = {"C": 3, "B": 2, "A": 1}

# print(sort_dict(data, by="key", order="asc"))
# print(sort_dict(data, by="key", order="desc"))
# print(sort_dict(data, by="value", order="asc"))
# print(sort_dict(data, by="value", order="desc"))





# types of variable(instance var)
# class New:
#     def __init__(self):
#         self.a=10

# obj1= New()
# obj2= New()
# obj3= New()
# obj1.a=20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)




# #static variable
# class New:
#     a=10
#     def __init__(self):
#         self.name=""
# obj1= New()
# obj2= New()
# obj3= New()
# New.a=50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)




# #combination of static and instance
# class College:
#     collegename="Modern college"
#     def __init__(self):
#         self.studentname = "prashant"
# principal = College()
# teacher = College()
# account = College()
# print("principal=",principal.collegename,"....",principal.studentname)
# print("teacher=",teacher.collegename,"....",teacher.studentname)
# print("account=",account.collegename,"....",account.studentname)
# College.collegename="HBD"
# principal.studentname="prashant jha"
# print("principal=",principal.collegename,"|",principal.studentname)
# print("teacher=",teacher.collegename,"|",teacher.studentname)
# print("account=",account.collegename,"|",account.studentname)





# #linked list
# class Node:
#     def __init__(self,date):
#         self.data = date
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
# linkedList = LinkedList()
# linkedList.head = Node(5)
# second          = Node(10)
# third           = Node(15)
# fourth          = Node(20)
# linkedList.head.next = second
# second.next = third
# third.next = fourth
# while linkedList.head!= None:
#     print(linkedList.head.data,"|",linkedList.head.next,"->",end=" ")
#     linkedList.head = linkedList.head.next






# #to create a Dynamic node
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def add_end(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node

#     def add_begin(self, value):
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node

#         if self.tail is None:
#             self.tail = new_node

#     def add_between(self, value, pos):
#         new_node = Node(value)

#         if pos == 0:
#             self.add_begin(value)
#             return

#         temp = self.head
#         for _ in range(pos - 1):
#             if temp is None:
#                 print("Invalid position")
#                 return
#             temp = temp.next

#         new_node.next = temp.next
#         temp.next = new_node

#         if new_node.next is None:
#             self.tail = new_node

#     def display(self):
#         temp = self.head
#         if temp is None:
#             print("List is empty")
#             return

#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

# if __name__ == "__main__":
#     ll = LinkedList()

#     while True:
#         print('\n1. Add Node Linkedlist')
#         print('2. Add Node in Beginning')
#         print('3. Add Node in Between')
#         print('4. Add Node in End')
#         print('5. Display Linked List')
#         print('6. Exit')

#         ch = int(input('Enter your choice: '))

#         if ch == 1:
#             value = int(input("Enter value: "))
#             ll.add_end(value)
#             print("Node added at end")

#         elif ch == 2:
#             value = int(input("Enter value: "))
#             ll.add_begin(value)
#             print("Node added at beginning")

#         elif ch == 3:
#             value = int(input("Enter value: "))
#             pos = int(input("Enter position: "))
#             ll.add_between(value, pos)
#             print("Node added in between")

#         elif ch == 4:
#             value = int(input("Enter value: "))
#             ll.add_end(value)
#             print("Node added at end")

#         elif ch == 5:
#             ll.display()

#         elif ch == 6:
#             break

#         else:
#             print("Invalid choice")




                # OR




# import sys
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
        
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None
        
#     def addNode(self,value):
#         self.node = Node(value)    
#         if self.head is None:
#             self.head = self.node
#             self.tail = self.node
#         else:
#             self.tail.next = self.node
#             self.tail     = self.node
            
            
#     def addatbegin(self,value):
#         print("add node begining")
#         self.node = Node(value)
#         if self.head is None:
#             self.head = self.node
#             self.tail = self.node
#         else:
#              self.node.next = self.head
#              self.head =  self.node
            
#     def display(self):
#         while self.head is not None:
#             print(self.head.data,"|","->",end=" ")
#             self.head = self.head.next
#         print()
    
    
# if __name__ == '__main__':
#     object = Linkedlist()
#     while True:
#         print("1.Add node in linkedlist")
#         print("2.Add node in begining")
#         print("3.Add node in between")
#         print("4.Add node in End")
#         print("5.Display Linkedlist")
#         print("6.Exit")
#         ch = int(input("enter your choice:"))
#         if ch == 1:
#             value = int(input("enter value for node:"))
#             object.addNode(value)
#             print("Node Successfully Added in single linkedlist:")
            
#         elif ch == 2:
#             value = int(input("enter value for node:"))
#             object.addatbegin(value)
            
#         elif ch == 5:            object.display()
#         elif ch == 6:            sys.exit()


