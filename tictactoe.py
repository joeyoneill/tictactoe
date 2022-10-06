# Joseph O'Neill
# 10.6.22
# Program for a tic tac toe game.

# Initialize Vars
game_count = 0

# Introductary Message
print("""
▄▄▌ ▐ ▄▌▄▄▄ .▄▄▌   ▄▄·       • ▌ ▄ ·. ▄▄▄ .    ▄▄▄▄▄
██· █▌▐█▀▄.▀·██•  ▐█ ▌▪▪     ·██ ▐███▪▀▄.▀·    •██  ▪
██▪▐█▐▐▌▐▀▀▪▄██▪  ██ ▄▄ ▄█▀▄ ▐█ ▌▐▌▐█·▐▀▀▪▄     ▐█.▪ ▄█▀▄
▐█▌██▐█▌▐█▄▄▌▐█▌▐▌▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌     ▐█▌·▐█▌.▐▌
 ▀▀▀▀ ▀▪ ▀▀▀ .▀▀▀ ·▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀      ▀▀▀  ▀█▄▀▪
             ▐▄▄▄      ▄▄▄ . ▄· ▄▌.▄▄ ·
              ·██▪     ▀▄.▀·▐█▪██▌▐█ ▀.
            ▪▄ ██ ▄█▀▄ ▐▀▀▪▄▐█▌▐█▪▄▀▀▀█▄
            ▐▌▐█▌▐█▌.▐▌▐█▄▄▌ ▐█▀·.▐█▄▪▐█
             ▀▀▀• ▀█▄▀▪ ▀▀▀   ▀ •  ▀▀▀▀
        ▄▄▄▄▄▪   ▄▄· ▄▄▄▄▄ ▄▄▄·  ▄▄· ▄▄▄▄▄      ▄▄▄ .
        •██  ██ ▐█ ▌▪•██  ▐█ ▀█ ▐█ ▌▪•██  ▪     ▀▄.▀·
         ▐█.▪▐█·██ ▄▄ ▐█.▪▄█▀▀█ ██ ▄▄ ▐█.▪ ▄█▀▄ ▐▀▀▪▄
         ▐█▌·▐█▌▐███▌ ▐█▌·▐█ ▪▐▌▐███▌ ▐█▌·▐█▌.▐▌▐█▄▄▌
         ▀▀▀ ▀▀▀·▀▀▀  ▀▀▀  ▀  ▀ ·▀▀▀  ▀▀▀  ▀█▄▀▪ ▀▀▀
             ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .
            ▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·
            ▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄
            ▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌
            ·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀
\n""")

# Display function
def display_board(line1, line2, line3):

    line1_str = " " + line1[0] + " | " + line1[1] + " | " + line1[2] + " "
    line2_str = " " + line2[0] + " | " + line2[1] + " | " + line2[2] + " "
    line3_str = " " + line3[0] + " | " + line3[1] + " | " + line3[2] + " "

    divider = "___________"

    print("")
    print(line1_str)
    print(divider)
    print(line2_str)
    print(divider)
    print(line3_str)
    print("")

# returns which player won
# used in def win_check(args)
def ret_player(val):
    if val == 'x':
        return "1"
    else:
        return "2"

# checks if someone won the game
# returns a list:
# iter 0: True/False if a player won or not
# iter 2: Which player won
def win_check(selected):

    ret = [False, -1]

    if selected[0] == selected[1] and selected[1] == selected[2] and selected[0] != False:
        ret[0] = True
        ret[1] = ret_player(selected[0])
    elif selected[3] == selected[4] and selected[4] == selected[5] and selected[3] != False:
        ret[0] = True
        ret[1] = ret_player(selected[3])
    elif selected[6] == selected[7] and selected[7] == selected[8] and selected[6] != False:
        ret[0] = True
        ret[1] = ret_player(selected[6])
    elif selected[0] == selected[3] and selected[3] == selected[6] and selected[0] != False:
        ret[0] = True
        ret[1] = ret_player(selected[0])
    elif selected[1] == selected[4] and selected[4] == selected[7] and selected[1] != False:
        ret[0] = True
        ret[1] = ret_player(selected[1])
    elif selected[2] == selected[5] and selected[5] == selected[8] and selected[2] != False:
        ret[0] = True
        ret[1] = ret_player(selected[2])
    elif selected[0] == selected[4] and selected[4] == selected[8] and selected[0] != False:
        ret[0] = True
        ret[1] = ret_player(selected[0])
    elif selected[2] == selected[4] and selected[4] == selected[6] and selected[2] != False:
        ret[0] = True
        ret[1] = ret_player(selected[2])

    return ret


# Game function
def game():

    # display
    line1 = ["_", "_", "_"]
    line2 = ["_", "_", "_"]
    line3 = ["_", "_", "_"]

    # Keeps track of which have been used
    selected = [False, False, False, False, False, False, False, False, False]

    player = 0

    while True:

        # SELECTION LOOP
        while True:

            if player == 0:
                print("\nIt is player 1's turn (x)!")
            else:
                print("\nIt is player 2's turn (o)!")

            selection = int(input("Enter a number 0-8:\n"))
            if selected[selection] != False:
                print("That one has already been selected! Try again.")
                continue
            else:
                print("\nGood choice!")
                if player == 0:
                    selected[selection] = 'x'
                    symbol = 'x'
                else:
                    selected[selection] = 'o'
                    symbol = 'o'
                break

        # changes display strings
        if selection == 0:
            line1[0] = symbol
        elif selection == 1:
            line1[1] = symbol
        elif selection == 2:
            line1[2] = symbol
        elif selection == 3:
            line2[0] = symbol
        elif selection == 4:
            line2[1] = symbol
        elif selection == 5:
            line2[2] = symbol
        elif selection == 6:
            line3[0] = symbol
        elif selection == 7:
            line3[1] = symbol
        elif selection == 8:
            line3[2] = symbol

        # displays the updated board
        display_board(line1, line2, line3)

        # checks if somebody won the game
        won = win_check(selected)
        if won[0] == True:
            print("""\n########################
#   Congratulations!   #
########################""")
            print("#   Player ", won[1], " wins!   #")
            print("########################\n\n")
            break

        # checks for a draw
        draw = False
        if False not in selected:
            draw = True

        if draw == True:
            print("\nOh no! Looks like it is a draw!")
            print("Better luck next time!\n\n")
            break

        # switch players
        if player == 0:
            player = 1
        else:
            player = 0

# MAIN GAME Loop
while True:

    # Loop to decide to play or exit
    while True:
        if game_count == 0:
            begin = input("Would you like to begin? (y/n)\n").lower()
        else:
            begin = input("Would you like to play again? (y/n)\n").lower()

        if begin == 'y':
            break
        elif begin == 'n':
            print("\nYou played:", game_count, "times!")
            print("Come play again some time!\n")
            exit()
        else:
            print("Please enter 'y' to play or 'n' to exit!")
            continue

    # Game function
    game()

    # Increment game count
    game_count += 1
