# create an empty set 
Myset = set()

# adding value to the set of different dtype 
Myset.add(5) #add integer
Myset.add(5.) # add float
Myset.add("harry potter") # adding string 
Myset.add((3,4))  #adding tuple 


# print it 
print(Myset)

# try to add list in set and check what happend 
# Myset.add([1,2,3,4,5]) -->  this give an error beacuse it is an unhasble type in python ting like list are unhashbel means they can change after creating so these are not suitable for things like dictaiony key and set items .

# trying to chage mutble objet in set like tuble 
