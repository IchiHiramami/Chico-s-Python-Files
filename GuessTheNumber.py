from random import randint


while True:
    numberToGuess = randint(0,25)
    attempt = 5
    win = False
    while attempt !=0:
        guess = int(input("Guess a number between 0 and 25: "))
        if guess == numberToGuess:
            print ("WOW Galeng naman")
            break
        else:
            print("Wrong answer, try again")
            attempt -= 1

    if win == True:
        print ("Congrats")

    elif win == False:
        print ("Tangina bobo kasi")

    uletulet = input("Retry? [y/n]: ").lower()
    if uletulet == 'y':
        pass
    elif uletulet == 'n':
        break