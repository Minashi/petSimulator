import random
import threading
import time
import sys


# ---------------------------------------------------------------------------------------------------- TODO figure
#  out how to have options replace whats on screen, so the game does not go down terminal
#  add more casino games,
#  Add jobs
#  add more speak phrases to speak() method
#  implimend death
#  ---------------------------------------------------------------------------------------------------- Information:
#  This will be a simulator of having a pet. At first there will just be basic functions. No databases of saving
#  functions will be implemented yet. With this, I will use lists, functions, math logic, and a game loop.
#  ----------------------------------------------------------------------------------------------------


# Class for titleScreen
class Title_Screen:
    def aboutPage(self):
        print("\nDeveloper: Brandon Gonzalez\n")
        time.sleep(1)
        titleScreen()

    def leaveGame(self):
        print("Are you sure you want to leave?")
        action = input(">")
        if action.lower() == 'yes':
            quit()
        else:
            titleScreen()


# Class blueprint for the pet
class PetStats:
    def __init__(self, name, age, breed, cleanliness, happiness, hunger, thirst, currency, location, food, water):
        self.name = name
        self.age = age
        self.breed = breed
        self.cleanliness = cleanliness
        self.happiness = happiness
        self.hunger = hunger
        self.thirst = thirst
        self.currency = currency
        self.location = location
        self.food = food
        self.water = water
        self.statusEffects = []

    # Prints the stats of the pet
    def printStats(self):
        print("########################################################################")
        print("\nName:", self.name, "Age:", self.age, "Breed:", self.breed, "Location:", self.location, )
        print("\n-Inventory:", "\n\tFood:", self.food, "\n\tWater:", self.water, "\n\tCurrency:", self.currency)
        print("\n-Stats:\n\tHunger:", self.hunger, "\n\tThirst:", self.thirst, "\n\tHappiness:", self.happiness,
              "\n\tCleanliness:", self.cleanliness)
        print("Status Effects:", self.statusEffects)
        print("\nType anything to return to the game.")
        print("########################################################################")
        input(">")

    # Leave game method
    def leaveGame(self):
        global leave
        global isExiting
        print("\nAre you sure you want to leave?", self.name, "will miss you! 'Yes/No'")
        action = input()
        if action.lower() == 'yes':
            leave = False
            isExiting = True
            return leave, isExiting
        else:
            return leave

    # PET ACTIONS

    def speak(self):
        dogSpeak = ['Ruff Ruff!', 'WOOOOOOF!', 'BARK BARK BARK!!!!']
        catSpeak = ['MEOW!', 'meoooooooooooooooooow', 'meeeooooOOOooooOWOOOOOOWW!']
        if self.breed == petTypes[0]:
            print(random.choice(dogSpeak))
        elif self.breed == petTypes[1]:
            print(random.choice(catSpeak))

    def age(self):
        self.age += 1

    def statDecrease(self):
        self.cleanliness -= 10
        self.happiness -= 10
        self.hunger -= 10
        self.thirst -= 10

    def status(self):
        if self.cleanliness < 50:
            print('\n', self.name, "is dirty!")
            if 'dirty' not in self.statusEffects:
                self.statusEffects.append('dirty')
        elif self.cleanliness > 50 and 'dirty' in self.statusEffects:
            self.statusEffects.remove('dirty')
        if self.happiness < 50:
            print('\n', self.name, "is unhappy!")
            if 'unhappy' not in self.statusEffects:
                self.statusEffects.append('unhappy')
        elif self.happiness > 50 and 'unhappy' in self.statusEffects:
            self.statusEffects.remove('unhappy')
        if self.hunger < 50:
            print('\n', self.name, "is hungry!")
            if 'hungry' not in self.statusEffects:
                self.statusEffects.append('hungry')
        elif self.hunger > 50 and 'hungry' in self.statusEffects:
            self.statusEffects.remove('hungry')
        if self.thirst < 50:
            print('\n', self.name, "is thirsty!")
            if 'thirsty' not in self.statusEffects:
                self.statusEffects.append('thirsty')
        elif self.thirst > 50 and 'thirsty' in self.statusEffects:
            self.statusEffects.remove('thirsty')
        else:
            return

    def petOptions(self):
        print("What would like to do with", self.name, "?")
        print("#####    Clean            #####")
        print("#####    feed             #####")
        print("#####    Give water       #####")
        print("#####    play with        #####")
        print("#####    Return           #####")
        action = input(">")
        if action.lower() in ['play', 'play with']:
            self.play()
        elif action.lower() in ['give food', 'feed']:
            self.feed()
        elif action.lower() in ['give water']:
            self.giveWater()
        elif action.lower() in ['clean']:
            self.clean()

    # Cleaning method
    def clean(self):
        if self.location != locations[1]:
            return "You have to be at home to clean", self.name
        else:
            if self.cleanliness < 100:
                print("You're currently cleaning", myPet.name, "...\n")
                time.sleep(3)
                self.cleanliness = self.cleanliness + 10
                myPet.speak()
                return "\nYou have cleaned,", self.name, "\n"
                if self.cleanliness > 50 and 'dirty' in self.statusEffects:
                    self.statusEffects.remove('dirty')
                    return self.name, " is no longer dirty!"
            else:
                print(self.name, "is already fully cleaned!")

    # Playing method
    def play(self):
        if self.location != locations[3]:
            return "You have to be at the park to play with", self.name
        else:
            if self.happiness < 100:
                print("You're playing with", self.name, "...\n")
                time.sleep(3)
                self.happiness = self.happiness + 10
                myPet.speak()
                return "\nYou have played with,", self.name, "\n"
                if self.happiness > 50 and 'unhappy' in self.statusEffects:
                    self.statusEffects.remove('unhappy')
                    return self.name, " is no longer unhappy!"
            else:
                print(self.name, "is tired!")

    # Feeding method
    def feed(self):
        if self.location != locations[1]:
            print("You have to be at home to feed", self.name)
        else:
            if self.hunger < 100:
                if self.food <= 0:
                    return "You don't have any food...\nYou can buy some from the store."
                else:
                    self.food -= 1
                    print("You're currently feeding", self.name, "...\n")
                    time.sleep(3)
                    print("\nYou have fed,", self.name, '\n')
                    self.hunger = self.hunger + 10
                    if self.hunger > 50 and 'hungry' in self.statusEffects:
                        self.statusEffects.remove('hungry')
                        return self.name, " is no longer hungry!"
                    else:
                        myPet.speak()
                        return "You still have", self.food, "food left.", "\n"
            else:
                print(self.name, "is full.")

    # Giving water method
    def giveWater(self):
        if self.thirst < 100:
            if self.water <= 0:
                return "You don't have any water...\nYou can buy some from the store."
            else:
                self.water -= 1
                print("You're currently giving", self.name, "water...\n")
                time.sleep(3)
                print("\nYou have gave,", self.name, "water.\n")
                self.thirst = self.thirst + 10
                if self.thirst > 50 and 'thirsty' in self.statusEffects:
                    self.statusEffects.remove('thirsty')
                    return self.name, " is no longer thirsty!"
                else:
                    myPet.speak()
                    return "You still have", self.water, "water left.", "\n"
        else:
            print(self.name, "is full.")

    # Options menu
    def options(self):
        print("##############################################################################################")
        print("\nHelp Menu\n")
        print("Change pet name: 'change name'\nRestart: 'restart'")
        print("To return to game: 'return'\n")
        print("##############################################################################################")
        action = input(">")
        if action == 'change name':
            print("What would you like to change the name to?")
            self.name = input(">")
        elif action == 'restart':
            global restart
            restart = True
        elif action == 'return':
            return

    # TRAVELING
    def travel(self):
        print("#########################################################")
        print("Travel:")
        print("\nWhere would you like to go?")
        print("\nAvailable locations:", locations[0:5])
        print("\nTo return type 'return'")
        print("#########################################################")
        action = input(">")
        while action.lower() != 'store' and action.lower() != 'home' and action.lower() != 'streets' and action.lower() != 'park' and action.lower() != 'dababy' and action.lower() != 'return' and action.lower() != 'casino':
            print("I'm not sure that place exists... Please try again.")
            action = input(">")
        else:
            if action == 'store':
                self.store()
            elif action == 'home':
                self.home()
            elif action == 'streets':
                self.streets()
            elif action.lower() == 'park':
                self.park()
            elif action.lower() == 'casino':
                self.casino()
            elif action.lower() == 'dababy':
                while True:
                    print(
                        "DABABY DABABY DABABY DABABY DABABY DABABY DABABY DABABY DABABY DABABY DABABY DABABY DABABY DABABY ")
            else:
                return

    # LOCATIONS
    def home(self):
        print("Traveling...\n")
        time.sleep(1)
        self.location = locations[1]
        print("You are now home!")
        return

    def streets(self):
        print("Traveling...\n")
        time.sleep(1)
        print("The streets have not been made yet...")
        return

    def store(self):
        print("Traveling...\n")
        time.sleep(1)
        lastLocation = self.location
        self.location = locations[2]
        print("###############################################")
        print("Currency:", "$", self.currency)
        print("\nWelcome to PetMart! What would you like to buy?")
        print("\nWater: $5\nFood: $10")
        print("\nTo leave type 'leave or leave store'\n###############################################")
        action = input(">")
        while action.lower() != 'water' and action.lower() != 'food' and action.lower() != 'leave' and action.lower() != 'leave store':
            print("I'm not sure I understand you? Please try again...")
            action = input(">")
        else:
            if action.lower() == 'water' and self.currency != 0:
                print("How much water do you want to buy?")
                amount = input(">")
                while amount.isdigit() is False:
                    print(amount, "is not a valid amount of water!")
                    amount = input(">")
                else:
                    amount = int(amount)
                    cost = amount * 5
                    while amount < 0 or self.currency < cost or amount == 0:
                        print("Sorry! You don't have enough money for that...\n")
                        print("How much water do you want to buy?")
                        amount = int(input(">"))
                        cost = amount * 5
                    else:
                        if cost == 0:
                            print("0 is not a valid amount...")
                            print("Come again!")
                            self.location = lastLocation
                            return
                        else:
                            self.water += amount
                            self.currency -= cost
                            print("You bought", amount, "water!")
                            print("\nThank you! Come again!")
                            self.location = lastLocation
                            return
            elif action.lower() == 'food' and self.currency != 0:
                print("How much food do you want to buy?")
                amount = input(">")
                while amount.isdigit() is False:
                    print(amount, "is not a valid amount of food!")
                    amount = input(">")
                else:
                    amount = int(amount)
                    cost = amount * 5
                    while amount < 0 or self.currency < cost or amount == 0:
                        print("Sorry! You don't have enough money for that...\n")
                        print("How much food do you want to buy?")
                        amount = int(input(">"))
                        cost = amount * 5
                    else:
                        if cost == 0:
                            print("Come again!")
                            self.location = lastLocation
                            return
                        else:
                            self.food += amount
                            self.currency -= cost
                            print("You bought", amount, "food!")
                            print("\nThank you! Come again!")
                            self.location = lastLocation
                            return
            elif action.lower() in ['leave', 'leave store']:
                self.location = lastLocation
                return
            elif self.currency == 0:
                print("I'm sorry.... But you don't have any money...")
                self.location = lastLocation
                return
            else:
                print("Error in store")
                exit()

    def park(self):
        print("Traveling...\n")
        time.sleep(1)
        self.location = locations[3]
        print("You are now at the park!")
        return

    def casino(self):
        print("##########################################")
        print("Welcome to the casino!")
        print("Available games:\n50/50")
        action = input()
        while action != '50/50':
            print("That game doesn't exist. Please try again!")
            action = input()
        else:
            if action == '50/50':
                print("Welcome to 50/50!!!\nThis is basically just a coin flip game. If you guess the right side, "
                      "you double your money!")
                print("How much would you like to wager?")
                wager = input()
                if self.currency >= int(wager):
                    print("Are you sure you want to wager", wager, '?')
                    action = input()
                    while action.lower() != 'no' and action != 'yes':
                        print("Please answer yes or no...")
                        action = input()
                    else:
                        if action.lower() == 'yes':
                            print("Which side will the coin land on? 'heads/tails")
                            choice = input()
                            heads = 1
                            tails = 2
                            coin = random.randint(1, 2)
                            if coin == heads:
                                print("It was heads!")
                                if choice == 'heads':
                                    moneyMade = int(wager) * 2 - int(wager)
                                    print("You doubled your money! You made,", moneyMade)
                                    self.currency += int(wager) * 2
                                    return
                                else:
                                    print("You lost all of your money!")
                                    self.currency -= int(wager)
                                    return
                            elif coin == tails:
                                print("It was tails!")
                                if choice == 'tails':
                                    moneyMade = int(wager) * 2 - int(wager)
                                    print("You doubled your money! You made,", moneyMade)
                                    self.currency += int(wager) * 2
                                    return
                                else:
                                    print("You lost all of your money!")
                                    self.currency -= int(wager)
                                    return
                        else:
                            print("Come back soon!")
                else:
                    print("You don't have enough money for that wager!")
            else:
                return 'error in casino'


