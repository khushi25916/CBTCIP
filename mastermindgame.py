#stores the no. of turns a player takes to complete the game
count1 = 0 
count2 = 0

#player 1 set no. to guess by player 2
player_1 = int(input("enter the no. that needs to be guessed by the player_2: "))

#player 2 turn 
while True:
    player_2 = int(input("guess the no.set by player 1: "))
    #the no. of turns player2 take to guess the no.
    count1 += 1
    
    if player_2 < player_1:
        print("Oops! Too low. Try a higher number.") 
    elif (player_2 > player_1):
        print("Oops! Too high. Try a lower number.")
    else:
        print("you won!")
        break

#player 2 set no. to guess by player 1
print("now its player 2 turn to set the no. to guess for player 1")
player_2 = int(input("enter the no. that needs to be guessed by player 1: "))

#player 1 turn
while True:
    player_1 = int(input("guess the no.set by player 2: "))
    #the no. of turns player1 take to guess the no.
    count2+=1 
    if (player_2 < player_1):
        print("Oops! Too low. Try a higher number.")
    elif (player_2 > player_1):
         print("Oops! Too high. Try a lower number.")  
    else:
        print("you won!")
        break

#display the results
print("the master mind of the game is:")

#results based on the comparison between no. of turns taken by each player
if count1>count2:
    print("player 1 is mastermind!!")
else:
    print("player 2 is the mastermind!")
