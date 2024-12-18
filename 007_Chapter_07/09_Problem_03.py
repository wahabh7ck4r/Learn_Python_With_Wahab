# get nubmer from user
num = input("enter the number: ")

# if user enter a number than typecast it into integer otherwise promt a masage invalid number
if num.isdigit():
    num = int(num)
else:
    print("Invalid number")

for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")
    