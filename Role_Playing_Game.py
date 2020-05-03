#Imports
import random
import time

#Useful functions
def choice_validation(x):
    """Turns a string into a user interface. Answers are restricted to the choices.
    
    Arguments:
        x {string} -- Content for user interface
    
    Returns:
       ans {integer} -- User's answer to available choices
    """
    #User interface
    print('\n')
    y = x.split('\n')
    xx = ''
    for z in y:
        xx += z + '\n\n'
    y = xx.split(' ')
    print(xx)
    z = []
    for t in y:
        if ')' in t:
            loc = t.index(')')
            loc -= 1
            z.append(int(t[loc]))
    #Answer restriction
    while True:
        try:
            ans = int(input('Enter the number associated with your decision: '))
            low = min(z)
            high = max(z)
            if ans < low or ans > high:
                print('Invalid answer! Try again.\n')
                print(xx)
                continue
            else:
                break
        except:
            print('You must choose a number. Try again.\n')
            print(xx)
            pass
    return ans

def star_generator(arg):
    """Generates a string of stars to be used with formatting code output
    
    Arguments:
        arg {integer} -- Number of stars needed for string
    
    Yields:
        {string} -- star
    """
    for x in range(arg):
        x = x
        yield '*'

def dash_generator(arg):
    """Generates a string of dashs to be used with formatting code output
    
    Arguments:
        arg {integer} -- Number of dashs needed for string
    
    Yields:
        {string} -- dash
    """
    for x in range(arg):
        x = x
        yield '-'

def layout(delay,*args):
    """Formats the ouput of the code
    
    Arguments:
        delay {integer} -- Length of time delay in between code outputs
        *args {strings} -- Lines of code output
    """
    #Use generators to create strings of stars and dashs used to format the code output
    star = ''
    for x in list(star_generator(150)):
        star += x
    dash = ''
    for x in list(dash_generator(150)):
        dash += x
    #Format and output code
    print('\n',star,'\n',star)
    for arg in args:
        print('\n',dash)
        print('\n',arg)
        time.sleep(delay)
    print('\n',dash)
    return

def combat_tutorial():
    """Gives a tutorial of combat. Strings are stores in the function and output through the layout function.
    """
    wording1 = '''Welcome to combat tutorial!
    You will be given three options at the start of every battle.
    \tOption 1) Fight your opponent 
    \tOption 2) Run away
    \tOption 3) Display Stats.'''
    wording2 = '''Lets dig into each of the options...
    Option 1) How does this work?
    Everyone has stats- Life, Speed, Strength, Weapon, and a few others ;)
    The fight will play out one strike at a time. This process is automated. 
    The person with the highest speed will go first. This speed by will be subtracted by one.
    Next round will re-evaluate who has the highest speed with the adjusted values.
    The magnitude of the strike will be (strength * weapon). Otherwise known as damage.
    The damage will be subtracted from the life of the strike recipient.'''
    wording3 = '''Option 1 Continued..
    This fight will continue until either someone dies, someone runs out of speed (and then dies), 
    or until your life drops below a low threshold. At the low threshold,
    you will be given the same options to re-evaluate with one difference.
    Instead of display stats, you will get the chance to pray to lady luck. Give it a shot!'''
    wording4 = '''If you manage to win your battle, you will be rewarded!
    Rewards will be a slight original (yes original not current) health boost and a random chance to boost
    either strength or speed. In other words, the more battles you win, the better you become at fighting!'''
    wording5 = '''Option 2) Running away like a coward.
    You will be punished. There will be a random chance to nerf either strength or speed.
    If you can fight, you should, or surfer the game's consequences.'''
    wording6 = '''Option 3) Display Stats.
    This option will be display the primary stats of you and your oponent. You only get this 
    option once per fight. It is always suggested to use it to help you decide if you fight
    or flight.'''
    wording7 = '''Lastly, you will notice a few things.
    Some of the enemies you will face will have special abilities.
    For example, goblins are not of human decent. Therefore,
    you will have trouble displaying their stats.'''
    layout(8,wording1,wording2,wording3,wording4,wording5,wording6,wording7)
    return

