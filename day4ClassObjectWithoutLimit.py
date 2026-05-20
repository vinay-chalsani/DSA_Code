# class Name:
#     age = 30
#     def display(self):
#         print("Hello world")
# obj = Name()
# print(obj.age)
# obj.display()




# class Student:
#     def __init__(self) :
#         self.nsme ="Prashant"
#         self.age =30
#     def display(self):
#         print("Name=",self.name)
#         print("Age=",self.age)
# stuObj = Student()
# print(stuObj)
    



# class Message:
#     def __init__(self):
#         print("I am constructor")
#     def shows(self):
#         print("Class program")
# obj = Message()
# obj.shows()
# obj2=Message()




# #parameterised constructor
# class StudentInfo():
#     def __init__(self,name,age,roll_no):
#         self.Name=name
#         self.Age=age
#         self.RollNo=roll_no
#     def displayStudentInfo(self):
#         print("Name",self.Name)
#         print("Age",self.Age)
#         print("roll_no",self.RollNo)
# studentObj = StudentInfo("Prakash",34,101)
# studentObj.displayStudentInfo()




# #stack Implementation without size limit
# import sys
# class Stack:
#     def __init__(self):
#         self.myStack =[]
#     def push(self, value):
#         self.myStack.append(value)
#         print("element push")
#     def display(self):
#         print(self.myStack)
#     def isEmpty(self):
#         if self.myStack == []:
#             return True
#         else:
#             return False
#     def pop(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.myStack.pop())
#     def peek(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.myStack[-1])
#     def deleteStack(self):
#         self.myStack = None
# obj = Stack()
# print("Stack has created :")
# while True:
#     print("1.Push Operation :")
#     print("2.Display stack :")
#     print("3.Pop operation :")
#     print("4.peek operation :")
#     print("5.Delete stack :")
#     print("6.Exit ")
#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#         value = int(input("enter value to push in stack :"))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     elif choice == 3:
#         obj.pop()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.deleteStack()
#     else:
#         sys.exit