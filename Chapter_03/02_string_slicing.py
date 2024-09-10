name  = "this is the first line" 

print(name[0:3]) # give first three letter only 
print(name[0:])  # give full name
print(name[6:14]) # white spces also count

# negative index
print(name[:])  # it will give comple name  (or equal to print(name))
print(name[-4:]) # - equal to print(name[17:])
print(name[:-4]) # - equal to print(name[:17])

# reserved string using negative index 
print(name[::-1]) 