#Types of characters
#Human class will be the primary parent class
class Human:
    #Define attributes
    def __init__(self,name):
        self.name = name
        self.life = 140
        self.strength = 10
        self.inhuman_id = 0
    #Display attributes. Wll be used in all child classes
    def display(self):
        wording1 = self.name + "\n" + " Weapon damge = " + str(self.weapon) + "\n" + " Life = " + str(self.life) + "\n" + " Speed = " + str(self.speed) + "\n" + " Strength = " + str(self.strength) + "\n"
        layout(2,wording1)
        return 

class Swordsman(Human):
    #Define attributes
    def __init__(self,name):
        self.name = name
        self.life = 140
        self.strength = 10
        self.inhuman_id = 0
        self.weapon = 5
        self.speed = 6

class Hammerman(Human):
    #Define attributes
    def __init__(self,name):
        self.name = name
        self.life = 140
        self.strength = 10
        self.inhuman_id = 0
        self.weapon = 8
        self.speed = 5

class Duelweilder(Human):
    #Define attributes
    def __init__(self,name):
        self.name = name
        self.life = 140
        self.strength = 10
        self.inhuman_id = 0
        self.weapon = 2
        self.speed = 8

class Vampire(Human):
    #Define attributes
    def __init__(self,name):
        self.name = name
        self.life = random.randint(75,175)
        self.weapon = 2
        self.strength = random.randint(1,3)
        self.speed = random.randint(8,13)
        self.inhuman_id = 1

class Warewolf(Human):
    #Define attributes
    def __init__(self,name):
        self.name = name
        self.life = random.randint(75,120)
        self.weapon = 8
        self.strength = random.randint(9,12)
        self.speed = 3
        self.inhuman_id = 2

#Goblin class, the only character class that does not inherit from the Human class
class Goblin:
    #Define attributes
    def __init__(self,name):
        self.name = name
        self.life = random.randint(90,190)
        self.speed = random.randint(1,13)
        self.strength = random.randint(1,12)
        self.weapon = 4
        self.inhuman_id = 0
    #Display a discription based off the attributes. Real numbers will not be shown for this class
    def display(self):
        wording1 = ""
        if self.life < 120:
            wording1 += "%s is sickly ass Goblin." % self.name
            judge = 1
        elif self.life < 150:
            wording1 += "%s is a formidable Goblin." % self.name
            judge = 2
        else:
            wording1 += "%s is one of those Goblins that eats bullets, blades, and blunts for midnight snacks." % self.name
            judge = 3
        if self.speed < 3:
            wording1 += " He moves at turtle warp speed and has "
            judge += 1
        elif self.speed < 8:
            wording1 += " He is an average speedster and has "
            judge += 2
        else:
            wording1 += " Hold the fucking phone he's secretly speedy Gonzales and has "
            judge += 3
        if self.strength < 3:
            wording1 += "puny arms."
            judge += 1
        elif self.strength < 8:
            wording1 += "medicore muscle mass"
            judge += 2
        else:
            wording1 += "arms that scream hercules was made into muscle milk and drank daily."
            judge += 3
        if judge <= 5:
            wording2 = '\nSend this bitch back to the cave.'
        elif judge <= 7:
            wording2 = '\nThink long and hard about this battle.'
        else:
            wording2 = "He's going to fuck you stupid snowflake."
        layout(2,wording1,wording2)
        return

