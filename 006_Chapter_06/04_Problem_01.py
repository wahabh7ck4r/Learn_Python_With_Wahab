# list of availbel name that are selceted for interview.

selectedNames = ['wahab', 'tony', 'harry', 'kashan']

# list of reaming jobs 
available_jobs = ['python', 'java', 'teacher', 'programer', 'web developer', 'AI', 'data science']


# ask user to enter their name  
name = input("Enter your name: ")

# check name 
if name in selectedNames:
    # ask user to enter their job title
    title = input("inter you job tile: ").lower()
    # check is that post still availble 
    if title in available_jobs:
        print("your interview will be conducted soon.")
    else:
        print("we're sorry! a candidte is selected for that post.")
else:
    print("you're not selected for the interview.")
    