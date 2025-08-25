from diceroll import roll_the_dice
# Snake Head Positions
snake_heads = [25, 44, 65, 76, 99]
# Snake Tail Positions
snake_tails = [6, 23, 34, 28, 56]
# Ladder Base Positions
ladder_bases = [8, 26, 38, 47, 66]
# Ladder Tops Positions
ladder_tops = [43, 39, 55, 81, 92]
# Positions of all players
positions = [0, 0, 0, 0]
# Names of all players
players = ["Red","Blue","Green","White"]
# defining the winner variable with an empty string
winner = ""

# Making sure the number of players is between 1 and 4 inclusive
num_players = 0
while num_players < 1 or num_players > 4:
    num_players = int(input("Enter the number of players that would like to play: "))
    if num_players < 1 or num_players > 4:
        print("Invalid input. Please enter a number between 1 and 4.")

# updating the player and positions lists based on the number of players
if num_players == 1: # if one player is playing the game, delete the names of the last 3 players and their positions
    del players[1:4]
    del positions[1:4]
elif num_players == 2: # if 2 players are playing the game, delete the names of the last 2 players and their positions
    del players[2:4]
    del positions[2:4]
elif num_players == 3: # if 3 players are playing the game, delete the name of the last player and their position  
    del players[3]
    del positions[3]
elif num_players>=4: #if 4 players are playing, do not change the lists
    players= players
    positions=positions   

i=0
while positions[i] < 100:  # loop ends if any position crosses 100 (loop condition)
    diceroll = roll_the_dice()  # calling roll_the_dice function
    positions[i] = positions[i] + diceroll
    if positions[i] > 100: # checking if position has exceeded 100 
        positions[i] = positions[i] - diceroll

    if positions[i] in snake_heads: # checking if the current player has stepped on snake head
        sh = snake_heads.index(positions[i])
        st = snake_tails[sh]
        positions[i] = st
        print("Player", players[i], "stepped on a snake and is now in position", positions[i])
    elif positions[i] in ladder_bases: # checking if the current player has stepped on ladder base
        lb = ladder_bases.index(positions[i])
        lt = ladder_tops[lb]
        positions[i] = lt
        print("Player", players[i], "climbed a ladder and is now in position", positions[i])
    else:
        positions[i] = positions[i]
        print("Player", players[i], "is in position", positions[i])

    if (positions[i] == 100): # checking for winner by checking if any position has reached 100
        winner = players[i]
        break
    i=i+1  #incrementing to the next player position
    if i == len(players): # maintaining index
        i=0
print("Player", winner, "has reached 100 and is the winner")  # printing the name of the winner