#Enemy class represents a NPC. It has a character tpe and will be used in combat
class Enemy():
    #NPC name pool
    names_npc = ['Bobo', 'Ben Dover', 'Jack Goff', 'Jacky Fister', 'Dick Pound', 'Chew Kok', 'Mister Love', 'Uncle Larry', 'Candy Cummings', 'Phat Ho', 'Greta Uranius', 'Anass Rhammar','Dick Gobbles','Nut Kusher']
    #Introduces the enemy npc and scales attributes based off the user player's level
    def __init__(self,protaginist):
        self.random_option = random.randint(1,7)
        if self.random_option == 1:
            self.type = Swordsman(random.choice(self.names_npc))
            wording1 = '%s the possessed Swordsman has arrived.' % self.type.name
            layout(1,wording1)
        elif self.random_option == 2:
            self.type = Hammerman(random.choice(self.names_npc))
            wording1 = '%s the possessed Hammerman has arrived.' % self.type.name
            layout(1,wording1)
        elif self.random_option == 3:
            self.type = Duelweilder(random.choice(self.names_npc))
            wording1 = '%s the possessed Duelweilder has arrived.' % self.type.name
            layout(1,wording1)
        elif self.random_option == 4:
            self.type = Vampire(random.choice(self.names_npc))
            wording1 = '%s the Vampire has arrived.' % self.type.name
            layout(1,wording1)
        elif self.random_option == 5:
            self.type = Warewolf(random.choice(self.names_npc))
            wording1 = '%s the Warewolf has arrived.' % self.type.name
            layout(1,wording1)
        else:
            self.type = Goblin(random.choice(self.names_npc))
            wording1 = '%s the Goblin has arrived.\n' % self.type.name
            layout(1,wording1)
        self.p = protaginist
        if self.p.level >= 9:
            self.type.life = self.type.life + 400
            self.type.strength += 21
            self.type.speed += 21
        elif self.p.level >= 7:
            self.type.life = self.type.life + 300
            self.type.strength += 16
            self.type.speed += 16
        elif self.p.level >= 5:
            self.type.life = self.type.life + 200
            self.type.strength += 10
            self.type.speed += 10
        elif self.p.level >= 3:
            self.type.life = self.type.life + 100
            self.type.strength += 5
            self.type.speed += 5

#Hero class represents the user's player. It has a character type and will be used in combat
class Hero():
    #Options for lady luck class function
    options = ['Thor','Health Potion','Lightning','Nothing','Rust']
    #Class choices for the user's player
    choices = "Welcome to Survial! \nThis is a world of three classes and you must choose who you will be. \n1) The Swordsman, \n2) The Hammerman, \n3) The Duelweilder."
    #Introduce the user's player.
    def __init__ (self):
        self.answer = choice_validation(self.choices)
        self.namer = input("\nWhat shall we call this powerful hero: ")
        if self.answer == 1:
            self.type = Swordsman(self.namer)
        elif self.answer == 2:
            self.type = Hammerman(self.namer)
        elif self.answer == 3:
            self.type = Duelweilder(self.namer)
        self.type.life += (self.type.life * 0.1)
        self.type.display()
        #Set attributes to reset them later as needed
        self.original_life = self.type.life
        self.original_speed = self.type.speed
        self.original_strength = self.type.strength
        self.original_weapon = self.type.weapon
        #Set values to be used with the levelup function
        self.level = 1
        self.evaluation = 2
    #Lady luck will randomly pull from the options list and remove the pulled option from the list
    def ladyluck(self):
        """Change user player's attributes by random chance. Some improve, some diminish, and some do nothing to the attributes
        """
        if len(self.options) > 0:
            response = random.choice(self.options)
            if response == 'Thor':
                wording1 = 'Thors hammer has fallen into your grasp. Use it wisely'
                layout(1,wording1)
                self.type.weapon += 2
            elif response == 'Health Potion':
                wording1 = 'A Health Potion dropped out of the sky. Drink it dumbass!'
                layout(1,wording1)
                self.type.life += 50
                self.original_life += 25
            elif response == 'Lightning':
                wording1 = 'Lightning strike out of no where! Get electro-fucked.'
                layout(1,wording1)
                self.type.life -= 75
            elif response == 'Nothing':
                wording1 = '... Nothing happens.'
                layout(1,wording1)
            elif response == 'Rust':
                wording1 = '%s discovered his weapon is rusty. Great upkeep dip stick.' % self.type.name
                layout(1,wording1)
                self.type.weapon -= 0.5
            else:
                wording1 = 'error'
                layout(1,wording1)
            self.options.remove(response)
        else:
            wording1 = '... Nothing happens.' #If the options list is empty, nothing will happen
            layout(1,wording1)
        return
    #levelup evaluation will determine if the user should level up based off combat experience. This will be used to scale the enemies attributes
    def levelup_evaluation(self):
        """Based off the change in user player's life from combat experience, the user player's level will be assessed for an increaese
        """
        if self.evaluation == 2:
            if self.original_life >= 200:
                self.level += 1
                self.evaluation += 1
                wording1 = 'Congradulations! You have leveled up to level %d' % self.level
                layout(1,wording1)
        elif self.evaluation == 3:
            if self.original_life >= 250:
                self.level += 1
                self.evaluation += 1
                wording1 = 'Congradulations! You have leveled up to level %d' % self.level
                layout(1,wording1)
        elif self.evaluation == 4:
            if self.original_life >= 300:
                self.level += 1
                self.evaluation += 1
                wording1 = 'Congradulations! You have leveled up to level %d' % self.level
                layout(1,wording1)
        elif self.evaluation == 5:
            if self.original_life >= 350:
                self.level += 1
                self.evaluation += 1
                wording1 = 'Congradulations! You have leveled up to level %d' % self.level
                layout(1,wording1)
        elif self.evaluation == 6:
            if self.original_life >= 400:
                self.level += 1
                self.evaluation += 1
                wording1 = 'Congradulations! You have leveled up to level %d' % self.level
                layout(1,wording1)
        elif self.evaluation == 7:
            if self.original_life >= 450:
                self.level += 1
                self.evaluation += 1
                wording1 = 'Congradulations! You have leveled up to level %d' % self.level
                layout(1,wording1)
        elif self.evaluation == 8:
            if self.original_life >= 500:
                self.level += 1
                self.evaluation += 1
                wording1 = 'Congradulations! You have leveled up to level %d' % self.level
                layout(1,wording1)
        elif self.evaluation == 9:
            if self.original_life >= 550:
                self.level += 1
                self.evaluation += 1
                wording1 = 'Congradulations! You have leveled up to level %d' % self.level
                wording2 = 'You are now at the maximum level!'
                layout(1,wording1,wording2)
        return

