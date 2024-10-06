# get jobTitle and age from user 
age  = int(input("Enter your age: "))
jobTitle = input("Enter your job title: ").lower()  #lower() convert in to small abc like this "Hello" --->"hello"


# stroed availbel job in the list 
availbel_jobs  = ['datascince', "machinelearning", 'computer', "ai", 'softwarenginner']

# we chcek both user age and what kind of job for user serching for if both condtion are true then print insede of if ise excuted.

# for understanding purpose 
print(age > 18)    
print(jobTitle in availbel_jobs)
# let's suppose user enter age 19 and jobTitle coputer than that kind of things happen: 
    # True        True
            #True 
if age > 18 and jobTitle in availbel_jobs:
    print("yes, you can apply for the job") 


# use of or operator 
have_job = input("yes(y)/No(n): ").lower()
# no matter user is 1 year old or two 
#     True        False
#          True 
if age > 18 or jobTitle in availbel_jobs: 
    print("yes , you're eligible ") 
    # you can also add else for better understanding if both condtion are false than else is excuted  
else:
    print("Sorry we can't allow child and poor to marry.")


#NOt convert ture to false and false to true 
print(not False)



