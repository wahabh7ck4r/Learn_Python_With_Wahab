serach_string = "this the the python file creadted by wahab for learning purpose."

# it will return the index of given string
print(serach_string.find("file"))
print(serach_string[20:24])

# check strign with end "."
print(serach_string.endswith("e"))  # it's return True if string endwith "." otherwise Flase.

# it will capitalize the string means convert first letter big 
capitalize_str = serach_string.capitalize()
print(capitalize_str)

# it will change string into uppercase 
upper_str = serach_string.upper()
print(upper_str)

# it will change into lowercase 
lower_str = upper_str.lower()
print(lower_str)

# it will replace given word with provided word 
new_str = serach_string.replace("wahab", "hammad")
print(new_str)

# it willremove first occurance in the string
print(serach_string.replace("the","",1 ))