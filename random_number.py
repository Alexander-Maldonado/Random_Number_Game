# guessing game in terminal
import random #python document to generate random is imported to run random.randit

def guess(x):  #x will be an int that wiill be used in the following function
    random_number= random.randint(1,(x))  # random randit is used to randomly select an interger between ((a) & (b))
    guess = 0 # in order for the loop to exist the guess must have a value. In this case 0 is selected because the random_number will never = 0 since we are starting at int 1
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))  # the user will be able to make a prediction and an int is only accepted 
        if guess < random_number:
            print("Sorry, Try again. Too low.")
        elif guess > random_number:
            print("Sorry, Try again. Too high")
    print(f"Congratulations You Guessed The Number {random_number} Correctly") # code will ignore while loop if guess iis correct

#guess(50)  # 50 iis taking the place of x in the function above


def computer_guess(x): #computer will attemp to guess your number
    low = 1 #variable will be used to have the computer continue guessing and we can guide the computer to the correct answer
    high = (x)
    value = ""
    while value != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low # or high (low == high)
        value= input(f"Was {guess} to high (h), too low (l), or correct (c) ")
        if value == "h":
            high = guess - 1 # we want the computer to keep guess but know that a higher number than the guess doesn't exist
        if value == "l":
            low = guess + 1 # the guess cannot be lower and must be a higher interger
    print(f"I guessed the number {guess} correctly!")

computer_guess(100)