#Combat class is the primary class of the game. It pulls the enemy npc and user player into a head-to-head battle. Character types will be given abilities in combat
class Combat():
    #choices for how the user can react to the combat situation
    choices_com = 'What will you do in this time of conflict? \n1) Fight \n2) Flee \n3) Display Stats'
    #Set variable to represent npc enemy, user player, and their speed attributes 
    def __init__(self,protaginist,enemy):
        self.answer_com = choice_validation(self.choices_com)
        self.p = protaginist
        self.ps = protaginist.type.speed
        self.e = enemy
        self.es = enemy.type.speed
        #Display stats option
        if self.answer_com == 3:
            self.p.type.display()
            self.e.type.display()
            choices2 = 'What will you do in this time of conflict? \n1) Fight \n2) Flee'
            answer2 = choice_validation(choices2)
            if answer2 == 1:
                self.answer_com = 1
            else:
                self.answer_com = 2
        #Combat option
        if self.answer_com == 1: 
            hero_down = 0
            if self.e.type.inhuman_id == 2: #If the enemy is a warewolf, a warewolf always takes first strike
                self.p.type.life -= (self.e.type.weapon * self.e.type.strength)
                wording1 = '%s transformed into a wolf and struck %s' % (self.e.type.name, self.p.type.name)
                wordingpl = '%s life: %r' % (self.p.type.name, self.p.type.life)
                wordingel = '%s life: %r' % (self.e.type.name, self.e.type.life)
                if self.p.type.life <= 0: #Evaluate if user player is dead
                    wording2 = '%s is dead. May he rest in pieces' % self.p.type.name
                    layout(1,wording1,wordingpl,wordingel,wording2) #Output damage taken
                    hero_down = 1
                elif self.p.type.life < 50: #Evaluate if user player is close to death
                    wording2 = '%s is gravely injured.' % self.p.type.name
                    layout(1,wording1,wordingpl,wordingel,wording2) #Output damage taken
                    new_choices = 'What will you do now? \n1) Keep fighting to the death! \n2) Run like hell! \n3) Pray to lady luck.' 
                    new_answer = choice_validation(new_choices)
                    if new_answer == 1: #Remain in combat
                        pass
                    elif new_answer == 2: #Flee from combat
                        wording3 = '%s runs away.' % self.p.type.name
                        wording4 = 'For being a coward, he has become a little less powerful.'
                        possibilities = ['strength','speed']
                        possibile = random.choice(possibilities) #If the user player flees from combat, diminish user player's attributes
                        if possibile == 'strength':
                            self.p.type.strength -= 1
                        else:
                            self.p.type.speed -= 1
                        layout(1,wording3,wording4) #Output result of fleeing 
                        hero_down = 1
                    else: #Call laduy luck function
                        self.p.ladyluck()
                        if self.p.type.life <= 0: #Evaluate if user player is dead
                            wording3 = '%s is dead. May he rest in pieces' % self.p.type.name
                            layout(1,wording3) #Output damage taken
                            hero_down = 1
                else:
                    layout(1,wording1,wordingpl,wordingel) #Output the damage taken from the warewolf's hit
            while True:
                if hero_down == 1: #If the enemy is a warewolf and the user player is dead, the combat will end
                    break
                if self.ps >= self.es and self.ps > 0 and self.es > 0: #Regular combat. User player strikes enemy npc
                    self.e.type.life -= (self.p.type.weapon * self.p.type.strength)
                    self.ps -= 1
                    wording1 = '%s struck %s' % (self.p.type.name, self.e.type.name)
                    wordingpl = '%s life: %r' % (self.p.type.name, self.p.type.life)
                    wordingel = '%s life: %r' % (self.e.type.name, self.e.type.life)
                    if self.e.type.life <= 0: #Evaluate if the enemy npc is dead
                        wording2 = '%s is dead. May he rest in pieces' % self.e.type.name
                        wording3 = '%s rests for a moment to catch his breathe. His speed and some of his health has been restored.' % self.p.type.name
                        wording4 = 'After winning the fight, you have grown a little more powerful.'
                        possibilities = ['strength','speed']
                        possibile = random.choice(possibilities) #Boost the user player's attributes
                        if possibile == 'strength':
                            self.p.type.strength += 1.3
                        else:
                            self.p.type.speed += 1.3
                        self.p.original_life += 15
                        if self.p.type.life < (self.p.original_life / 2): #Partial heal if user player is very injured
                            self.p.type.life += (self.p.original_life / 2)
                        else:
                            self.p.type.life = self.p.original_life #Full heal if the user player is slightly injured
                        layout(1,wording1,wordingpl,wordingel,wording2,wording3,wording4) #Output the damage inflicted
                        break #End combat if enemy npc is dead
                    elif self.e.type.life < 50: #Evaluate if enemy npc is close to death
                        wording2 = '%s is gravely injured.' % self.e.type.name
                        if self.p.type.inhuman_id == 1: #If user player is a vampire, kill the enemy npc (vampire special ability)
                            wording3 = '%s fangs extended from his mouth. %s jumps up in the air like a bat and dives down on to %s. %s\'s fangs enter his throat. This is his end..' % (self.p.type.name, self.p.type.name,self.e.type.name,self.p.type.name)
                            wordingel = '%s life: %r' % (self.e.type.name, self.e.type.life)
                            wording4 = '%s rests for a moment to catch his breathe. His speed and some of his health has been restored.' % self.p.type.name
                            wording5 = 'After winning the fight, you have grown a little more powerful.'
                            possibilities = ['strength','speed']
                            possibile = random.choice(possibilities) #Boost the user player's attributes
                            if possibile == 'strength':
                                self.p.type.strength += 1.3
                            else:
                                self.p.type.speed += 1.3
                            self.p.original_life += 15
                            if self.p.type.life < (self.p.original_life / 2): #Partial heal if user player is very injured
                                self.p.type.life += (self.p.original_life / 2)
                            else:
                                self.p.type.life = self.p.original_life #Full heal if the user player is slightly injured
                            layout(1,wording1,wordingpl,wordingel,wording2,wording3,wording4,wording5) #Output damage inflicted (User player is a vampire)
                            self.e.type.life = 0
                            break #End combat if enemy npc is dead
                        else:
                            layout(1,wording1,wordingpl,wordingel,wording2) #Output the damage inflicted (Enemy npc is close to death)
                    else:
                        layout(1,wording1,wordingpl,wordingel) #Output the damage inflicted
                elif self.es > self.ps and self.ps > 0 and self.es > 0: #Regular combat. Enemy npc strikes user player
                    self.p.type.life -= (self.e.type.weapon * self.e.type.strength)
                    self.es -= 1
                    wording1 = '%s struck %s' % (self.e.type.name, self.p.type.name)
                    wordingpl = '%s life: %r' % (self.p.type.name, self.p.type.life)
                    wordingel = '%s life: %r' % (self.e.type.name, self.e.type.life)
                    if self.p.type.life <= 0: #Evaluate if user player is dead
                        wording2 = '%s is dead. May he rest in pieces' % self.p.type.name
                        layout(1,wording1,wordingpl,wordingel,wording2) #Output damage taekn
                        break
                    elif self.p.type.life < 50: #Evaluate if user player is close to death
                        wording2 = '%s is gravely injured.' % self.p.type.name
                        if self.e.type.inhuman_id == 0: #Evaluate if enemy npc is a vampire
                            layout(1,wording1,wordingpl,wordingel,wording2) #Output damage taken (User player is close to death)
                            new_choices = 'What will you do now? \n1) Keep fighting to the death! \n2) Run like hell! \n3) Pray to lady luck.' 
                            new_answer = choice_validation(new_choices)
                            if new_answer == 1: #Remain in combat
                                pass
                            elif new_answer == 2: #Flee from combat
                                wording3 = '%s runs away.' % self.p.type.name
                                wording4 = 'For being a coward, he has become a little less powerful.'
                                possibilities = ['strength','speed']
                                possibile = random.choice(possibilities) #Diminish user player's attributes
                                if possibile == 'strength':
                                    self.p.type.strength -= 1
                                else:
                                    self.p.type.speed -= 1
                                layout(1,wording3,wording4) #Output result of fleeing
                                break
                            else:
                                self.p.ladyluck() #Call laduy luck function
                                if self.p.type.life <= 0: #Evaluate if user player is dead
                                    wording3 = '%s is dead. May he rest in pieces' % self.p.type.name
                                    layout(1,wording3) #Output damage taken
                                    break
                        else: #If enemy npc is a vampire, kill the user player (vampire special ability)
                            wording3 = '%s fangs extended from his mouth. %s jumps up in the air like a bat and dives down on to %s. His fangs enter %s\'s throat. This is the end..' % (self.e.type.name, self.e.type.name,self.p.type.name,self.p.type.name)
                            layout(1,wording1,wordingpl,wordingel,wording2,wording3) #Output damage taken (Enemy npc is a vampire)
                            self.p.type.life = 0
                            break
                    else:
                        layout(1,wording1,wordingpl,wordingel) #Output damage taken
                elif self.ps <= 0: #Evaluate if the user player is out of energy
                    wording1 = '%s has dropped to his knees, exhausted. %s in one fatal blow, chops off %s\'s head!' % (self.p.type.name, self.e.type.name, self.p.type.name)
                    self.p.type.life = 0 #User player dies
                    wordingpl = '%s life: %r' % (self.p.type.name, self.p.type.life)
                    wordingel = '%s life: %r' % (self.e.type.name, self.e.type.life)
                    layout(1,wording1,wordingpl,wordingel) #Output damage taken
                    break
                else: #Evaluate if enemy npc is out of energy
                    wording1 = '%s has dropped to his knees, exhausted. %s in one fatal blow, chops off %s\'s head!' % (self.e.type.name, self.p.type.name, self.e.type.name)
                    self.e.type.life = 0 #Enemy npc dies
                    wordingpl = '%s life: %r' % (self.p.type.name, self.p.type.life)
                    wordingel = '%s life: %r' % (self.e.type.name, self.e.type.life)
                    wording2 = '%s rests for a moment to catch his breathe. His speed and some of his health has been restored.' % self.p.type.name
                    wording3 = 'After winning the fight, you have grown a little more powerful.'
                    possibilities = ['strength','speed']
                    possibile = random.choice(possibilities) #Boost the user player's attributes
                    if possibile == 'strength':
                        self.p.type.strength += 1
                    else:
                        self.p.type.speed += 1
                    self.p.original_life += 15
                    if self.p.type.life < (self.p.original_life / 2): #Partial heal if user player is very injured
                        self.p.type.life += (self.p.original_life / 2)
                    else:
                        self.p.type.life = self.p.original_life #Full heal if user player is slightly injured
                    layout(1,wording1,wordingpl,wordingel,wording2,wording3) #Output damage inflicted
                    break
        else: #Flee from combat
            wording1 = '%s runs away.' % self.p.type.name
            wording2 = 'For being a coward, you have become a little less powerful.'
            possibilities = ['strength','speed']
            possibile = random.choice(possibilities) #Diminish user player's attriubtes
            if possibile == 'strength':
                self.p.type.strength -= 1
            else:
                self.p.type.speed -= 1
            layout(1,wording1,wording2) #Output results of fleeing
        self.p.levelup_evaluation() #Evaluate if user player should level up post-combat
        regen_chance = random.randint(0,5) #Random chance to full heal
        if regen_chance == 3 and self.p.type.life > 0:
            self.p.type.life = self.p.original_life
            wording1 = '%s finds a medkit laying on the ground. Full life has been restored!' % self.p.type.name
            layout(1,wording1) #Output user player life regeneration

