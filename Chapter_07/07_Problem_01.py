# There are many way to print a even number and we're using the simplest way 


# for loop 
for i in range(2, 21 , 2): # in this case for loop start from 2 and end at 20 and 2 means skip 1 value like firstly i is two than skip 3 i become 4 and so on ...
    print(i)


# also we can use if statement in a loop to print even number 
print("=========")
for i in range(2, 21):
    # check condtion for even number 
    if i % 2 == 0:
        print(i)