# setting global variables and lists
t1 = Title_Screen()
myPet = None
leave = True
restart = False
isExiting = False
petTypes = ['dog', 'cat']
actions = ['examine', 'give food', 'give water', 'play', 'clean']
locations = ['streets', 'home', 'store', 'park', 'casino']


# Main entrance to game
def titleScreen():
    print("####################################")
    print("#######    Pet Simulator     #######")
    print("#######        Play          #######")
    print("#######        About         #######")
    print("#######        Leave         #######")
    print("####################################")
    action = input(">")
    global t1
    while action.lower() != 'play' and action.lower() != 'about' and action.lower() != 'leave':
        print("Unrecognized input. Please try again...")
        action = input(">")
    else:
        if action.lower() == 'play':
            return
        elif action.lower() == 'about':
            t1.aboutPage()
        elif action.lower() == 'leave':
            t1.leaveGame()


# Character Creation for pet
def characterCreation():
    global restart
    restart = False
    print("###############################\nHello! Welcome to Pet Simulator.\n###############################\n")
    print("This game is all text and input based.\n")
    time.sleep(1)
    print("First, lets create your pet!\n")
    time.sleep(1)
    print("\nWhat would you like to name your pet?")
    PetStats.name = input(">")
    petName = PetStats.name
    print(PetStats.name, "is a beautiful name!")
    time.sleep(1)
    print("\nWhat kind of pet do you want? You can choose from: ", petTypes[0:2])
    PetStats.breed = input(">")
    breed = PetStats.breed
    while PetStats.breed.lower() != 'dog' and PetStats.breed != 'cat' and PetStats.breed != 'dababy':
        print("Sorry that is unrecognizable. Please try again...")
        PetStats.breed = input(">")
    else:
        if PetStats.breed == 'dog' or 'cat' or 'dababy':
            print("\nA", PetStats.breed, "is a great choice!\n")
            time.sleep(1)
            print("Gook luck out there with", petName, "!\n")
            global myPet
            global thread1
            myPet = PetStats(petName, 0, breed, 100, 100, 100, 100, 500, locations[0], 0, 0)


