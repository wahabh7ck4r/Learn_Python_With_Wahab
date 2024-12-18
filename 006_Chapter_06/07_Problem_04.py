# ask user to enter a number
number = int(input("Enter the number:"))

# perform given conditions 
if number/3 and number/5:
    print("Divisible by both 3 and 5.")
elif number/3 or number/5:
    print("Divisible by 3 or 5, but not both.")
else:
    print("NOt divisible by 3 or 5.")
    