#Story part 1- Introduction to the world 
def story_begin():
    """Create the user's player and immerse user in the game world
    
    Returns:
        [object] -- User's player
    """
    you = Hero() #Create user's player
    #Story part 1
    wording1 = 'Loading you into the game...'
    wording2 = '%s wakes up.' % you.type.name
    wording3 = '%s: mmhmm what a dream. I wonder what time it could be.' % you.type.name
    wording4 = '%s gets up to go to the window to see if the sun has started rising.' % you.type.name
    wording5 = 'There\'s a noise. It starts out quiet coming from the other side of the building. %s leans out the window to try to see what\'s causing the sound.' % you.type.name
    wording6 = 'The noise gets louder. Its banging and tossing and rumbling. almost like a fight. %s has to stop leaning before falling out of the window.' % you.type.name
    wording7 = 'A stranger yells "Get out of here now they\'re coming!"'
    wording8 = 'Just then, the door slings open. It\'s Brad, %s friend, comrade, and traveling companion. He looks spaced out as if he\'s not really here.' % you.type.name
    wording9 = '%s takes a step forward and says, "Brad, look man, something\'s going on. I\'m not sure what but that doesn\'t matter. We need to get..."' % you.type.name
    wording10 = 'Brad grabs his sword and lunges at %s!' % you.type.name
    wording11 = '%s dodges and reaches for his weapon: ' % you.type.name
    wording12 = 'Brad goes in for the kill; fiercely and fearless slashing his sword. %s is more trained at combat. A fatal blow is delt to Brad ending his life.' % you.type.name
    layout(2,wording1,wording2,wording3,wording4,wording5,wording6,wording7,wording8,wording9,wording10,wording11,wording12)
    #Give the user the option to have a combat tutorial
    choice_tutorial = 'Welcome to combat would you like a tutorial? \n1) Yes \n2) No'
    answer_tutorial = choice_validation(choice_tutorial)
    #Create a string of dashes to format in between choice and combat tutorial or story part 2
    dash = ''
    for x in list(dash_generator(150)): 
        dash += x
    print('\n',dash)
    #Combat tutorial
    if answer_tutorial == 1:
        combat_tutorial()
    else:
        pass
    return you

