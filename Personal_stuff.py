import random

RandomNumber = random.randint(1,10)

while True:
    
    Guess = int(input('Guess a number between 1 and 10: '))

    if Guess == RandomNumber:
        print(f"Good Job! The number was {RandomNumber}")
        break
    else:
        print('Try Again')

print("Press enter to exit")