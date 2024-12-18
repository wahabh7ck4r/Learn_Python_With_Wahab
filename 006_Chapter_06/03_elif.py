# get age from user 
age = int(input("Enter your age: "))

# we check if user is older than or equal to 18
if age >= 18:  #if yse the print inside of this exucted and ramiaing code skip.
    print('Congratulation! your are free do anything.')

elif age >= 15: # if upper condition flase than this is excuted.
    print("uhh, you're not Independent but still youcan do alot of thing to your own.")

elif age >= 10: # if upper elif false than this is excuted  
    print("your are child,but don't worry you can do things by getting you parents permision.")
    # Note: you can add as more elif as you need. There can be any number of elif.

else: # if all condition are fasle than the else is excuted.
    print("sorry you're too younger.")