#Story part 2- Set up for surival
def story_part_2(you):
    """Give the user an option to react to the situation created in story part 1
    
    Arguments:
        you {object} -- User's player
    """
    options = 'Blood on your hands. Blood on your clothes. What will you do? \n1) Flee for your life. Jump out of the window! \n2) Run down the hallway, down the stairs, and to a window to see what\'s coming.'
    answer_options = choice_validation(options)
    if answer_options == 1:
        wording1 = '%s jumps from the window and lands infront of three gaurds.' % you.type.name
        wording2 = 'The gaurds yell "Seize him! He\'s covered in blood. He must be what the commotion is all about!'
        wording3 = 'Just then a goblin comes from behind and cuts two of the gaurds in half. The other gaurd turns and tries to fight him.'
        wording4 = '%s gets up and grabs his weapon laying on the ground.' % you.type.name
        wording5 = '%s: "What the fuck is going on. Goblins? I\'ve never even seen a goblin. They are from myth. I\'ve got to get out of here."' % you.type.name
        wording6 = '%s runs while the goblin is distracted....' % you.type.name
        wording7 = 'Welcome to survial ;)'
        layout(2,wording1,wording2,wording3,wording4,wording5,wording6,wording7)
    else:
        wording1 = '%s runs down the stairs. There\'s a blood bath. A vampire looks directly at %s' % (you.type.name,you.type.name)
        wording2 = '%s: "What the fuck are you?"' % you.type.name
        wording3 = 'The vampire flys over to %s. %s jumps back and starts running back up the stairs.' % (you.type.name,you.type.name)
        wording4 = 'The vampire grabs %s from behind. His teeth try to go into %s\'s neck.' % (you.type.name,you.type.name)
        wording5 = '%s swiftly places his weapon on his should and the vampire breaks his tooth' % you.type.name
        wording6 = 'The vampire throws %s out of the door all the way across the room.' % you.type.name
        wording7 = 'There is dead bodies everywhere. %s quickly gets up and grabs a weapon next to one of the dead bodies.' % you.type.name
        wording8 = '%s runs before its too late...' % you.type.name
        wording9 = 'Welcome to survival ;)'
        layout(2,wording1,wording2,wording3,wording4,wording5,wording6,wording7,wording8,wording9)
    return

