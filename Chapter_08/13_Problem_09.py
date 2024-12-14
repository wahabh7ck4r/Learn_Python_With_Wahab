def combine_args_kwargs(*args, **kwargs):
    # in args we get list of name that pass the exam 
    print("List of student that pass the exam: ")
    for i in args:
        print(i)

        # To make them info seprate
    print("\n")
    # in kawargs we display where the the next text is and aslo what they need to do 
    print("NEXT ROUND INFO: ")
    for key, value in kwargs.items():
        print(key, ": ", value)

    # if i don't return the funtion also print none at the end (because it return none when nothings return).
    return ""    

# excute the funtion to check is it
print(combine_args_kwargs(("wahab", 'kamran', 'nomi', 'hammad', 'zaheer'), location="Islamabad", number=50 , passing_marks=23, subjects = ["ENGLISH", "MATHS", "PHYSICS"]))
    