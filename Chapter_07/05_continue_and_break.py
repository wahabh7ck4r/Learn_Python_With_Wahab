# we can use this in program when we have to do skip or exit the loop 

# use of break statement 

for i in range(10):
    # when i become 3 stop the loop 
    if i == 3:
        break
    print(i)

print("===========")

# use of continue statement - it only skip thse value where condition met 
for i in range(10):
    # skip the value when this condtion occur and than continue again (means skip one step)
    if i == 3:
        continue
    print(i)
