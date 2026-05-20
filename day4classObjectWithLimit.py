
# # stack Implementation with size limit

# import sys

# class Stack:
#     def __init__(self, size):
#         self.myStack = []
#         self.stackSize = size

#     def isFull(self):
#         if len(self.myStack) == self.stackSize:
#             return True
#         else:
#             return False

#     def push(self, value):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             self.myStack.append(value)
#             print("Element pushed")

#     def display(self):
#         print(self.myStack)

#     def isEmpty(self):
#         if self.myStack == []:
#             return True
#         else:
#             return False

#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Popped element:", self.myStack.pop())

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Top element:", self.myStack[-1])

#     def deleteStack(self):
#         self.myStack = []
#         print("Stack deleted")


# # Ask user for stack size
# size = int(input("Enter size of stack: "))

# obj = Stack(size)

# print("Stack has been created:")

# while True:
#     print("\n1. Push Operation")
#     print("2. Display Stack")
#     print("3. Pop Operation")
#     print("4. Peek Operation")
#     print("5. Delete Stack")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         value = int(input("Enter value to push in stack: "))
#         obj.push(value)

#     elif choice == 2:
#         obj.display()

#     elif choice == 3:
#         obj.pop()

#     elif choice == 4:
#         obj.peek()

#     elif choice == 5:
#         obj.deleteStack()

#     elif choice == 6:
#         sys.exit()

#     else:
#         print("Invalid choice")







# #program practice...........................................................................
# mylist = [5,7,2,3,7,8,2,3,3]
# newdict = {}
# for i in range(len(mylist)):
#     count = 0
#     key = mylist[i]
#     j = 1
#     while j<len(mylist):
#         if key == mylist[j]:
#             count +=1

#         j = j+1
#     if count>1:
#         newdict[key]= count
# max =newdict
# print(max)









# # Student Management System

# import sys

# students = []

# while True:
#     print("\n----- Student Management System -----")
#     print("1. Add Student")
#     print("2. Show Students")
#     print("3. Update Student")
#     print("4. Delete Student")
#     print("5. Exit")

#     choice = int(input("Enter choice: "))

#     # Add Student
#     if choice == 1:
#         student = {}

#         student["id"] = int(input("Enter ID: "))
#         student["rollno"] = int(input("Enter Roll No: "))
#         student["name"] = input("Enter Student Name: ")
#         student["city"] = input("Enter Student City: ")

#         students.append(student)

#         print("Student added successfully")

#     # Show Students
#     elif choice == 2:
#         if len(students) == 0:
#             print("No student records found")
#         else:
#             for s in students:
#                 print("\nID:", s["id"])
#                 print("Roll No:", s["rollno"])
#                 print("Name:", s["name"])
#                 print("City:", s["city"])

#     # Update Student
#     elif choice == 3:
#         sid = int(input("Enter student ID to update: "))

#         found = False

#         for s in students:
#             if s["id"] == sid:
#                 s["rollno"] = int(input("Enter new Roll No: "))
#                 s["name"] = input("Enter new Name: ")
#                 s["city"] = input("Enter new City: ")

#                 print("Student updated successfully")
#                 found = True
#                 break

#         if found == False:
#             print("Student not found")

#     # Delete Student
#     elif choice == 4:
#         sid = int(input("Enter student ID to delete: "))

#         found = False

#         for s in students:
#             if s["id"] == sid:
#                 students.remove(s)
#                 print("Student deleted successfully")
#                 found = True
#                 break

#         if found == False:
#             print("Student not found")

#     # Exit
#     elif choice == 5:
#         sys.exit()

#     else:
#         print("Invalid choice")


