s = input("Enter anything: ") # take input from user 

reverse_string = ''

for i in range(len(s)):
    reverse_string += s[-1 - i]


print(reverse_string)