# binary search is faster than linear search
# half of the remaining elements can be eliminated at a time, insted of eliminiting them one by one
# it only works on sorted array




# def binarySearch(array,target):
#     low=0
#     high=len(array)-1
#     while low <=high:
#         mid=(low+high)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# array =[2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
# target=72
# result = binarySearch(array, target)
# if result == -1:
#     print("element not found")
# else:
#     print("element found at",result)




# #bubble sort
# def bubbleSort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):
#             if array[j] > array[j+1]:
#                 temp = array[j]
#                 array[j]=array[j+1]
#                 array[j+1]=temp
#                 print(array)
#             print()           
# array =[64,34,25,12,22,11,90]
# bubbleSort(array)






# to find security key of data 
# n=input()
# count=0
# for i in range(10):
#     if n.count(str(i))>1:
#         count += 1
# if count ==0:
#     print(-1)
# else :
#     print(count)
