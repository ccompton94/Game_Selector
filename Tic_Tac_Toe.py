
def winner(xlog, olog):
    """Determines if a player has won the game
    
    Arguments:
        xlog {list} -- All positions taken by x player
        olog {list} -- All positions taken by o player
    
    Returns:
        win {string} -- winner of the game or no winner 
    """
    win = 'No Winner' #Assume no winner until proven otherwise
    #Systematically go through every scenario where a player could have won and evaluate if they did
    if 'T1' in xlog and 'T2' in xlog and 'T3' in xlog:
        win = '\nX player wins!'
    elif 'M1' in xlog and 'M2' in xlog and 'M3' in xlog:
        win = '\nX player wins!'
    elif 'B1' in xlog and 'B2' in xlog and 'B3' in xlog:
        win = '\nX player wins!'
    elif 'T1' in xlog and 'M1' in xlog and 'B1' in xlog:
        win = '\nX player wins!'
    elif 'T2' in xlog and 'M2' in xlog and 'B2' in xlog:
        win = '\nX player wins!'
    elif 'T3' in xlog and 'M3' in xlog and 'B3' in xlog:
        win = '\nX player wins!'
    elif 'T1' in xlog and 'M2' in xlog and 'B3' in xlog:
        win = '\nX player wins!'
    elif 'T3' in xlog and 'M2' in xlog and 'B1' in xlog:
        win = '\nX player wins!'
    elif 'T1' in olog and 'T2' in olog and 'T3' in olog:
        win = '\nO player wins!'
    elif 'M1' in olog and 'M2' in olog and 'M3' in olog:
        win = '\nO player wins!'
    elif 'B1' in olog and 'B2' in olog and 'B3' in olog:
        win = '\nO player wins!'
    elif 'T1' in olog and 'M1' in olog and 'B1' in olog:
        win = '\nO player wins!'
    elif 'T2' in olog and 'M2' in olog and 'B2' in olog:
        win = '\nO player wins!'
    elif 'T3' in olog and 'M3' in olog and 'B3' in olog:
        win = '\nO player wins!'
    elif 'T1' in olog and 'M2' in olog and 'B3' in olog:
        win = '\nO player wins!'
    elif 'T3' in olog and 'M2' in olog and 'B1' in olog:
        win = '\nO player wins!'
    return win

def tto():
    """Tic Tac Toe game
    """
    #Create variable to represent the game display
    T1 = ' '
    T2 = '|   |'
    T3 = ' '
    line1 = '----------'
    M1 = ' '
    M2 = '|   |'
    M3 = ' '
    B1 = ' '
    B2 = '|   |'
    B3 = ' '
    choices = ['Top Left', 'Top Middle', 'Top Right', 'Middle Left', 'Middle Middle', 'Middle Right', 'Bottom Left', 'Bottom Middle', 'Bottom Right'] #Positions the players can take
    count = 2 #Variable for determining player turn
    xlog = '' #log of positions taken by x player
    olog = '' #Log of positions taken by o player
    while True:
        if count % 2 == 0: #If even then it is the x players turn
            print('\n\nX turn!')
            while True:
                print('\n', T1 + T2 + T3, '\n' + line1 + '\n', M1 + M2 + M3, '\n' + line1 + '\n', B1 + B2 + B3,'\n') #Display tic tac toe board 
                num = 1
                numlog = '' #Log how many choices remain
                for x in choices: #Display the positions remaining 
                    print(num,') ' + x)
                    numlog += str(num)
                    num += 1
                try:
                    ans = int(input('\nChoose one: ')) #Ask for the position 
                    #Find the position the player chose 
                    if str(ans) in numlog:
                        find = 1
                        for x in choices:
                            if find == ans:
                                ans = x
                            else:
                                find += 1
                        break
                    else:
                        print('\n\nINVALID CHOICE')
                        continue
                except:
                    pass
            #Systematically go through all the options the player could have choosen, evaluate if they did, and update the display board based off their decision
            if ans == 'Top Left':
                T1 = 'X'
                xlog += 'T1'
            elif ans == 'Top Middle':
                T2 = '| X |'
                xlog += 'T2'
            elif ans == 'Top Right':
                T3 = 'X'
                xlog += 'T3'
            elif ans == 'Middle Left':
                M1 = 'X'
                xlog += 'M1'
            elif ans == 'Middle Middle':
                M2 = '| X |'
                xlog += 'M2'
            elif ans == 'Middle Right':
                M3 = 'X'
                xlog += 'M3'
            elif ans == 'Bottom Left':
                B1 = 'X'
                xlog += 'B1'
            elif ans == 'Bottom Middle':
                B2 = '| X |'
                xlog += 'B2'
            elif ans == 'Bottom Right':
                B3 = 'X'
                xlog += 'B3'
        else:
            print('\n\nO turn!') #If count is odd then it is is o turn 
            while True:
                print('\n', T1 + T2 + T3, '\n' + line1 + '\n', M1 + M2 + M3, '\n' + line1 + '\n', B1 + B2 + B3,'\n') #Display the board 
                num = 1
                numlog = '' #Log how many choices remain 
                for x in choices: #Display the remaining positions 
                    print(num,') ' + x)
                    numlog += str(num)
                    num += 1
                try:
                    ans = int(input('\nChoose one: ')) #Ask the position 
                    #Find the position player chose 
                    if str(ans) in numlog:
                        find = 1
                        for x in choices:
                            if find == ans:
                                ans = x
                            else:
                                find += 1
                        break
                    else:
                        print('\n\nINVALID CHOICE')
                        continue
                except:
                    pass
            #Systematically go through all the options the player could have choosen, evaluate if they did, and update the display board based off their decision
            if ans == 'Top Left':
                T1 = 'O'
                olog += 'T1'
            elif ans == 'Top Middle':
                T2 = '| O |'
                olog += 'T2'
            elif ans == 'Top Right':
                T3 = 'O'
                olog += 'T3'
            elif ans == 'Middle Left':
                M1 = 'O'
                olog += 'M1'
            elif ans == 'Middle Middle':
                M2 = '| O |'
                olog += 'M2'
            elif ans == 'Middle Right':
                M3 = 'O'
                olog += 'M3'
            elif ans == 'Bottom Left':
                B1 = 'O'
                olog += 'B1'
            elif ans == 'Bottom Middle':
                B2 = '| O |'
                olog += 'B2'
            elif ans == 'Bottom Right':
                B3 = 'O'
                olog += 'B3'
        #print('\n', T1 + T2 + T3, '\n' + line1 + '\n', M1 + M2 + M3, '\n' + line1 + '\n', B1 + B2 + B3) #Display the updated board 
        count += 1
        choices.remove(ans) #Remove the taken position 
        if len(choices) == 0: #If there are still positions to choose from, keep the game going
            print('\n\nThe match is a draw!') #It's a draw if there are no more positions to take
            break
        win = winner(xlog,olog) #Call winner function to see if someone won
        if win == 'No Winner': #Keep game going if there is no winner
            pass
        else:
            print('\n',win) #Display winner 
            break
    return

def keep_going():
    """Allow the players to choose to keep playing 
    """
    tto() #Start the game
    while True:
        while True:
            #After the gaem is over, ask the players if they want to play again
            print('\nDo you want to keep playing? \n1) Yes \n2) No')
            answer = input('\nChoose one: ')
            if answer != str(1) and answer != str(2):
                print('\n\nINVALID CHOICE')
                pass
            else:
                break
        if answer == str(1):
            tto() #Play again
        else:
            break #End the game 
    return

keep_going()