# data structures are different ways of organizing data on your computer, that can be used effectively


# def findBiggestNumber(sampleArray):
#     biggestNumber = sampleArray[0]              #O(1)
#     for index in range(1,len(sampleArray)):     #O(N)
#         if sampleArray[index]>biggestNumber:    #O(1)
#             biggestNumber=sampleArray[index]    #O(1)
#     print(biggestNumber)                        #O(1)
# sampleArray =[5,7,9,2,3,4]              
# findBiggestNumber(sampleArray)
# #final total time complexity==========================================>  O(1)+O(1)+O(1)+O(1)+O(N)=O(N)



# def foo(array):
#     sum = 0 #-------------------------------------------------------------> O(1)
#     product = 1 #---------------------------------------------------------> O(1)
#     for i in array:#------------------------------------------------------> O(N)
#         sum += i #--------------------------------------------------------> O(1)
#     for i in array:#------------------------------------------------------> O(N)
#         product *= i #----------------------------------------------------> O(1)   
#     print ("sum="+str(sum)+", Product = "+str(product))#------------------> O(1)




# #linear search
# def linearSearch(array,target):
#     for i in range(0,len(array)):
#         if array[i]==target:
#             return i
# array=[1,2,3,4,8,7,9]
# target=7 # search target value = 7
# linearSearch(array,target)
# result=linearSearch(array,target)
# if result == -1:
#     print("target value not found")
# else:
#     print("element found at index",result)




#removing spaces from string:
#1.rstrip()===>to remove spaces at right hand side
#2.lstrip()===>to remove spaces at left hand side
#3.strip()====>to remove spaces from both sides
# city=input("Enter your city name:")
# scity=city.strip()
# if scity=='Hyderbad':
#     print("Hello hyderbadi..Adab")
# if scity=='Chennai':
#     print("Hello Madrasi..Vanakam")
# if scity=='Banglore':
#     print("Hello Kannadiga..Namaskara")
# else:
#     print("your entered city is invallid")




# #Row wise max value
# #[[100,198,333,323],
# # [122,132,221,111],
# # [223,565,245,764]]
# mylist=[[100,198,333,323],[122,132,221,111],[223,565,245,764]]
# newlist=[]
# for i in range(3):   #i=0
#     j=0
#     max = mylist[i][j]  #[0][0] | max=100
#     for j in range(4):
#         c_max =  mylist [i][j]
#         if max < c_max:
#             max = c_max
#     newlist.append(max)
# print(newlist)



# # input=prashant*is*a*good*programmer
# # output=****prashantisagoodprogrammer
# name = 'prashant*is*a*good*programmer'
# newname=''
# val=''
# for i in name:
#     if i != '*':
#         newname += i
#     else:
#         val+= i
# print(newname)
# print(str(val+newname))





# input=aaabbbbccceeeee
# output=a3b4c3e5
# name = 'aaabbbbccceeeee'
# newname = ''
# count = 1  # Initialize count for consecutive characters
# for i in range(1, len(name)):
#     if name[i] == name[i - 1]:  # Check if the current character is the same as the previous one
#         count += 1 
#     else:
#         newname += name[i - 1] + str(count)  # Append character and its count to newname
#         count = 1  
# newname += name[-1] + str(count)
# print(newname)



# salary = int(input('enter ur salary'))
# rating = int(input('enter ur performance appraisal rating :'))
# increment =0
# if rating >=1 and rating <=3:
#     increment = salary*10/100
# elif rating >=3.1 and rating <=4:
#     increment = salary*30/100
# elif rating >=4.1 and rating <=5:
#     increment = salary*40/100
# else:
#     print('invalid rating')
# print('Incremented salary: ',increment+salary)




# # Basic Salary
# basic_salary = 20000
# # Calculating allowances
# hra = basic_salary * 20 / 100
# ta = basic_salary * 30 / 100
# da = basic_salary * 45 / 100
# # Gross Salary Calculation
# gross_salary = basic_salary + hra + ta + da
# # Displaying results
# print("Basic Salary :", basic_salary)
# print("HRA :", hra)
# print("TA :", ta)
# print("DA :", da)
# print("Gross Salary :", gross_salary)