# Interactivity of game, actions/choices here
def prompt():
    print("\n   What would you like to do?")
    print("#####    Pet              #####")
    print("#####    Travel           #####")
    print("#####    Examine Stats    #####")
    print("#####    options          #####")
    print("#####    Quit             #####")
    action = input(">")
    if action.lower() in ['exit', 'leave', 'quit']:
        myPet.leaveGame()
    elif action.lower() in ['pet', 'pet options', 'my pet']:
        myPet.petOptions()
    elif action.lower() in ['examine', 'look at', 'examine stats']:
        myPet.printStats()
    elif action.lower() in ['travel']:
        myPet.travel()
    elif action.lower() in ['help', 'options']:
        myPet.options()


def statsThread():
    timeStart = time.time()
    timeAge = time.time()
    while True:
        if timeStart - time.time() < -120:
            myPet.statDecrease()
            timeStart = time.time()
            myPet.status()

        if timeAge - time.time() < -600:
            myPet.age()
            timeAge = time.time()

        if isExiting:
            print("Thread is exiting...")
            sys.exit()
    else:
        return 'thread error'


statsThread = threading.Thread(target=statsThread)


# main game loop
def interactivity():
    print("Now that you have a pet...\n")
    while leave is True and restart is False:
        if prompt() is True:
            prompt()
    else:
        if restart is True:
            global myPet
            del myPet
            characterCreation()
            interactivity()
        else:
            exit()


# starts game loops
def Game():
    titleScreen()
    characterCreation()
    statsThread.start()
    interactivity()


Game()
