

def printer(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + "  ")
    print("   |   |   ")
    print("_ "*6)
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + "  ")
    print("   |   |   ")
    print("_ "*6)
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + "  ")
    print("   |   |   ")


def symbol_choice():
    player1_symbol = ' '
    while not(player1_symbol.upper()=='O' or player1_symbol.upper()=='X'):
        player1_symbol = input("Player 1: Choose 'X' or 'O' ").upper()
    if player1_symbol == 'X':
        player2_symbol = 'O'
    else:
        player2_symbol = 'X'

    return (player1_symbol, player2_symbol)


def input_check(pos):

    check = False
    while not check:
        x = int(input("Enter position: (1-9) \n"))
        if x not in range(1, 10):
            print('Wrong Input!! \n\n')
            check = False
        elif x in pos:
            print("Duplicate Input!! \n\n")
            check = False
        else:
            check = True
    return x




def continue_game(pos1,pos2):
    d = {1:[1,2,3], 2:[4,5,6], 3:[7,8,9], 4:[1,4,7], 5:[2,5,8], 6:[3,6,9], 7:[1,5,9], 8:[3,5,7]}
    check = False
    for i in d.values():
        if (set(pos1) >= set(i)) or (set(pos2) >= set(i)):
            check = True
    return check




c=0
board = [" "]
pos1=[]
pos2=[]
start = input("Shall we start? Y or N  ")
if start.lower() == 'y':
    play = True

    p1_choice, p2_choice=symbol_choice()

    board = [" "]*10
    printer(board)

    while play:
        if c%2==0:
            x = input_check(pos1+pos2)
            pos1.append(x)
            board[x] = p1_choice
            printer(board)
        else:
            x = input_check(pos1 + pos2)
            pos2.append(x)
            board[x] = p2_choice
            printer(board)
        c+=1

        if continue_game(pos1,pos2):
            if c%2==0:
                print("Player 2 won the game!!")
            else:
                print("Player 1 won the game")
            play = False

        if c>8 :
            print("It's a tie")
            play = False

elif start.lower()!='n':
    print("Wrong Input")

else:
    exit()




