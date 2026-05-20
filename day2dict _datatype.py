# mydict={
#     101:"prashant",
#     102:"ashish",
#     "103":"mohini",
#     "104":"trivani",
#     101:"ashish",
#     104:"ashish"
# }
# print(mydict)



# a = mydict[102]
# print(a)


# mydict[102]="peter"
# print(mydict)

# for x in mydict:
#     print(x)


# for x in mydict.values():
#     print(x)


# for x, y in mydict.items():
#     print(x, y)
    


# mydict["mobile_no"]= 8888488766
# print(mydict)




# mydict.pop(101)
# print(mydict)


# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[(4,5)])



# a = {'a':1,'b':2,'c':3}
# print(a[('a','b')])



# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1
# print (arr)
# sum = 0
# for k in arr:
#     sum += arr[k]
# print(sum)



# my_dict = {}
# my_dict[1] = 1
# my_dict['1']=2
# my_dict[1.0] = 4
# print(my_dict)
# sum=0
# for k in my_dict:
#     sum += my_dict[k]
# print (sum)




# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)]= 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)



# box = {}
# jars = {}
# crates = {}
# box['biscuit']=1
# box['cake']=3
# jars['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(len(crates[box]))



# dict = {'c': 97,'a': 96,'b': 98}
# for _ in sorted(dict):
#     print (dict[_])


# rec = {'Name': "Python","Age":"20","addr" : "NJ","Country" : "USA"}
# id1 = id(rec)
# del rec
# rec = {'Name': "Python","Age":"20","addr" : "NJ","Country" : "USA"}
# id2 = id(rec)
# print(id1 == id2)




#write a key with min value in a dictionary ,input={"x":20,"y":10,"2":30}
# input_dict = {"x": 20, "y": 10, "2": 30}
# min_key = min(input_dict, key=input_dict.get)
# print(min_key)




#function to count frequency of elements in a list using a dictionary, input=[1,2,2,3,4,3,5]
# def count_frequency(lst):
#     counts = {}# empty dictionary
#     for item in lst:# iterate through list
#         if item in counts:# if already present
#             counts[item] += 1
#         else:# first occurrence
#             counts[item] = 1
#     return counts
# input_list = [1, 2, 2, 3, 4, 3, 5]
# result = count_frequency(input_list)
# print(result)





# num = 123  #321
# a =num % 10 #a=3
# num = num // 10 #num=12
# b = num % 10 #b=2
# c = num // 10 #c=1
# rev = a*100 + b*10 + c*1   #300+20+1=321
# print(rev) #123456 = 654321



