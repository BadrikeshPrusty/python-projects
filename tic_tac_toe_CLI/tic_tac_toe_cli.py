'''
Name            : Badrikesh Prusty
Organisation    : Emertxe Information Technologies (P) Ltd.
Date            : 15/06/2020
Description     : Python code to create a game Tic Tac Toe for two players.
Input           : Enter player names, the a player is randomly asked to select his/her marker, then position to enter the marker.
Output          :
                -------------------------------------------------------------------------------------------------------------------
                Welcome to the World of Tic Tac Toe
                -------------------------------------------------------------------------------------------------------------------
                Game Window in terminal to play the game

'''

#Function to display the board
def display_board(board):
    
    for i in range(1, 10):                  #as first char '#' is unused range start from 1 to iterate
        print(board[i]+'\t', end = " ")
        
        if i % 3 == 0:                      #newline after every printing every 3 values to make 3 x 3 table
            print("\n")


#Function to take player input
def player_input():                         #to take the input from the player player input function is called everytime
    while True:                             #inf loop
        try:            #to check if input is correct (integers) if wrong input other than integers entered it will go to except block
            position = int(input("Enter the position to which you want to insert your marker: "))

        except ValueError:                  #to throw user created error
            print("\nError: You have entered invalid position. Please use integer values only\n")
            print("------------------------------------------------------------------------------------------------------------------------")
            continue                        #continue to continue the loop from same spot ans ask for position again
        
        if position > 0 and position < 10:  #if position lies in the given range go to this block

            if space_check(board, position):        #check if the entered position is empty or not. if empty it the function return true
                place_marker(board, marker, position)   #place the marker at particular board position
                break   #break the loop

            else:
                print("\nError: The entered position on the board is already filled. Please check the board and enter position carefully\n")
                print("------------------------------------------------------------------------------------------------------------------------")

        else:
            print("\nError: Position entered is out of range. Please enter the position from 1 to 9 only\n")
            print("------------------------------------------------------------------------------------------------------------------------")

    #end of function definition


#Function to place the marker at the given position on the board
def place_marker(board, marker, position):
    board[position] = marker                #add the marker at user input position on the board


#Checking if the either player 1 or player 2 won after entering 5 positions

def win_check(board, mark):                 #function definition for checking who won the game
    for i in [1, 2, 3, 4, 7]:               #iterating through all the posible positions a player can win from 
        if board[i] != mark:
            continue                        #if marker not foundin that location continue to check the next location
        
        count = 0                           #count variable to keep track of the matches to check if user has won or not
        
        #Column elements scan for each row
        if i == 1 or i == 4 or i == 7:          #user can win only in these 3 conditions on a horizontal check
            for j in [1, 2]:                    #for adding to the first position to the first found condition check marker matches or not
                if board[i] == board[i+j]:
                    count += 1                  #if matches increase the count
                
                else:
                    count = 0                   #turn the count back to 0 to check the next step
                    break                       #if fails break the second loop
            
            if count == 2:
                return True                     #if count is 2 then that particular user won the game

        #row elements scan for each column
        if i == 1 or i == 2 or i == 3:          #vertical elements check only 3 possible conditions
            for j in [3, 6]:
                if board[i] == board[i+j]:      #adding 3 and 6 to 1 will check 4th and 7th to check if the user has won or not
                    count += 1
                
                else:
                    count = 0
                    break
            
            if count == 2:
                return True
        

        #diagonal element scan
        if i == 1:                              #diagonal element check can only start from cornors 1, 3, 7, 9
            for j in [4, 8]:                    #if fount in 1 then it will check 5th and 9th position
                if board[i] == board[i+j]:
                    count += 1
                
                else:
                    break                       #if condition doesn't immidiately break the statement
                
                if count == 2:
                    return True
        
        if i == 3:
            for j in [2, 4]:                    #check for 5th and 7th position
                if board[i] == board[i+j]:
                    count += 1
                
                else:
                    break
                
                if count == 2:
                    return True

    return False                                #if none of the scan is successful return false for no wins


#Function to randomly select a player to who will play first and able to select his/her marker 
from random import randint

def choose_first():
    return randint(1, 2)                        #randint function will random select in the given range of number. here it's just
                                                #1, 2 so it switches randomly between 1 and 2 when the function is called

#Function to check the space if the space is empty or not
def space_check(board, position):
    if board[position] == '_':                  #if the entered position is empty or '_' return true 
        return True
    return False                                #if not empty return false


#Checking if the board is full or not
def full_board_check(board):
    for i in range(1, 10):                      #checks for any empty or '_' characters to see if the board is not full
        if board[i] == '_':
            return False
    return True                                 #if '_' not found return true that board is not empty


#Function to check if users want to replay or not
def replay():
    print("\n------------------------------------------------------------------------------------------------------------------------")
    repeat = input("\nDo you want to play another game ? (Yy/Nn): ")

    if repeat == 'Y' or repeat == 'y':          #if the user enters Y or y run the game
        return True

    return False                                #false to quit the game





#Run the Game

from os import system                           #importing system function from os module
system('clear')                                   #to clear the terminal screen

print("------------------------------------------------------------------------------------------------------------------------")
print("Welcome to the World of Tic Tac Toe!")
print("------------------------------------------------------------------------------------------------------------------------\n")

