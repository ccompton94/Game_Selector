def cow_bull():
    """Cow Bull is a 4 digit number guessing game. 
    """
    import random
    ran = []
    for i in range(4):
        nums = random.randint(0,9)
        ran.append(nums)
    ran_str = '' #Format to be a string for display
    for x in ran:
        ran_str += str(x)
    attempts = 0
    while True:
        while True:
            while True:
                try:
                    guess = input('\nEnter your four number guess (type quit to end the game): ')
                    if guess.upper() == 'QUIT':
                        break
                    check = int(guess) #Make sure there are four numbers entered 
                    if len(guess) != 4:
                        print('You must enter four numbers.')
                        continue
                    break
                except ValueError:
                    print('You must enter four numbers.')
            if guess.upper() == 'QUIT': #Allow the user to give up
                print('You tried {} time(s) to guess: {} \nBetter luck next time!'.format(attempts,ran_str))
                break
            else:
                attempts += 1
                g = []
                for x in guess:
                    g.append(int(x))
                cow = 0 #Correct number in correct position
                bull = 0 #Correct number incorrect position
                index = 0
                for y in g: #Evaluate guess
                    if y in ran:
                        if y == ran[index]:
                            cow += 1
                        else:
                            bull +=1
                    index +=1
                if cow == 4:
                    print('Congraduations you won! It took you {} attempts.'.format(attempts)) #User won, end game
                    break
                else:
                    print('Cow = {} Bull = {}'.format(cow,bull)) #Results if user did not win
        while True: #Ask the user if they would like to keep playing
            try:
                answer = int(input('\n\nDo you want to keep playing? \n1) Yes \n2) No \nChoose one: '))
                if answer > 2 and answer < 1:
                    print('\nYou only have two choices.')
                    continue
                break
            except ValueError:
                print('\nYou must choose the number associated with the option.')
        if answer == 2: #End program
            break
    return

cow_bull()