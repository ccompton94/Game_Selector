def Games():
    """Interface to allow the user to select a game to play.
    """
    while True: #Allow the user to select different games even after one is finished
        try: #Get user's choice
            choice = int(input('\n\nWhich game would you like to play? \n\n1) Rock Paper Scissors \n\n2) Guessing Game \n\n3) Cow Bull \n\n4) Tic Tac Toe \n\n5) Survival (Role Playing Game) \n\n6) Quit Playing \n\nChoose one: '))
        except ValueError:
            print('\n\nERROR: You must enter the number associated with the option.') #Error if user doesn't pick a number
            continue
        #Evaluate user's choice
        if choice == 1:
            import Rock_Paper_Scissors
        elif choice == 2:
            import Guessing_Game
        elif choice == 3:
            import Cow_Bull
        elif choice == 4:
            import Tic_Tac_Toe
        elif choice == 5:
            import Role_Playing_Game
        elif choice == 6:
            break
        else:
            print('\n\nERROR: You must choose between options 1, 2, 3, 4, 5, and 6') #Error if user picks a number outside of the options
    return


Games()