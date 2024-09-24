# creating a set - There are two way to create a set 

# 1. 
S1 = set()  # this is an empty set you can add value by using add() method like this : 
S1.add(4)
print(S1)


# 2
S2 = {1,2,3,4,5,5}    #you can use this syntax to create a non-empty set if you wnat to create an empty set you must you 1. way beacuse in python "{}" this is dictionary until you don't add value for set.
print(S2)   

chekctype1 = set()
print("empty set type1: " , type(chekctype1))
chekctype2 = {}    # this will give <class 'dict'> beacuse in pyton this is a syntax for empty dictionary if you want to create empty set you have to use - set()
print("empty set type2: ", type(chekctype2))