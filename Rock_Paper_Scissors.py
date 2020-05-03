def rps():
    """Rock Paper Scissors against AI or against a friend. 
    """
    print('\nGet ready to play Rock Paper Scissors!')
    #Allow the user to play against a friend or the A.I.
    while True:
        try:
            ans = int(input('\n\nWho do you want to play against? \n1) A.I. \n2) Friend \nChoose one: '))
            if ans > 2 or ans < 1:
                print('\nYou only have two choices.')
                continue
            break
        except ValueError:
            print('\nYou must choose the number associated with the option.')
    if ans == 1:
        while True:
            #A.I. random choice 
            import random
            u1 = random.randint(1,3) # 1 = Rock, 2 = Paper, 3 = Scissors
            rps_dic = {1:'Rock', 2:'Paper', 3:'Scissors'}
            while True: #User choice 
                try:
                    u2 = int(input('\nWhat\'s your pick? \n1) Rock \n2) Paper \n3) Scissors \nChoose one: '))
                    if u2 < 1 or u2 > 3:
                        print('\nInvalid choice! Try again.')
                        continue
                    break
                except ValueError:
                    print('\nYou must choose the number associated with the option.')
            print('\nTrust me I\'m not cheating. I choose my answer before you. I choose: {}'.format(rps_dic[u1])) #Reassure User 
            #Evaluate the choices made to determine a winner
            if u1 == u2:
                print('Its a tie!')
            elif u1 == 1 and u2 == 2:
                print('You win!')
            elif u1 == 1 and u2 == 3:
                print('I win!')
            elif u1 == 2 and u2 == 1:
                print('I win!')
            elif u1 == 2 and u2 == 3:
                print('You win!')
            elif u1 == 3 and u2 == 1:
                print('You win!')
            elif u1 == 3 and u2 == 2:
                print('I win!')
            #Ask the user if they would like to keep playing
            while True:
                try:
                    answer = int(input('\n\nDo you want to keep playing? \n1) Yes \n2) No \nChoose one: '))
                    if answer > 2 and answer < 1:
                        print('\nYou only have two choices.')
                        continue
                    break
                except ValueError:
                    print('\nYou must choose the number associated with the option.')
            if answer == 2:
                break
    else:
        print('\nHere is how this works. You choose your response. Don\'t let your friend see.\nThen let your friend choose and don\'t watch what they choose.') #Rules 
        while True:
            while True: #User 1 choice
                try:
                    u1 = int(input('\nUser 1, what\'s your pick? \n1) Rock \n2) Paper \n3) Scissors \nChoose one: '))
                    if u1 < 1 or u1 > 3:
                        print('\nInvalid choice! Try again.')
                        continue
                    break
                except ValueError:
                    print('\nYou must choose the number associated with the option.')
            #Space the users apart so user 2 cannot cheat
            for space in range(100):
                print('\n')
            while True: #User 2 choice
                try:
                    u2 = int(input('\nUser 2, what\'s your pick? \n1) Rock \n2) Paper \n3) Scissors \nChoose one: '))
                    if u2 < 1 or u2 > 3:
                        print('\nInvalid choice! Try again.')
                        continue
                    break
                except ValueError:
                    print('\nYou must choose the number associated with the option.')
            #Evaluate the choices made and determine a winner
            if u1 == u2:
                print('\nIts a tie!')
            elif u1 == 1 and u2 == 2:
                print('\nUser 2 wins!')   
            elif u1 == 1 and u2 == 3:
                print('\nUser 1 wins!')
            elif u1 == 2 and u2 == 1:
                print('\nUser 1 wins!')
            elif u1 == 2 and u2 == 3:
                print('\nUser 2 wins!')
            elif u1 == 3 and u2 == 1:
                print('\nUser 2 wins!')
            elif u1 == 3 and u2 == 2:
                print('\nUser 1 wins!')
            #Ask the user if they would like to keep playing
            while True:
                try:
                    answer = int(input('\n\nDo you want to keep playing? \n1) Yes \n2) No \nChoose one: '))
                    if answer > 2 and answer < 1:
                        print('\nYou only have two choices.')
                        continue
                    break
                except ValueError:
                    print('\nYou must choose the number associated with the option.')
            if answer == 2:
                break
    return

rps()