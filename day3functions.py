# i=1
# while i<=5:
#     print(i)
#     i+=1



#function
# def hello():  #called function
#     print("hello world")
# hello() #calling function
# hello()



# def arithmatic():
#     a = int(input("enter value of a:"))
#     b = int(input("enter value of b:"))
#     sum=a+b
#     sub=a-b
#     div=a/b
#     mul=a*b
#     return sum,sub,div,mul 
# # print(arithmatic())
# result =arithmatic()
# print("arithmatic = ",result)






#types of arguments we pass in function?
# 1.positional argument
# 2.keyword argument
# 3.default argument
# 4.variable length argument / variable number of argument


# def arithmatic(a, b):
#     sum=a+b
#     sub=a-b
#     div=a/b
#     mul=a*b
#     return sum,sub,div,mul 
# # 1.positional argument
# result =arithmatic(5,5)
# print("arithmatic = ",result)


# # 2.keyword argument
# def credential(username, password):
#     if username == password:
#         print("login sucessfully")
#     else:
#         print("invalid credentials")
# credential(username="admin",password="admin")#calling function



# # 3.default argument
# def cityName(city ="Pune"):
#     print(city)
# cityName("Nagpur")
# cityName("Mumbai")
# cityName()



# # 4.variable length argument
# def cityName(*name):
#     print(name)
# cityName("Nagpur","Delhi","Mumbai","pune")




# # Modularity approach in function
# import sys
# def add():
#     a=int(input("enter value of A:"))
#     b=int(input("enter value of B:"))
#     print(a+b)
# def sub():
#     a=int(input("enter value of A:"))
#     b=int(input("enter value of B:"))
#     print(a-b)
# def div():
#     a=int(input("enter value of A:"))
#     b=int(input("enter value of B:"))
#     print(a/b)
# def mul():
#     a=int(input("enter value of A:"))
#     b=int(input("enter value of B:"))
#     print(a*b)
# while True:
#     print("1.Addition")
#     print("2.Subtraction")
#     print("3.Divison")
#     print("4.Multiplication")
#     print("5.Exit")
#     choice=int(input("Enter your choice:"))
#     if choice == 1:
#         add()
#     elif choice == 2:
#         sub()
#     elif choice == 3:
#         div()
#     elif choice == 4:
#         mul()
#     elif choice == 5:
#         sys.exit()

