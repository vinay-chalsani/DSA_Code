myList = ["Jay","Om","Priya","Diya",77,"Niya",60,52,"jay"]
# print(myList)
# print(type(myList))#<List>
# print(myList[0])#jay
# print(myList[1])#om
# print(myList[2])#priya
# print(myList[-1])#jay
# print(myList[2:5])
# print(myList[:5])
# print(myList[1:])
# print(myList[1:8:2])


# myList[2]="Omkar"
# print(myList)


# if"Priya" in myList:
#     print("yes Priya is available")
# else:
#     print("mot available")



# myList.append('Harsh')
# myList.append('Laxman')
# print(myList)


# myList.insert(3,"Vinay")
# print(myList)


# myList.remove("Niya")
# print(myList)

# newlist= myList.copy()
# print(newlist)

# myList = [['Prashant','jha'],[85,86],[440022,"yyy"]]
# print(myList)
# print(myList[0][0])#prashant
# print(myList[0][1])#jha
# print(myList[1][0])#85,56
# print(myList[2][0])#440022
# print(myList[2][1])#yyy


# list2 =[50,25,50,'Prashant']
# del list2[2]
# #del list2
# print(list2)


# list2 =[50,25,50,'Prashant']
# list2.clear()
# print(list2)


# name="Prashant"
# print(name)
# myname=list(name)
# print(myname)


# myList=[44,23,77,8,9,88]
# #myList.sort()
# myList.sort(reverse=True)#for decending order
# print(myList)


# myList=[44,23,77,8,9,88]
# newlist= myList
# print(id(myList))
# print(id(newlist))

# myList=[44,23,77,8,9,88]
# for i in myList:
#     print(i)



#i/p=[0,1,4,0,2,5] o/p=[1,4,2,5,0,0] move 0 in last
# list1 = [0,1,4,0,2,5] 
# for i in list1: 
#     if i==0:
#         list1.remove(i)
#         list1.append(i)
# print(list1)


#to find second largest element [7,3,9,2,8]
# list1 = [7,3,9,2,8]
# list1.sort()
# print(list1[-2])

#MCQ------------------------------------------------->  sol=error
# a=[1,2,3,4,5,6,7,8,9]
# a[: :2]=10,20,30,40,50,60
# print(a)



#MCQ------------------------------------------------->  sol=4,3,2
# a=[1,2,3,4,5]
# print(a[3:0:-1])


#MCQ------------------------------------------------->  sol=4,7,11,15
# arr=[[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
# for i in range(0,4): 
#     print(arr[i].pop())



#MCQ------------------------------------------------->  sol=2,3,4,5,6,6
# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]
# for i in range(0,6):
#     print(arr[i],end=" ")


#MCQ- ADVANCE------------------------------------------------->  sol=
# fruit_list1=['Apple','Berry','Cherry','papaya']
# fruit_list2=fruit_list1
# fruit_list3=fruit_list1[:]
# fruit_list2[0]='Guava'
# fruit_list3[1]='Kiwi'
# sum=0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0] == 'Guava':
#         sum+= 1
#     if ls[1] =='kiwi':
#         sum+=20
#         print(sum)


#MCQ
# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]
# for i in A:
#     if i in B and i in C:
#         print(i)



