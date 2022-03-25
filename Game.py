#This program is a substructure square root  game
# Start with number of  coins, players to number his square root coins.
# The one who takes the last coin win     
# Authors: Mariam Haitham 
# Version: 1.0
# assigmnent 1 game 7 task 2


print ( " Rules of game \n start with coins that the user wants \n the first player will entre number of coins he want to remove and the number must have a square root \n tje seond player does that too \n the first to make the number of coins equal to zero is winner ")
print ("<<<<<<<<<<<<<<<<<<<<<< start game >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")


import math

def check_sqrt(player):
# this function check if a number has a square root,
    squar_root = int(math.sqrt(player))
    
    if squar_root == math.sqrt(player):
        return True
        
    else:
        return False


def players(user, coins):
    
    if user < 0:
    # this condition check if player1 or player2 input number less than zero
        print("Please enter positive number")
        user = get_player_input(coins)#get coins from any player in function get_player_input
        return user

    elif check_sqrt(user) == False:
        print("please enter a number that has a sqaure root")
        user = get_player_input(coins)
        return user

    if user > coins:
        # this condition check the player entred a number < coins or not
        print("this number is bigger than the number of coins, please try again")
        user = get_player_input(coins)
        return user

    elif type(user) != int:
        #this condition check the player enter string
        print("please enter numbers only")
        user = get_player_input(coins)
        return user


    elif check_sqrt(user) == True and user <= coins and coins > 0:
        # check a number has a sqrt
        return user


def get_coins():
    # function to get coins from user
    coins = input("please enter  number of coins ")
    
    while not coins.isdigit():#check if player input string
        coins = input("please enter a number only")
    coins = int(coins)
    
    while coins <= 0:
        # check if coins < zero
        print("please enter postive number of coins")
        coins = input()
        
        while not coins.isdigit():
            coins = input("please enter a number only")
        coins = int(coins)
    return coins


def get_player_input(coins):
    
    # function to get number from players
    # Here the player enters a part of the coins and it must have a square root and be less than the number of the base coins
    
    player = input()
    if not player.isdigit():
        print("please enter numbers only")
        return get_player_input(coins)
    player = int(player)
    
    while player > coins:
        print("this number is bigger than the number of coins, please try again")
        return get_player_input(coins)
    return player


def main():
    coins = get_coins()
    while True:

        print("player1 turn please choose a number that has a root")
        player1 = get_player_input(coins)
        player1 = players(player1, coins)
        coins -= player1  
        # The number of coins entred by player1 is subtaced from the number of base coins
        print("Reminder = ", coins)

        if coins == 0:
            # if the player1 makes the number of coins = 0, he is the winner
            print("player1 wins")
            print( " Congratulations")
            break

        print("player2 turn please choose a number that has a root")
        player2 = get_player_input(coins)
        player2 = players(player2, coins)
        coins -= player2  # The number of coins entred by player2 is subtaced from the number of base coins
        print("Reminder = ", coins)

        if coins == 0:
            # if the player2 makes the number of coins = 0, he is the winner
            print("player2 wins")
            print("Congratulations")
            break

main()
