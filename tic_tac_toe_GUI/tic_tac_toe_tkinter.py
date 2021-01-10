'''
Author Name     : Badrikesh Prusty
Organisation    : Emertxe Information Technologies (P) Ltd.
Date            : 21/06/2020
Description     : Python program to create a Graphical User Interface of Tic Tac Toe game using Tkinter Module
Input           : Run the program using: python3 tic_tac_toe_tkinter.py
                  Then add your marker to a specific position using mouse pointer
Output          : The game window opens to play the game the game finished we a successful condition for tic_tac_toe is reached. 
                  The game can be replayed using play again button. 
                  There's also a start over button that allows to restart the game at anytime the user wants.

'''

from tkinter import *                   #from tkinter module import everything
from tkinter import font                #importing font to change the font and font settings
from random import choice               #importing random to select the start marker randomly

window = Tk()                           #First step is to create a GUI window. Here in window in object we can apply many methods
window.title("Tic_Tac_Toe")             #window title
window.geometry("338x450")              #to set the default resolution that game will run when executed
window.resizable(0, 0)                  #to stop capability of resizing the window

bold_32 = font.Font(family = 'Courier 10 Pitch', size = 33, weight = 'bold')        #defining 3 fonts with its preferences
bold_18 = font.Font(family = 'Courier 10 Pitch', size = 18, weight = 'bold')        #family for font name, size for font size
bold_12 = font.Font(family = 'Courier 10 Pitch', size = 12, weight = 'bold')

def win_check(buttons, curr_marker):            #function definition to check the board and return True if a player wins
    
    for i in [1, 2, 3, 4, 7]:                   #iterating through all the possible staring  positions a player can win from
        if buttons[i]['text'] != curr_marker:
            continue                            #if currently entered marker doesn't match with button skip running entire loop
                                                                                        #and continue to check with next i value
        count = 0                               #count variable to keep track of count of matching condition

        #column element scan for each row
        if i == 1 or i == 4 or i == 7:          #all the starting position of rows a user can win from
            for j in [1, 2]:                    #adding 1 and 2 to check next 2 element to check if user wins or not
                if buttons[i]['text'] == buttons[i+j]['text']:                  #to check if markers are same or not
                    count += 1                                                  #increase the count if match occurs              

                else:
                    count = 0                   #if any of the match fails turn back the counter to 0 and break the current loop
                    break

                if count == 2:
                    buttons[i].config(bg = "light green")               #if user wins turn the buttons to green color indicating
                    buttons[i+1].config(bg = "light green")             #that user won game completed
                    buttons[i+2].config(bg = "light green")
                    return True                                         #returning True so it stops executing the current loop at this
                                                                        #and move the control to main program
        #row elements scan for each column
        if i == 1 or i == 2 or i == 3:
            for j in [3, 6]:                                            #checking if column elements are same next column element in same
                if buttons[i]['text'] == buttons[i+j]['text']:          #row is checked by adding 3 and 6. if 1 then 4 and  7th position
                    count += 1

                else:
                    count = 0
                    break

                if count == 2:
                    buttons[i].config(bg = "light green")
                    buttons[i+3].config(bg = "light green")
                    buttons[i+6].config(bg = "light green")
                    return True

        #diagonal element scan
        if i == 1:                                                      #diagonal element scan for to check 1 5 and 9th position
            for j in [4, 8]:
                if buttons[i]['text'] == buttons[i+j]['text']:          #checking if the buttons text are equal or not
                    count += 1

                else:
                    break

                if count == 2:
                    buttons[i].config(bg = "light green")
                    buttons[i+4].config(bg = "light green")
                    buttons[i+8].config(bg = "light green")
                    return True

        if i == 3:                                                      #to check 3 5 and 7th position 
            for j in [2, 4]:
                if buttons[i]['text'] == buttons[i+j]['text']:
                    count += 1

                else:
                    break

                if count == 2:
                    buttons[i].config(bg = "light green")
                    buttons[i+2].config(bg = "light green")
                    buttons[i+4].config(bg = "light green")
                    return True

    return False                                                         #return false if none of the condition satisfies


def label(str_pass, color):             #to create a label with the passed string text and color for text
    #global status_label
    status_label = Label(window, text = str_pass, fg = color, font = bold_18) #fg for foreground color of the text, adding to the window
    status_label.place(x = 23, y = 375) #placing the text at specific position of the current window

    #status_label.destroy()



marker = " "+choice("OX")+" "           #setting starting marker as random to select between O and X

total_added = 0                         #to check how many boxes marker has been added

flag = 0                                #flag for start over and play again button state

