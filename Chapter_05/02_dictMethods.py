a = {
    "name":"wahab",
    "friend":"hammad",
    "course": "python",
    "marks":[21, 22, 99, 98]
}


# get()
print(a.get("name"))   # same as ---> a['name']

# new = tuple(a["name"])
# print("".join(new))
# print(type(new))
# items()
print(a.items())  # it will give key value pair in tuples 
# new = tuple(a["name"])
# print("".join(new))
# print(type(new))

# update()
a.update({'box': 'daba'})   #same as ---> a['box'] = 'daba'
print(a)

# keys()
print(a.keys())  #it will give keys 

# values()  
print(a.values())   # it will give values 

# new = tuple(a["name"])
# print("".join(new))
# print(type(new))



