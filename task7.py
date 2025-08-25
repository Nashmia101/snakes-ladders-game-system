from diceroll import roll_the_dice, special_roll
from helpers import generate_surprises

# initialise_game function contains the 'game' dictionary
def initialise_game() -> dict:
    return (
        {
        "players" : {
            "Red" : 0,
           "Blue" : 0,
          "Green" : 0,
          "White" : 0
        },
        "snakes"  : {
             "25" : 6,
              "44" : 23,
              "65" : 34,
               "76" : 28,
               "99" : 56
        },
        "ladders" : {
                "8" : 43,
               "26" : 39,
               "38" : 55,
               "47" : 81,
               "66" : 92
        }
         }
    )
# get_num_players function
def get_num_players() -> int:
    num_players = (int(input("Enter the number of players that would like to play: ")))# taking input from the user
    if (num_players <1 or num_players >4): #checking input validity
        print("Invalid input. Please enter again.")
        return get_num_players()
    return num_players

def update_players_dictionary(num_players: int, game: dict):# updating the players dictionary according to the number of players
    names = ["Red", "Blue", "Green", "White"]
    if num_players == 1:
    # Remove last 3 players (and positions)
        for name in names[-3:]:
            del game["players"][name]
    elif num_players == 2:
        # Remove last 2 players
        for name in names[-2:]:
            del game["players"][name]
    elif num_players == 3:
        # Remove last player
        for name in names[-1:]:
            del game["players"][name]
    return game
    
#  play game function     
def play_game(game: dict) -> str:
    # Adding surprise tiles list into the the special_tiles dictionary in the main game dictionary
    surprise_tiles = list(generate_surprises()) # calling generate_surprises function
    game["special_tiles"]=surprise_tiles
    # converting each dictionary into lists 
    player = list(game["players"].keys())
    positions = list(game["players"].values())
    snake_heads1 = list(game["snakes"].keys())
    snake_tails = list(game["snakes"].values())
    ladder_bases1 = list(game["ladders"].keys())
    ladder_tops = list(game["ladders"].values())
    snake_heads = []
    ladder_bases = []
    # converting snake heads list which has string values into int 
    for s in range(len(snake_heads1)):
        num=int(snake_heads1[s])
        snake_heads.append(num)
   
    # converting ladder bases list which has string values into int
    for b in range(len(ladder_bases1)):
        l=int(ladder_bases1[b])
        ladder_bases.append(l)
    

    i = 0
# this is where the main game is being played      
    while positions[i] < 100:  # loop ends if any position crosses 100 (loop condition)
        diceroll = roll_the_dice()  # calling the dice_roll function
        print("The result of dice roll is:",diceroll)
        positions[i] = positions[i] + diceroll 
        if positions[i] > 100:  # checking if position has exceeded 100 
            positions[i] = positions[i] - diceroll
    
        if positions[i] in snake_heads: # checking if the current player has stepped on snake head
            sh = snake_heads.index(positions[i])
            st = snake_tails[sh]
            positions[i] = st
            print("Player", player[i], "stepped on a snake and is now in position", positions[i])
        elif positions[i] in ladder_bases:  # checking if the current player has stepped on ladder base
            lb = ladder_bases.index(positions[i])
            lt =ladder_tops[lb]
            positions[i] = lt
            print("Player", player[i], "climbed a ladder and is now in position", positions[i])
        else:
            positions[i] = positions[i]
            print("Player", player[i], "is in position", positions[i])
            
        if positions[i] in surprise_tiles:  # checking if the current player has stepped on special title
            special_dice = special_roll()
            print("The result of special roll dice is:",special_dice)
            if special_dice==0: # if the special dice is 0 the current player gets an another turn
                print("Player",player[i],"has stepped on the special tile. Hence you get to role the dice again")
                continue
            elif special_dice==1: # if the special dice is 1 then the player after the current player loses a turn
                print("Player",player[i],"has stepped on the special tile. Hence the player next to you loses turn ")
                i=((i+2)%len(player))
                print("Hence it is now player",player[i],"turn")
                continue
            elif special_dice==2: #if the special dice is 2 then all the players except the current player move 5 spaces back
                print("Player",player[i],"has stepped on the special title Hence now all the other players move back 5 spaces")
                for j in range(len(player)):
                    if j != i:
                        positions[j]=positions[j]-5
                        if positions[j]<0: # if a player goes back to position below 0 then it's position should change to 0
                            positions[j]=0
                    print("Now player",player[j],"is in position",positions[j])      
                    
        if (positions[i] == 100): # checking for winner by checking if any position has reached 100
            winner = player[i]
            c = 0
            for n in player:
                game["players"][n]= positions[c] #updating final positions in the dictionary players
                c += 1
            break

        i=i+1 #incrementing to the next player position
        if i == len(player): # maintaining index
            i =0

    return winner

# pick winner function
def pick_winner(players: dict) -> str: 
    for player, position in players.items(): #checking if any position is 100 if yes then return the specific player name for that position
        if position == 100:
            return player
    return None  # if there is no winner then it returns None

