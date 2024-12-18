# To keep this course simple, I'll use examples that explain arguments clearly.
# Don't worry about argument types; just focus on how they work.

# Defining a function
def welcome(name):  # This function greets the user by name
    print(f"Welcome, {name}!")

# Calling the function with an argument
welcome("Wahab")

# Now, let's think about a worst-case scenario: what if the user calls the function without a name?
# In such cases, we can use a default parameter so the function still works even if no name is provided.

# Creating the same function as above, with a minor change (adding a default parameter)
def welcome2(name='Sir'):
    print(f"Welcome, {name}!")

# Calling the function without passing an argument
welcome2()  
# It also works if we pass an argument
welcome2("Hammad")
