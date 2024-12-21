import random 

# select random number between 1 and 100
RANDOM_NUMBER =  random.randint(0, 100)

# total number of choices
chances_remeaning = 10  


# get number from user 
def getNumber():
    while True:
        num = input("Select a nuber between 0 & 100: ")
        if num.isdigit():
            num = int(num)
            if num <= 100 and num >=0:
                return num
            else:
                print("Pleace select number only between 0 and 100")
        else:
            print("Plese Enter the integer only.")

    

# check 
def playGame():
    # get access of gloabl variable so we can modifiy it latter
    global chances_remeaning 
    while True:
        if chances_remeaning < 1:
            print("You loss the game ")
            print(f'the corect number is {RANDOM_NUMBER}')
            break

        num = getNumber()
        if num == RANDOM_NUMBER:
            print("YOU WON!!\n You guess it rigth")
            print(f"your guess: {num}")
            break
        elif num > RANDOM_NUMBER:
            chances_remeaning -= 1
            print("Select smaller number") 
            print(f"Chance Remaning {chances_remeaning}")
        elif num <  RANDOM_NUMBER:
            chances_remeaning -=1
            print("Select larger number") 
            print(f"Chance Remaning {chances_remeaning}")

# play the game 
playGame()


