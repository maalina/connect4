'''Let's play connect four!!!'''
#cool things:
#board size constraints could be fixed
#more dummy prevention/goof counters
#the 3 win functions looked less stupid
#pause after #cool1 by like a second
#colourful circly things
#oops/undo button?
#if name == main block: how to do user input though...


import random
from sys import exit #how do i properly exit this thing....

def set_up():
        input_1 = input("What is your name?\n")
        input_2 = input("What is your name?\n")
        print("Let's see who goes first! One moment please...\n") #cool1
        if random.randint(1,2) == 1:
                print(input_1, 'goes first. Your pieces are the "X"\'s.', input_2, 'goes second. Your pieces are the "Y"\'s.\n')
        else:
                print (input_2, 'goes first. Your pieces are the "Y"\'s.', input_1, 'goes second. Your pieces are the "X"\'s.\n')
        return input_1, input_2

def play_game():
        names = set_up()
        global name_1 #how else can i deal with names throughout...?
        name_1 = names[0]
        global name_2 
        name_2 = names[1]
        pieces = board_pieces()
        make_board(pieces)
        count = 0
        while count < 3:
                player1(pieces)
                print_board(pieces)
                player2(pieces)
                print_board(pieces)
                count += 1
        while wins(pieces) == False:
                player1(pieces)
                print_board(pieces)
                wins(pieces)
                player2(pieces)
                print_board(pieces)
                wins(pieces)
                
def player1(pieces):
        print(name_1 + "'s turn.")
        position("X", pieces)
        
def player2(pieces):
        print(name_2 + "'s turn.")
        position("Y", pieces)

#you get the actual board
def print_board(pieces):
        for i in range(5):
                print (pieces[i][0] + "  | " + pieces[i][1] + " | " + pieces[i][2] + " | " + pieces[i][3] + " | " + pieces[i][4])
                print ("--- --- --- --- ---")
                
def position(sym, pieces):
        goof_count = 0       
        col = int(input("Pick a column to drop your piece.\n"))
        while (col < 0) or (col > 4):
                print("You goofed. Try again")
                goof_count += 1
                col = int(input("Pick a column to drop your piece.\n"))
                if goof_count == 3:
                        print("Please, let's stick to the game...")
                if goof_count > 5:
                        print("Let's stop this now, shall we?\n")
                        exit(0) #exit quietly without that Tracebook, etc????
        i = 4
        while i >= 0:
                if pieces[i][col] == " ":
                        pieces[i][col] = sym
                        return pieces
                else:
                        i -= 1
        if i < 0:
                print ("No space in this column. Please pick another column.")
        #how to get them to try again???

#building the list of list piece placements
def board_pieces():
        pieces = []
        for i in range(0,5):
                pieces.append([" "] * 5)
        return pieces

#make the board
def make_board(pieces):
        for i in range(5):
                print (pieces[i][0] + "  | " + pieces[i][1] + " | " + pieces[i][2] + " | " + pieces[i][3] + " | " + pieces[i][4])
                print ("--- --- --- --- ---")

        #jokes, not actually needed anymore, maybe for a diff game        
        '''print("These are the board indices.")
        for j in range(5):
                for k in range(5):
                        print (j,k,end="    ")
                print ("\n")
'''

#has someone won yet?
def wins(pieces):
        vert_wins(pieces)
        hori_wins(pieces)
        diag_wins(pieces)
        if (vert_wins(pieces) == False) and (hori_wins(pieces) == False) and (diag_wins(pieces) == False):
                return False
        
#3 ways to win
def vert_wins(pieces):
        for j in range(0,5):
                if (pieces[0][j] == pieces[1][j] == pieces[2][j] == pieces[3][j]) or (pieces[1][j] == pieces[2][j] == pieces[3][j] == pieces[4][j]):
                        if pieces[2][j] == "X" and pieces[2][j] != " ":
                                print(name_1, "won.")
                                play_again() #call the play again function
                        elif pieces[2][j] == "Y" and pieces[2][j] != " ":
                                print (name_2, "won.")
                                play_again()
        return False

def hori_wins(pieces):
        for j in range(0,5):
                if (pieces[j][0] == pieces[j][1] == pieces[j][2] == pieces[j][3]) or (pieces[j][1] == pieces[j][2] == pieces[j][3] == pieces[j][4]):
                        if pieces[j][3] == "X" and pieces[j][3] != " ":
                                print("Player 1 won.")
                                play_again()
                        elif pieces[j][3] == "Y" and pieces[j][3] != " ":
                                print("Player 2 won.")
                                play_again()
        return False

def diag_wins(pieces):
        #winning lines from top left to bottom right
        for i in range(0,2):
                for j in range(0,2):
                        if pieces[i][j] == pieces[i + 1][j + 1] == pieces[i+2][j+2] == pieces[i+3][j+3]:
                                if pieces[i][j] == "X":
                                        print(name_1, "won.")
                                        play_again()
                                elif pieces[i][j] == "Y":
                                        print(name_2, "won.")
                                        play_again()
        #winning lines from top right to bottom left
        for m in range(0,2):
                for n in range(3,5):
                        if pieces[m][n] == pieces[m+1][n-1] == pieces[m+2][n-2] == pieces[m+3][n-3]:
                                if pieces[m][n] == "X":
                                        print(name_1, "won.")
                                        play_again()
                                elif pieces[m][n] == "Y":
                                        print(name_2, "won.")
                                        play_again()
        return False
                                
#play again?
def play_again():
        val = input("Do you wish to play again?\n")
        goof_count = 0        
        if val == "yes":
                play_game()
        elif val == "no":
                print ("Bye!\n")
                sys.exit() #not sure how to actually exit
        
        #not entirely sure how to do a recurring loop thing
        '''        
        else:
                while goof_count < 5:
                        print ("Please enter either 'yes' or 'no'.\n")
                        val = input("Do you wish to play again?\n")
                        goof_count += 1
        '''
