# Get number from user to calculate the factorial
num = int(input("Enter the number: "))

# Initialize the factorial variable to 1 (since factorial of 0 is 1)
factorial = 1 

# Initialize the counter variable
i = num 

# Loop until the counter is greater than 1
while i > 1:
    factorial *= i  # Multiply the current value of factorial by i
    i -= 1          # Decrement i by 1

print(f"The factorial of {num} is: {factorial}")
