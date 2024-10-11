# get the marks of the sutednt 
marks = int(input("Enter you marks(0 - 100): "))

# if marks is grater than equal to 90 than give grade A

if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks < 80:
    print("C")
elif marks >= 60 and marks < 70:
    print("D")
elif marks < 60 and marks > 0:
    print("F")
else:
    print("Please Enter valid marks.")

    