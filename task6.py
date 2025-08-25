from diceroll import roll_the_dice
from typing import Tuple, List

# Define the game tuple
def initialise_game() -> Tuple[List[str], List[int], List[int], List[int], List[int], List[int]]:
    return (
    ["Red", "Blue", "Green", "White"],  # Players
    [0, 0, 0, 0],            # Positions
    [25, 44, 65, 76, 99],    # Snake heads
    [6, 23, 34, 28, 56],     # Snake tails
    [8, 26, 38, 47, 66],     # Ladder bases
    [43, 39, 55, 81, 92]     # Ladder tops
    )

# get_num_players function
def get_num_players() -> int:
    num_players = (int(input("Enter the number of players that would like to play: "))) # taking input from the user
    if (num_players < 1 or num_players > 4): #checking input validity
        print("Invalid input. Please enter again.")
        return get_num_players()
    return num_players

# updating the players and positions list according to the number of players
def update_players_positions_list(num_players: int, players: List[str], positions: List[int]) -> Tuple[List[str], List[int]]:
    if num_players == 1:
        players = players[:-3]  # Remove last 3 players
        positions = positions[:-3]  # Remove last 3 positions
    elif num_players == 2:
        players = players[:-2]  # Remove last 2 players
        positions = positions[:-2]  # Remove last 2 positions
    elif num_players == 3:
        players = players[:-1]  # Remove last player
        positions = positions[:-1]  # Remove last position
    elif num_players>=4:
        players= players
        positions=positions    

    return players, positions   
 
#  play game function  
# this is where the main game is being played
def play_game(players,positions,snake_heads,snake_tails,ladder_bases,ladder_tops)-> list:
    i = 0
    while positions[i] < 100: # loop ends if any position crosses 100 (loop condition)
        diceroll = roll_the_dice() # calling diceroll function
        positions[i] = positions[i] + diceroll 
        if positions[i] > 100:  # checking if position has exceeded 100 
            positions[i] = positions[i] - diceroll
    
        if positions[i] in snake_heads: # checking if the current player has stepped on snake head
            sh = snake_heads.index(positions[i])
            st = snake_tails[sh]
            positions[i] = st
            print("Player", players[i], "stepped on a snake and is now in position", positions[i])
        elif positions[i] in ladder_bases:  # checking if the current player has stepped on ladder base
            lb = ladder_bases.index(positions[i])
            lt =ladder_tops[lb]
            positions[i] = lt
            print("Player", players[i], "climbed a ladder and is now in position", positions[i])
        else:
            positions[i] = positions[i]
            print("Player", players[i], "is in position", positions[i])

        if (positions[i] == 100): # checking for winner by checking if any position has reached 100
            break
        i=i+1 #incrementing to the next player position
        if i == len(players): # maintaining index
            i =0

    return positions # returning final positions

def pick_winner(final_positions):
    for i in range(len(final_positions)): #checking if any position is 100 if yes then return the specific player name for that position
        if final_positions[i] == 100:
            return i  # Return the index of the winner 
    return -1 # if there is no winner then it returns -1
                   
    

def main():
    players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops = initialise_game() # calling initalise game function
    num_players = get_num_players() # calling get_num_players function and storing the number of players in num_players
    players, positions = update_players_positions_list(num_players, players, positions) # calling update_players_positions_list function in order to update the lists of players and positions inside the tuple
    final_positions = play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops) # calling play_game function to play the main game
    winner = pick_winner(final_positions)  # calling pick_winner function to get the name of the winner
    if winner==-1: # if winner is equal to -1 then that means there is no winner so it should print -1
        print(-1)
    else:
        print(f"The winner is {players[winner]}!") # if there is a winner it should print the name of the winner
    
    
if __name__ == "__main__":
    main() # calling main function
