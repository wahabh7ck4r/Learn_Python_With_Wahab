packed = (33,44,33)

a,b,c = packed
print(a)
print(b)
print(c)

# another example  
packed_tuple = (33, (33, 43), 33) 

d , (e, f ), g = packed_tuple   #if i dont add bracket it will error  if you don't add bracket then "e" storue whole tuple insted of single value 
print(d)
print(e)
print(f)
print(g)

# like in this case b store whole tuple (33, 43)
h , i , j = packed_tuple
print(h)
print(i)
print(j)








