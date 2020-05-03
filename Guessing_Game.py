def ggo():
    """Guessing game. Guess the random number choosen 
    """
    import random
    #Allow the user to select the range for the game (high and low values)
    print('\nGet ready to play the guessing game! Lets start with the boundaries..')
    while True:
        while True:
            try:
                low = int(input('\nWhat is the lowest number you want to include in my guess? By the way, I do not accept negative numbers! : '))
                if low < 0:
                    print('Come on now, play by the rules. Lets try that again.')
                    pass
                else:
                    break
            except ValueError:
                print('ERROR: Enter the number as an integer')
        while True:
            try:
                high = int(input('\nWhat is the highest number you want to include in my guess? By the way, anything over 1000 is going to take all day: '))
                if high > 1000:
                    print('Dude seriously, I don\'t have all day and neither do you. Lets try that again.')
                    pass
                else:
                    break
            except ValueError:
                print('ERROR: Enter the number as an integer')
        #Evaluate the range selected by the user.
        if low >= high:
            print('Your range is invalid. Please try again.')
        else:
            break
    value = random.randint(low,high) #Get a random number within the range specified by the user
    attempt = 0 #Track the number of attempts taken by the user
    #Start the game
    while True:
        while True:
            attempt += 1
            bad_attempt = 0
            while True:
                #Evaluate the user's guess against the provided range and the rules of the game
                try:
                    guess = input('\nWhat number am I thinking? It\'s between %d and %d. (Type \'exit\' to quit) \nEnter your guess: ' % (low, high))
                    if guess.upper() == 'EXIT' or guess.upper() == 'QUIT':
                        break
                    guess = int(guess)
                    if guess > high:
                        print('Clearly you guessed too high... Try again.')
                        bad_attempt += 1
                        continue
                    elif guess < low:
                        print('Clearly you guessed too low... Try again.')
                        bad_attempt += 1
                        continue
                    else:
                        break
                except ValueError:
                    print('You must type a number value or \'exit\' to quit.')
            if str(guess).upper() == 'EXIT' or str(guess).upper() == 'QUIT':
                break
            elif guess == value:
                print('\nCongradulations you guessed correct! It took you %d tries.' % (attempt + bad_attempt))
                break
            elif guess > value:
                print('\nYou guessed too high.')
                attempt += 1
            else:
                print('\nYou guessed too low.')
                attempt += 1
        #Ask the user if they would like to play again
        while True:
            try:
                nxt = int(input('\nDo you want to play again? \n1) Yes \n2) No \nChoose one: '))
                if nxt < 1 or nxt > 2:
                    print('\nThere are only two options.')
                    continue
                break
            except ValueError:
                print('ERROR: You must type the number associated with the option.')
        if nxt == 2:
            break
    return

ggo()

#Make while loops more efficient 
#Check if the high value is lower than the low. Print error and start over if true