#Survial - the function where the bulk of the game takes place
def survial(you):
    """Create a loop for endless combat with enemy npcs. Break the loop once the user is tired of the game
    
    Arguments:
        you {oject} -- User's player
    """
    counter = 0 #Used to keep track of combat encounters
    #Enless combat encounter loop
    while True:
        counter += 1
        continue_playing = 0 #Variable to be used later for determining if the user should be asked if they would like to keep playing
        wording1 = '%s runs fast and hard through the city looking for survivers.' % you.type.name
        #Verbage options for encountering enemy npcs
        options = ['There\'s a sound from behind.', 
        'Something lands fast and hard beside %s.' % you.type.name, 
        'There is something sprinting at %s from his peripheral.' % you.type.name,
        'Something emerges from a pile of dead bodies.', 
        'A door to a store swings open and something runs towards %s.' % you.type.name, 
        'Something creeps around a corner and sees %s. Its coming at %s, fast!' % (you.type.name,you.type.name), 
        '%s hears a screaming sound. %s turns. Something just killed someone and is now coming for %s.' % (you.type.name,you.type.name,you.type.name),
        '%s smells something awful. It\'s getting worse. Something is close by. It pops out from a bush right next to %s.' % (you.type.name,you.type.name)]
        wording2 = random.choice(options)
        layout(2,wording1,wording2)
        enemy = Enemy(you)
        combat = Combat(you,enemy)
        if you.type.life <= 0: #Evaluate if user's player has died in combat
            wording3 = 'Do you wish to keep playing? \n1) Yes \n2) No'
            continue_playing = 1
            answer = choice_validation(wording3) #Give the user an option to quit after dying
            if answer == 1:
                wording4 = 'A vampire comes by. He drops some of his blood into %s\'s mouth. Rise my minon he says..' % you.type.name
                wording5 = 'A few moments later, after the vampire has given up on reviving %s and left, %s rises up fully healed.' % (you.type.name,you.type.name)
                wording6 = 'Surprisingly, %s is not under th vampire\'s control. But you feel different. Colder and thirsty.' % you.type.name
                layout(2,wording4,wording5,wording6)
                you.type.life = you.original_life
                you.type.inhuman_id = 1 #Turn the user's player into a vampire if the user wants to keep playing
            else:
                wording4 = '%s wake up from his dream. It\'s as if he was sleep walking or sleep killing rather.' % you.type.name
                wording5 = '%s looks around in shock as the entire building is filled with dead bodies.' % you.type.name 
                wording6 = '%s\'s weapon is covered in blood. What have you made him do...' % you.type.name
                layout(2,wording4,wording5,wording6)
                break #End the game
        if continue_playing == 0 and counter > 2: #If the user player did not die and get a chance to end the game, give the user a chance to end the game
            wording3 = 'Congradulations on defeating your enemies. Do you wish to keep playing? \n1) Yes \n2) No'
            answer = choice_validation(wording3)
            if answer == 1:
                counter = 0 #Reset counter if user wants to keep playing
            else:
                break #end the game
    return

#Compile all the functions into one function to call
def game_begin():
    """One function used to call the others
    """
    you = story_begin()
    story_part_2(you)
    survial(you)
    return

#Start the game
game_begin()