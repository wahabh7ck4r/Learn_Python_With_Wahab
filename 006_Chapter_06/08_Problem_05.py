# get user detail for scholarshilp (GPA and Family income)

GPA = float(input("Enter you GPA: "))
familyIncome = int(input("Enter you family income: "))

# if user met any condtion tell him he is eligible otherwise tell him there is no scholarship availble for you now.

if GPA >= 3.5 or familyIncome <= 50000 :
    print("Eligible for scholarship.")
else:
    print("Not eligible for scholarship.")