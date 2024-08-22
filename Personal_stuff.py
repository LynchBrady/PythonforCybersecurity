import random
#random.randint[1,10]
RandomNumber = ('3')#random.randint(1)

UserGuess = int(input("Guess the number between 1 and 10: "))

while UserGuess > 0:
    if UserGuess == (RandomNumber):
            print('Good Job!')
            break
    else:
          if UserGuess == RandomNumber:
                (print('Good Job!'))
                break