# turn_by_turn_gameplay function    
# turn by turn function is playing a two player game between player Red and player Blue 
def turn_by_turn_gameplay(game: dict) -> str: 
    game["players"].clear() # clearing out the players dictionary in main dictionary game
    game["players"]["Red"]=0 # adding player Red and its position into the dictionary
    game["players"]["Blue"]=0 # adding player Blue and its position into the dictionary
    surprise_tiles = list(generate_surprises()) # calling generate_surprises function
    game["special_tiles"]=surprise_tiles # # Adding surprise tiles list into the new special_tiles dictionary in the main game dictionary
    # converting each dictionary's keys and values into lists 
    player = list(game["players"].keys())
    positions = list(game["players"].values())
    snake_heads1 = list(game["snakes"].keys())
    snake_tails = list(game["snakes"].values())
    ladder_bases1 = list(game["ladders"].keys())
    ladder_tops = list(game["ladders"].values())
    snake_heads = []
    ladder_bases = []
    # converting snake heads list which has string values into int 
    for s in range(len(snake_heads1)):
        num=int(snake_heads1[s])
        snake_heads.append(num)
    # converting ladder bases list which has string values into int 
    for b in range(len(ladder_bases1)):
        l=int(ladder_bases1[b])
        ladder_bases.append(l)
    
    i = 0
    answer1="" # intializing answer1 with empty string 
    turn_winner="" # intializing turn_winner with empty string
    print("-------------------------TURN BY TURN GAME PLAY------------------------------------")

    while positions[i] < 100: # loop ends if any position crosses 100 (loop condition)
       print("-------------------------------------------------------------------------------") 
       print("Player",player[i],"'s turn") # current player's turn 
       answer1 = input("Do you want to roll the dice or quit the game? If you want to play, enter 'roll'. Otherwise, enter 'quit': ") # taking user input
       if (answer1 != "roll" and answer1 != "quit"): # checking input validity
          print("Invalid input")
          continue # if invalid input then it asks user for input again 
       print("Player",player[i],"wants to",answer1,"the game") 

       # if user wants to play the game
       if (answer1=="roll"): 
            diceroll = roll_the_dice() # calling the dice_roll function
            print("The result of dice roll is:",diceroll)
            positions[i]=positions[i]+diceroll
            if positions[i]>100: # checking if position has exceeded 100 
                positions[i]=positions[i]-diceroll    
        
            if positions[i] in snake_heads: # checking if the current player has stepped on snake head
                sh = snake_heads.index(positions[i])
                st = snake_tails[sh]
                positions[i] = st
                print("Player", player[i], "stepped on a snake and is now in position", positions[i])
            elif positions[i] in ladder_bases: # checking if the current player has stepped on ladder bases
                lb = ladder_bases.index(positions[i])
                lt =ladder_tops[lb]
                positions[i] = lt
                print("Player", player[i], "climbed a ladder and is now in position", positions[i])
            else:
                positions[i] = positions[i]
                print("Player", player[i], "is in position", positions[i])
                
            # checking if the current player has stepped on special title     
            if positions[i] in surprise_tiles:
                special_dice= special_roll()
                print("The result of special roll dice is:",special_dice)
                if special_dice==0:  # if the special dice is 0 the current player gets an another turn
                    print("Player",player[i],"has stepped on the special tile. Hence you get to role the dice again")
                    continue
                elif special_dice==1: # if the special dice is 1 then the player after the current player loses a turn
                    print("Player",player[i],"has stepped on the special tile. Hence the player next to you loses turn ")
                    i=((i+2)%len(player))
                    print("Hence it is now player",player[i],"turn")
                    continue
                elif special_dice==2: #if the special dice is 2 then all the players other than the current player move 5 spaces back
                    print("Player",player[i],"has stepped on the special title Hence now all the other players move back 5 spaces")
                    for j in range(len(player)):
                        if j != i:
                            positions[j]=positions[j]-5
                            if positions[j]<0:  # if a player goes back to position below 0 then it's position should change to 0
                                positions[j]=0
                        print("Now player",player[j],"is in position",positions[j])      
                        
            if (positions[i] == 100): # checking for winner by checking if any position has reached 100
                turn_winner = player[i]
                c = 0
                for n in player:
                    game["players"][n]= positions[c]  #updating final positions in the dictionary players
                    c += 1
                break
    
            i=i+1 #incrementing to the next player position
            if i == len(player): # maintaining index
                i =0
       elif(answer1=="quit"): # checking if user wants to quit the game
           break    

    return turn_winner

def main():
    game = initialise_game() # calling initalise game function and storing into game
    num_players = get_num_players() # calling get_num_players function and storing the number of players in num_players
    game=update_players_dictionary(num_players,game) # calling update_players_dictionary function in order to update the dictionary 
    winner = play_game(game)# calling play_game function to play the main game
    print(f"The winner is {winner}!") # printing winner name
    # for turn_by_turn game
    turn_winner =turn_by_turn_gameplay(game) # calling turn_by_turn_gameplay function to play the turn_by_turn 2 player game
    check = pick_winner(game["players"]) # calling pick_winner function to get the name of the winner
    if (check==None): # if there is no winner then it displays game ended
        print("Game Ended")
    else:
        print(f"The winner is {check}!") # if there is a winner it displays the name of the winner

if __name__ == '__main__':
    main() # calling main function
