# age=33
# pi=3.14
# name="Vinay"
# result= True
# print(type(age))
# print(type(pi))
# print(type(name))
# print(type(result))


# math=50
# phy=50
# chem=50
# print(id(math))
# print(id(chem))
# print(id(phy))



# print(2+2)
# print("2"+"2")
# a= int(input("Enter the first number: "))
# b= int(input("Enter the second number: "))
# print(a+b)



#int() used to cover in integer 33.14=int=3
# print(int(3.14))
# print(int(10+5))
# print(int(True))
# print(int(False))
# #print(int("4,22"))
# print(int("4"))
# print(int("4"))
# #print(int("Vinay"))



#float used  for decimal point
# print(float(3.14))
# print(float(10+5))
# print(float(True))
# print(float(False))
# #print(float("4,22"))
# print(float("4"))
# print(float("4"))
# #print(float("Vinay"))



# #complex() used to convert
# print(complex(3.14))
# print(complex(10+5))
# print(complex(True))
# print(complex(False))
# #print(complex("4,22"))
# print(complex("4"))
# print(complex("4"))
# #print(complex("Vinay"))



#bool() used to convert into returntype
# print(bool(3.14))
# print(bool(10+5))
# print(bool(True))
# print(bool(False))
# #print(bool("4,22"))
# print(bool("4"))
# print(bool("4"))
# #print(bool("Vinay"))




# #simple if
# a=int(input("Enter any single digit :"))
# if a>0:
#     print("positive number")
# if a<0:
#     print("negative number")
# if a==0:
#     print("zero")



# day = input("Enter a day: ").lower()
# days = ["monday", "tuesday", "wednesday",
#         "thursday", "friday", "saturday", "sunday"]
# if day in ["saturday", "sunday"]:
#     print("Weekend")
# else:
#     print("Working Day")



# per=65
# if per >=65:
#     print("grade A")
# elif per <=65 and per>=50:
#     print("Grade B")
# else:
#     print("Fail")



# chr = ord(input("Enter any one character :"))#b
# if chr >=65 and chr<=90:
#     print("Upper case")
# elif chr >97 and chr <=122:
#     print("Lower case")
# elif chr >=48 and chr <=57:
#     print("digit")
# else:
#     print("special symbol")



#membership operator
# name="help4code"
# print('p' not in name)




#identity operator for address compairation
# math = 50
# chem = 50
# print(math is chem)



#for(initialization : condition; inc/dec)
#for i in range(2,11,2): 
   # print(i)
# for i in range(2,11,2):
#     print(i)




# for i in range(1,11):
#     print(i*2)



# # Tables 1 to 10 on top
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{j} x {i} = {j*i:<3}", end="\t")
#     print()
# # Line separator
# print("-" * 140)
# # Tables 11 to 20 below corresponding tables
# for i in range(1, 11):
#     for j in range(11, 21):
#         print(f"{j} x {i} = {j*i:<3}", end="\t")
#     print()





#wap to accept there paper marks and calculate total, percentage and check if he/she is passed in all subjects so print pass else print fail , if percentage is greater than 65 and gender is male then he is eligible for placement else not
# a = int(input("Enter marks 1: "))
# b = int(input("Enter marks 2: "))
# c = int(input("Enter marks 3: "))
# gender = input("Enter gender: ")
# total = a + b + c
# per = total / 3
# print("Total =", total)
# print("Percentage =", per)
# if a >= 35 and b >= 35 and c >= 35:
#     print("Pass")
    
#     if per > 65 and gender == "male":
#         print("Eligible for Placement")
#     else:
#         print("Not Eligible")      
# else:
#     print("Fail")




# a = 1
# b = 5

# while a <= 5:
#     if a != 3:
#         print(a, "\t", b)
    
#     a = a + 1
#     b = b - 1





# b = 5

# for a in range(1, 6):
#     if a != 3:
#        print(a, "\t", b)
    
# b = b - 1
# b = 5

# for a in range(1, 6):
#     if a != 3:
#         print(a, "\t", b)
    
#     b = b - 1