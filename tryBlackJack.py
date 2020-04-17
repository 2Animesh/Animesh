from random import choice


def card_deck(playercard, playing, c_point):
    deck = {'2 of spade': 2, '3 of spade': 3, '4 of spade': 4, '5 of spade': 5, '6 of spade': 6, '7 of spade': 7,
            '8 of spade': 8, '9 of spade': 9, 'Jack of spade': 10, 'Queen of spade': 10, 'King of spade': 10,
            '2 of clubs': 2, '3 of clubs': 3, '4 of clubs': 4, '5 of clubs': 5, '6 of clubs': 6, '7 of clubs': 7,
            '8 of clubs': 8, '9 of clubs': 9, 'Jack of clubs': 10, 'Queen of clubs': 10, 'King of clubs': 10,
            '2 of heart': 2, '3 of heart': 3, '4 of heart': 4, '5 of heart': 5, '6 of heart': 6, '7 of heart': 7,
            '8 of heart': 8, '9 of heart': 9, 'Jack of heart': 10, 'Queen of heart': 10, 'King of heart': 10,
            '2 of diamond': 2, '3 of diamond': 3, '4 of diamond': 4, '5 of diamond': 5, '6 of diamond': 6,
            '7 of diamond': 7, '8 of diamond': 8, '9 of diamond': 9, 'Jack of diamond': 10, 'Queen of diamond': 10,
            'King of diamond': 10, 'Ace of diamond': [1, 11], 'Ace of spade': [1, 11], 'Ace of clubs': [1, 11],
            'Ace of heart': [1, 11]
            }

    while True:
        rand_card = list(choice(list(deck.items())))
        if rand_card[0] in playercard:
            continue

        else:
            print(rand_card[0])
            if rand_card[0] in ('Ace of diamond', 'Ace of spade', 'Ace of clubs', 'Ace of heart'):
                if playing == 'computer':
                    if (c_point + 11) <= 21:
                        rand_card[0] = 11
                        return rand_card
                    else:
                        rand_card[0] = 1
                        return rand_card
                else:
                    rand_card[1] = int(input("Enter the value of ace (1 or 11) you want to choose: "))

            return rand_card


# It will check game status including bust and return game status

def game_status(pcard_total, playing, ccard_total):
    if playing == 'player':
        if pcard_total < 21:
            return True, True, False
        elif pcard_total == 21:
            print('\nCongratulation! You have won!!\nCollect your $$Money$$')

            return False, False, True

        else:
            print("\n\nBust! \nYou lost the game")
            return False, False, False

    else:
        if ccard_total > 21:
            print("\n\nBust! \nComputer lost the game\nCollect your $$Money$$\n\n")

            return False, True, True

        elif ccard_total == 21 or (21 - ccard_total) < (21 - pcard_total):
            print('\n\nComputer has won!!\n\n')
            return False, True, False

        else:
            return True, False, False



class Player():

    def __init__(self):
        self.point = 0
        self.money = 100
        self.card_track = []

    def card_update(self, hitcard):

        self.point = self.point + hitcard[1]
        self.card_track.append(hitcard[0])

    def bet(self):
        while True:
            chips = int(input("Place your bet: "))
            if (self.money - chips) < 0:
                print('Not Enough Money!!')
                print(f'Your current balance is {self.money}')
            else:
                self.money = self.money - chips
                break
        return chips

    def balance_update(self,bet_amount, win):
        if win:
            self.money = self.money + bet_amount*2

        elif self.money == 0:
            print('Out of money!!')
            exit()

        else:
            self.money = self.money


play = False

while True:
    response = input("Shall we start the game? (y/n): ")
    if response.lower() == 'y':
        play = True
        player = Player()
        computer = Player()
        break

    elif response.lower() == 'n':
        exit()

    else:
        print('Wrong Input')
        continue


while play:
    player.point = 0
    computer.point = 0
    check_another_hand = True
    win_status = False
    print(f"You have {player.money} chips ")
    bet_amount = player.bet()

    print('\n\nYou have ')
    for i in range(2):
        x = card_deck(player.card_track, 'player', computer.point)
        player.card_update(x)

    play, player_game, win_status = game_status(player.point, 'player', computer.point)

    player_game = True
    while player_game == True and player.point < 21:
        response = int(input('\nEnter 1: to hit and \n      2: to stay\n'))
        if response == 1:
            x = card_deck(player.card_track, 'player', computer.point)
            player.card_update(x)

            play, player_game, win_status = game_status(player.point, 'player', computer.point)


        elif response == 2:
            player_game = False
            break

        else:
            print('Wrong Input!!')
            continue

    if play == False:
        while True:
            another_hand = input('Want to play another Hand? (y/n):\n')
            if another_hand.lower() == 'y':
                play = True
                player_game = True
                check_another_hand = False
                player.balance_update(bet_amount, win_status)
                break

            elif another_hand.lower() == 'n':
                exit()

            else:
                print('Wrong Input')
                continue

    if play != False:
        while not player_game:

            while player_game == False and computer.point < 21:
                x = card_deck(computer.card_track, 'computer', computer.point)
                computer.card_update(x)

                play, player_game, win_status = game_status(player.point, 'computer', computer.point)


    while True and check_another_hand:
        another_hand = input('Want 2 play another Hand? (y/n)')
        if another_hand.lower() == 'y':
            play = True
            player_game = True
            player.balance_update(bet_amount,win_status)
            break

        elif another_hand.lower() == 'n':
            exit()

        else:
            print('Wrong Input')
            continue
            


