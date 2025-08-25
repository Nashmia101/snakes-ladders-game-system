from diceroll import roll_the_dice
winner=""
# Player 1 Name
p1_name = str("Red") #the name type is a string

# Player 1 Position
p1_position = 0

# Player 2 Name
p2_name = str("Blue")

# Player 2 Position
p2_position = 0

# Snake Head Positions
snake_heads = [25,44,65,76,99] #snake_heads, snake_tails, ladder_bases and ladder_tops are lists

# Snake Tail Positions
snake_tails = [6,23,34,28,56]

# Ladder Base Positions
ladder_bases = [8,26,38,47,66]

# Ladder Tops Positions
ladder_tops = [43,39,55,81,92]

while (p1_position < 100 or p2_position < 100): # if any position is greater than 100 than come out of the loop

    # Roll the dice for the first player
    diceroll = roll_the_dice()

    # Logic to move the 1st player
    p1_position = p1_position + diceroll
    if p1_position > 100: #checking if postion is greater than 100
        p1_position = p1_position - diceroll

    # Check if player 1 is either on a snake head or ladder Base
    if p1_position in snake_heads:
        sh= snake_heads.index(p1_position)
        st = snake_tails[sh]
        p1_position = st
        print("Player Red stepped on a snake and is now in position",p1_position)

    elif p1_position in ladder_bases:
        lb= ladder_bases.index(p1_position)
        lt = ladder_tops[lb]
        p1_position = lt
        print("Player Red climbed a ladder and is now in position",p1_position)
    else: 
        p1_position=p1_position
        print("Player Red is in position",p1_position)

    if (p1_position==100): #check if the first player has reached positon 100 and declare them as the winner
        winner=p1_name 
        break   

    # Roll the dice for the second player
    diceroll = roll_the_dice()

    # Logic to move the second player 
    p2_position = p2_position + diceroll
    if p2_position > 100: #checking if postion is greater than 100
        p2_position = p2_position - diceroll
    

    # Check if player 2 is either on a snake head or ladder Base
    if p2_position in snake_heads:
        sh2= snake_heads.index(p2_position)
        st2 = snake_tails[sh2]
        p2_position = st2
        print("Player Blue stepped on a snake and is now in position",p2_position)

    elif p2_position in ladder_bases:
        lb2= ladder_bases.index(p2_position)
        lt2 = ladder_tops[lb2]
        p2_position = lt2
        print("Player Blue climbed a ladder and is now in position",p2_position)
    else: 
        p2_position=p2_position
        print("Player Blue is in position",p2_position) 

    if(p2_position==100): #check if the second player has reached positon 100 and declare them as the winner
        winner=p2_name
        break
#display the winner's name
print("Player",winner,"has reached 100 and is the winner!")
