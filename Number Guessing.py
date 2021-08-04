import random

minNumber = 1
maxNumber = 10

while(True):
    try:
        guess = int(input(f"Enter 0 To Exit\nGuess a Number Between {minNumber} and {maxNumber} : "))
        numberToGuess = random.randint(1, 10)
        if(guess == 0):
            break
        elif(numberToGuess == guess):
            print("Your Guess is Right!")
        else:
            print(f"Your Guess is Not Right! The Number Was {numberToGuess}")
    except:
        print("Wrong Input")
    finally:
        print("---------------------------")