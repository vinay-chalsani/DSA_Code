# name = "prashantjha"  #this is our string
#     #012345678910
# print(name[0]) #p
# print(name[1])    
# print(name[-1])
# #print(name[15])
# print(name[0:5])
# print(name[1:])
# print(name[:5])#rashantjha
# print(name[:1])#5-1=4 prash
# print(name[1:8:2])#'''8-1=7
# print(name[::-1])#reverse of string



# s="Python are High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())


#format function..........................................................
# name="vinay"
# sal=5000
# age=23
# print("{} sal is {} age is {}".format(name,sal,age))
# print("{0} sal is {1} age is {2}".format(name,sal,age))
# print("{x} sal is {y} age is {z}".format(x=name,y=sal,z=age))
# A=1
# print(f"{A}is a a good boy")



# name="prashant"
# for i in name: #i=0
#     print(i)



#i/p =prashant
#o/p =prashnt
#WAP to remove duplicate char
# name="prashant"
# newname =""
# for i in name:#i=0:p
#     if i not in newname:
#         newname += i
# print(newname)



#i/p =prashant
#o/p =tnahsarp
# #WAP to reverse char
# name="prashant"
# newname =""
# N = len(name)#8
# for i in range(N-1,-1,-1):#i=6:n
#     newname += name[i]
# print(newname)




#check the pallindrome:
#question:  WAP to check if a given string ia a palindrome
#logic:    use loops to compair char from start and end
# name = "racecar"
# print(name)
# print(name[::-1])
# if name == name[::-1]:
#     print("palindrone")
# else:
#     print("Not palindrone")



#check vowels and consonants, to count number of vowels and consonents
#input="hello"
#output=Vowels:2, Consonants:3
# vowels =['a','e','i','o','u']
# name = "hello"
# cons=0
# vow=0
# for i in name: 
#     if i in vowels:
#         vow+=1
#     else:
#         cons+=1
# print(cons)
# print(vow)



# check for anagram
# input=listen, output=silent
# str1 = "listen"
# str2 = "silent"
# Check for anagram
# if sorted(str1) == sorted(str2):
#     print("Anagram")
# else:
#     print("Not Anagram")




#count words in string
#input=this is a sentence, output= 4
#use loop to count spaces and words
#WAP tp count numbers of words in a string
# Input
# s = "this is a sentence"
# # Count words using loop
# count = 1
# for ch in s:
#     if ch == " ":
#         count += 1
# # Output
# print("Number of words:", count)



#BODMAS...................................................
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)#160
# print((a-b)*(c/d))
# print(a+(b*c)/d)





#secretmessage agency provides message ecoding and decoding services for secure data transfer.
#the first step in decoding includes removel of special char and with whitespaces from the message as special characters and whitespaces do not hold any meaning
#  write an algorithm to help the agency find no of special char and white spaces in a given message input= it consists of string message , representing the message that need to be decoded by the agency
# message = "gasgg54@#vscd!s*"
# special = 0
# spaces = 0
# for ch in message:
#     if ch == " ":
#         spaces += 1
#     elif not ch.isalnum():
#         special += 1
# print("Number of spaces =", spaces)
# print("Number of special characters =", special)




# input=this is a text, to apply title................................................
# message = "this is a test"  #this is our string
# print(message.title())




# print('prashantjha777'.isalnum())
# print('prashantjha'.isalpha())
# print('777f'.isdigit())
# print('sdsdsdsd'.islower())
# print(''.islower())
# print('PRASHANTj'.isupper())
# print('My Name Is Prashant'.istitle())
# print(''.istitle())
# print(''.isspace())




# print("prashant".find("r"))
# print("prashant".index("r"))
# print("prashant jha".count("a"))




#   1 1 1
#   2 2 2 
#   3 3 3
# for i in range(1,4):
#     for j in range(1,4):
#         print(i ,end =" ")
#     print()




# n=int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()




    
# n=int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print("*",end=" ")
#     print()




# n=int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print()



# import time
# n=int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     print("  "*(n-i),end=" ")
#     for j in range(i,i+1):
#         time.sleep(3)
#         print("*",end=" ")
#     print()