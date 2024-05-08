# Importing modules
import random
import time
from prettytable import PrettyTable

# Creating a function to roll the dice
def roll_dice():
    dice=random.randint(1, 6)
    if dice==6:
        num_moves=3
    elif dice==4:
        num_moves=2
    elif dice==5:
        num_moves = 2
    elif dice==3:
        num_moves=3
    elif dice==2:
        num_moves=2
    else:
        num_moves = 0
    return (dice, num_moves)

# Creating Variables
player_pos=[]
computer_pos=[]
player_moves_number=[]
computer_moves_number=[]
col_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
player_moves=0
computer_moves=0
player_black=0
computer_black=0

# Starting the game
while True:
    # Input of player
    input("Press Enter to roll the dice")
    dice, num_moves=roll_dice()
    # Checking if the dice rolls 6
    if dice==6:
        print("Human dice roll is",dice,"can start the game")
        playerdice=dice
        time.sleep(1)
        break
    else:
        print("Human dice roll is",dice,"cannot start the game")
        time.sleep(1)
    dice, num_moves=roll_dice()
    if dice==6:
        print("Computer dice roll is",dice,"can start the game")
        time.sleep(1)
        break
    else:
        print("Computer dice roll is",dice,"cannot start the game")
        time.sleep(1)
        continue
print("\n\n")

# Main gameplay
while True:
    # Creating board using PrettyTable
    table=PrettyTable()
    table.field_names=col_list # Adding fields
    if True:
        input("Press Enter to roll the dice")
        dice, num_moves=roll_dice()
        time.sleep(1)
    player_moves+=num_moves
    player_column=1 # A variable to match the player row index
    player_row=" "
    print("You rolled a",dice,"can move",num_moves)
    # Player gameplay loop
    while player_column<=20:
        if player_moves==player_column:
            player_row="X"
        if player_column==7 or player_column==14:
            player_row="O"
        if player_moves==7 or player_moves==14:
            time.sleep(1)
            print("\nYou hit the black hole")
            player_moves=1
            player_row="X"
            player_black+=1
        player_pos.append(player_row)
        player_row=" "
        player_column+=1
    # Appending number of player moves to a list
    player_moves_number.append(player_moves)
    table.add_row(player_pos)

    # Computer gameplay
    print("\n\nComputer rolling the dice now")
    time.sleep(1)
    dice, num_moves=roll_dice()
    computer_moves+=num_moves
    computer_column=1
    computer_row=" "
    print("Computer rolled a",dice,"can move",num_moves)
    # Computer gameplay loop
    while computer_column<=20:
        if computer_moves==computer_column:
            computer_row="X"
        if computer_column==7 or computer_column==14:
            computer_row="O"
        if computer_moves==7 or computer_moves==14:
            print("\nComputer hit the black hole")
            computer_moves=1
            computer_row="X"
            computer_black+=1
        computer_pos.append(computer_row)
        computer_row=" "
        computer_column+=1
    # Appending number of computer moves to a list
    computer_moves_number.append(computer_moves)
    table.add_row(computer_pos)
    time.sleep(1)
    print (table) 
    time.sleep(1)
    if player_moves>=20:
        print("\nCongratulations you win the game!")
        break
    if computer_moves>=20:
        print("\nComputer won the game!, You lost")
        break

    # Resetting the row list for the loop to continue
    player_pos=[]
    computer_pos=[]

# Saving the game to a text file
save=time.strftime("%Y_%m_%d_%H_%M") + ".txt"
with open(save, "w") as game_save:
    game_save.write("Human\n")
    game_save.write(f"Total number of moves {len(player_moves_number)}\n")
    game_save.write(f"Black hole hits {player_black}\n")
    if player_moves>=20:
        game_save.write("Won the game\n\n")
    else:
        game_save.write("Lost the game\n\n")
    game_save.write("Computer\n")
    game_save.write(f"Total number of moves {len(computer_moves_number)}\n")
    game_save.write(f"Black hole hits {computer_black}\n")
    if computer_moves>=20:
        game_save.write("Won the game\n\n")
    else:
        game_save.write("Lost the game\n\n")