def btn_cmd(n):                         #value of button number is passed when clicked
    global flag
    global marker                       #declaring previous defined variables as global so that its value can be accessed
    global total_added                                                                              #all over the program
    
    flag = 0                            #flag is set to 0 if no one won and whenever the button is clicked

    if  marker == " X ":                #checking if current marker is X and a button is clicked
        buttons[n].config(text = marker, disabledforeground = "black", bg = "light grey", state = "disable")
        curr_marker = " X "             #add the text, disabledfg is marker color when button is disabled and disabling
        marker = " O "                  #curr_marker to keep track of marker applied                       #that button
                                        #changing the marker to O
    else:
        buttons[n].config(text = marker, disabledforeground = "red", bg = "light grey", state = "disable")
        curr_marker = " O "             #adding O marker when next time button is clicked
        marker = " X "

    total_added += 1                    #increase the added value everytime the button is added

    replay_btn_state()                  #calling the replay_btn to change state of the button as per the flag

    if total_added >= 5:                #check for win condition only if 5 or more buttons are added
        if win_check(buttons, curr_marker):         #function call to check win. returns true if current marker wins
            flag = 1                                #change the flag to 1
            replay_btn_state()          #change the state of replay buttons as per the flag
            
            for i in range(1, 10):      #disabling all the buttons if any of the player wins
                if buttons[i]['bg'] != "light green":
                    buttons[i].config(state = "disable", bg = "light grey")     #changing the color of all the buttons that are
                    string = "MARKER"+curr_marker+"PLAYER WON!!"                                               #not light green
                    label(string, "green")                      #string to be added as a label and passed color to create label
                                                                                                    #using label function call
        elif total_added == 9:          #if no one wins and all the boxes are added
            flag = 1
            replay_btn_state()
            string = "    MATCH DRAW!!!"    #pass the string and color to the label to print the label
            label(string, "Blue")           #function call to print the label


def replay_btn_state():         #function definition for replay buttons

    if flag == 0:
        replay_buttons[1].config(state = "normal")          #if flag is 0 disable and enable specific replay buttons
        replay_buttons[2].config(state = "disable")

    else:           #for flag any other than 0 i.e., 1 in this case
        replay_buttons[1].config(state = "disable")
        replay_buttons[2].config(state = "normal")



def repl_cmd():                 #fuction definitions if any of the replay buttons are pressed
    global total_added
    total_added = 0
    global marker
    marker = " "+choice("OX")+" "     #randomly select when replay button is pressed
    
    #status_label.destroy()

    label("                        ", "light grey")         #adding big blank label to clear the label 
    
    replay_buttons[1].config(state = "disable")             #disabling replay buttons
    replay_buttons[2].config(state = "disable")

    for i in range(1, 10):              #changing all the marker buttons back to original state
        buttons[i].config(text = "   ", state = "normal", bg = "white")

    
#Button list to add the marker and its properties. Lambda function is used to pass the value to pass arguments. # if no args passed only
#firstbutton is dummy and not used is done so that our button start from 1                #function name is used without any parenthesis
buttons = [ '#',
        Button(window, text = "   ", activebackground = "aqua", height = 2, font = bold_32, bd = 3, bg = "white", command = lambda: btn_cmd(1)),
        Button(window, text = "   ", activebackground = "aqua", height = 2, font = bold_32, bd = 3, bg = "white", command = lambda: btn_cmd(2)),
        Button(window, text = "   ", activebackground = "aqua", height = 2, font = bold_32, bd = 3, bg = "white", command = lambda: btn_cmd(3)),
        Button(window, text = "   ", activebackground = "aqua", height = 2, font = bold_32, bd = 3, bg = "white", command = lambda: btn_cmd(4)),
        Button(window, text = "   ", activebackground = "aqua", height = 2, font = bold_32, bd = 3, bg = "white", command = lambda: btn_cmd(5)),
        Button(window, text = "   ", activebackground = "aqua", height = 2, font = bold_32, bd = 3, bg = "white", command = lambda: btn_cmd(6)),
        Button(window, text = "   ", activebackground = "aqua", height = 2, font = bold_32, bd = 3, bg = "white", command = lambda: btn_cmd(7)),
        Button(window, text = "   ", activebackground = "aqua", height = 2, font = bold_32, bd = 3, bg = "white", command = lambda: btn_cmd(8)),
        Button(window, text = "   ", activebackground = "aqua", height = 2, font = bold_32, bd = 3, bg = "white", command = lambda: btn_cmd(9)) ]
      #current object #emoty text   #when mouse is on the      #additional  #font used as #border width #background     #function call when
                                    #button (button color)     # height     #button text                #color          #button is pressed

#replay button list with its properties
replay_buttons = ['#',
        Button(window, text = "Start Over", activebackground = "aqua", state = "disable", font = bold_12, command = repl_cmd),
        Button(window, text = "Play Again", activebackground = "aqua", state = "disable", font = bold_12, command = repl_cmd) ]


count = 0               #creating button grid for all the buttons in the list
for i in range(0, 3):
    for j in range(0, 3):
        count += 1
        buttons[count].grid(row = i, column = j)        #grid position for buttons is denoted by specific value of row and column


replay_buttons[1].place(x = 20, y = 410)                #place replay buttons in this position
replay_buttons[2].place(x= 190, y = 410)


window.mainloop()                        #this acts like a loop to run the game if not used the game will open and close right away
