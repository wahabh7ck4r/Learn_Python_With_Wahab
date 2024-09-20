# creating a dictionarly 
myDict = {
    "box": "daba",
    "book": "kitab",
    "teaher":"ustad"
}
# chek the type of above variable
print(type(myDict))


l = ['a','b','c']  # list is order we can access it by using indexes but in dict we can't do that for this we have you keys to acces valuesbool': True,
#    0    1   2   
# print(myDict['kitab'])  #this line gives error beacuse we cannot access key by using it's value.


# changing value 

myDict["box"] = "pens"
print(myDict)

# cannot contain a duplicate key 
myDict["new"] = "daba"
print(myDict)

# can contain all type of data 
myDict["bool"] = True  #adding booling value 
myDict["list"] = [1,2,3] #addign list
myDict["dict"] = {
    'keys':'values'
}   #adding dictionary in dictionary
print(myDict)




