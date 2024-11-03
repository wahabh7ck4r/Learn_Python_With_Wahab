# you can return value in a function like when you need sum of number and someone ask to create  a function that do this.
# what will you do ? 


# let's check what happend if we don't return it 
def sum(x, y):
    s = x + y

s = sum(3, 5) 
print(s)  # in that why you need need to use the print inside the sum but if user need to the sum in variable the you must use return like if we return sume in above function than s store the sum(x + y)

# let's try 

def return_sum(x, y):
    s = x + y
    return s

s = return_sum(3, 5) # now s store the value of x + y 
print(s)

# you can also use to stop the funtion excution usign return like: 


def check(age):
    if age < 18:
        return None
    
    print("====WELCOME=========")

# In that case if age is grater than 18 than funtion print welcome otherwise if condition become true and funtion return none before excuting print

age = int(input("Enter the age: "))

check(age)


# NOTE: if a function doesn’t have a return statement, it returns None by default. So, without return, the function runs but doesn’t give any output to the caller.