from time import sleep                          #importing time to use sleep command

while True:
    while True:
        player1 = input("Enter Player 1 Name: ")                #input player name
        
        if len(player1):                        #if name not entered then the length the string is condition fails so it will
            break                               #if name has some length break the loop                       #rerun the loop
        print("\nPlease enter your name to continue\n")
    
    while True:
        player2 = input("\nEnter Player 2 Name: ")
        
        if len(player2):
            break
        print("\nPlease enter your name to continue\n")

    print("\n------------------------------------------------------------------------------------------------------------------------")
                                                                                    #line separator
    if choose_first() == 1:     #choose first function to randomly select which player will go first in this case player 1
        flag = 1                #declaring flag variable to keep track of a particluar player
        
        while True:
            print("Two markers available 'O' or 'X'. Select any one of the two:\n")     #user can only select these two markers
            
            player_1_marker = input(player1+" select a marker: ")
     
            if player_1_marker == 'O':                      #if player 1 selects O then assign X to player 2
                player_2_marker = 'X'
                break                                       #and break the loop
            
            elif player_1_marker == 'X':                    #or vice-versa
                player_2_marker = 'O'
                break
        
            else:
                print("\nInvalid option selected. Please select an appropriate marker\n\n")
                print("------------------------------------------------------------------------------------------------------------------------\n")

    else:                   #if the condition of if block fails it will go to this block
        flag = 2            #flag 2 for player 2

        while True:
            print("Two markers available 'O' or 'X'. Select any one of the two:\n")

            player_2_marker = input(player2+" select a marker: ")
        
            if player_2_marker == 'O':
                player_1_marker = 'X'
                break
        
            elif player_2_marker == 'X':
                player_1_marker = 'O'
                break
        
            else:
                print("\nInvalid option selected. Please select the appropriate option\n\n")
                print("------------------------------------------------------------------------------------------------------------------------\n")
    
    
    
    system('clear')                     #clear the terminal screen

    print('\n'+player1+"'s marker:", player_1_marker, end = '\t\t')
    print(player2+"'s marker:", player_2_marker)                    #display both players markers

    print("\n"+player1+" and "+player2+" please remember your markers")

    print("\n------------------------------------------------------------------------------------------------------------------------\n")

    print("Starting the game in few seconds....")
    sleep(3)

    system('clear')
    
    print("\nInitial Board Layout:\n")
    board = ['#', '_', '_', '_', '_', '_', '_', '_', '_', '_']      #adding empty characters as '_' in box and we want to use position from 1
    display_board(board)                                            #function to display the board

    print('\n'+player1+"'s marker:", player_1_marker, end = '\t\t')
    print(player2+"'s marker:", player_2_marker)                    #display player markers

    count = 0                               #count to keep track of how many markers added

    while True:

        count += 1                          #increase the count everytime the loop runs to check how many positions added

        if flag == 1:                       #here using the flag to alternately give chances to the players to give the input
            print("------------------------------------------------------------------------------------------------------------------------")
            print(player1+"'s turn")
            marker = player_1_marker        #setting to marker to player 1 marker
            print("Your marker: "+marker)
            print("------------------------------------------------------------------------------------------------------------------------")
            player_input()                  #calling the input function to input the marker for the particular position
            flag = 2                        #turning the flag to 2 so that next time user 2 can enter

        elif flag == 2:
            print("------------------------------------------------------------------------------------------------------------------------")
            print(player2+"'s turn")
            marker = player_2_marker
            print("Your marker: "+marker)
            print("------------------------------------------------------------------------------------------------------------------------")
            player_input()
            flag = 1
        
        system('clear')                     #clear the screen
        
        print("\nBoard Layout:\n")
        display_board(board)                #display the updated board
        
        print('\n'+player1+"'s marker:", player_1_marker, end = '\t\t')
        print(player2+"'s marker:", player_2_marker)        #display the marker

        if count >= 5:                      #go to this block only if 5 positions on the board has been add as it is the least number of positions
            if win_check(board, marker):    #function call to check who won passing board and marker         #two player playing this game can win
                print("------------------------------------------------------------------------------------------------------------------------\n")
                if flag == 1:               #the flag is reversed here because when taking flag condition previously at the time of player input
                    print(player2+" won the game :)")   #winning message player 2             #we are updating the flag for other person to play
                    print('\n'+player1+" :( better luck next time!!")
                
                else:
                    print(player1+" won the game :)")
                    print('\n'+player2+" :( better luck next time!!")
                
                break

            if full_board_check(board):         #if the board is full it will return True so match is draw
                print("------------------------------------------------------------------------------------------------------------------------\n")
                print("Match draw!!!")  
                print("\nBetter luck next time!!")
                break                           #break the current while loop 

    if replay():                #if replay returns True re run the game
        system('clear')
        print("------------------------------------------------------------------------------------------------------------------------")
        print("Starting Another Game.....")
        print("------------------------------------------------------------------------------------------------------------------------\n")
        sleep(2)                                #wait for 2 seconds between matches

    else:
        print("\n------------------------------------------------------------------------------------------------------------------------\n")
        print("\nPlease feel free to play this game anytime you want.\n\nBye :)\n")
        print("\nExiting the Game......")
        sleep(3)
        system('clear')
        break       #if users doesn't want to replay exit the game
