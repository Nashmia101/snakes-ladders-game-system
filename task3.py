from diceroll import roll_the_dice
# Player 1 Name
p1_name = str("Red") #the name type is a string

# Player 1 Position
p1_position = 0

# Player 2 Name
p2_name = str("Blue")

# Player 2 Position
p2_position = 0

# Snake Head Positions
snake_heads = [32,48,56,63,97] #snake_heads, snake_tails, ladder_bases and ladder_tops are lists

# Snake Tail Positions
snake_tails = [10,26,38,18,78]

# Ladder Base Positions
ladder_bases = [1,28,50,71,80]

# Ladder Tops Positions
ladder_tops = [44,76,67,92,99]

# Roll the dice for the first player
diceroll = roll_the_dice()

# Logic to move the 1st player
p1_position = p1_position + diceroll
if p1_position > 100:
    p1_position = p1_position - diceroll

# Roll the dice for the second player
diceroll = roll_the_dice()

# Logic to move the 2nd player
p2_position = p2_position + diceroll
if p2_position > 100:
    p2_position = p2_position - diceroll

# Check if player 1 is either on a snake head or ladder Base and update position
if p1_position in snake_heads:
    sh= snake_heads.index(p1_position)
    st = snake_tails[sh]
    p1_position = st
else: 
    p1_position=p1_position 

if p1_position in ladder_bases:
    lb= ladder_bases.index(p1_position)
    lt = ladder_tops[lb]
    p1_position = lt
else: 
    p1_position=p1_position      

# Check if player 2 is either on a snake head or ladder Base and update position
if p2_position in snake_heads:
    sh2= snake_heads.index(p2_position)
    st2 = snake_tails[sh2]
    p2_position = st2
    print(p2_position)
else: 
    p2_position=p2_position 

if p2_position in ladder_bases:
    lb2= ladder_bases.index(p2_position)
    lt2 = ladder_tops[lb2]
    p2_position = lt2
else: 
    p2_position=p2_position      

# Print the position of player 1
print("Player",p1_name,"is in position",p1_position)
# Print the position of player 2
print("Player",p2_name,"is in position",p2_position)
