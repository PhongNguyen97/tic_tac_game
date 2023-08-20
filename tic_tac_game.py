import random

# test_board = ['#','X','O','X','O','X','O','X','O','X']


def choose_first(marker_1, marker_2):

    player = random.randint(0, 1)

    print(f"=== PLAYER {player + 1} WILL PLAY FIRST ===")

    if player == 0:
        player = marker_1
    else:
        player = marker_2
    return player


def space_check(board, position):
    return board[position] == ' '


def full_check(board):
    for x in range(1, 10):
        if space_check(board, x):
            return False
    # Board is full
    return True


def player_input():
    '''
        OUTPUT = (Player_1 Marker, Player_2 Marker)
    '''

    marker = ''

    # Asking player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    # Assign Player 2, the opposite marker:
    player_1 = marker
    # print('player_1 = marker', player_1, marker)

    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    return (player_1, player_2)


def place_marker(board, marker, position):
    # position = int(input("Choose your marker position: "))
    # print('place_marker', marker)
    board[position] = marker


def display_board(board):
    print('\n'*100)
    print('', board[7], '|', board[8], '|', board[9])
    print('', '-', '|', '-', '|', '-')
    print('', board[4], '|', board[5], '|', board[6])
    print('', '-', '|', '-', '|', '-')
    print('', board[1], '|', board[2], '|', board[3])


def win_check(board, marker):

    # Rows
    for r in range(1, len(board), 3):
        if marker == board[r] == board[r+1] == board[r+2]:
            return True

    # Columns
    for c in range(1, 4):
        if marker == board[c] == board[c+3] == board[c+3+3]:
            return True

    # 2 diagonnals
    if (marker == board[1] == board[5] == board[9]):
        return True

    if (marker == board[3] == board[5] == board[7]):
        return True

    return False


def player_choice(board, marker):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose your marker position: "))
        # print('player_choice', position, marker)
        # board[position] = marker
    return position


def game_on_choice():
    still_play = 'Wrong'
    acceptable_choices = ['Y', 'N', 'y', 'n',
                          'YES', 'NO', 'Yes', 'No', 'yes', 'no']

    while still_play not in acceptable_choices:
        still_play = input("Would you like to play again (Y/N)? ")

        if still_play in acceptable_choices[0::2]:
            return True
        elif still_play in acceptable_choices[1::2]:
            return False
        else:
            print("Please answering with a correct answer (Y/N)!")
            continue

# print(game_on_choice())


def play():
    # while loop to keep playing
    print("Welcome to Tic Tac Toe")
    while True:

        # Play game

        # Reset the game
        board = [' '] * 10
        player_1, player_2 = player_input()
        print('play1', player_1, 'player_2', player_2)

        turn = choose_first(player_1, player_2)
        # print('turn', turn)

        play_game = input("Ready to play? (y or n): ")

        if play_game == 'y':
            game_on = True
        else:
            game_on = False

        # Game play
        while game_on:
            # Player 1 turn
            if turn == 'X':
                # print('Player 1 - game on', turn)

                # Show the board
                display_board(board)

                # Choose position
                position = player_choice(board, turn)

                # Place the marker on the position
                place_marker(board, turn, position)

                # Check if they won
                if win_check(board, turn):
                    display_board(board)
                    print("=== PLAYER 1 HAS WON!!! ===")
                    game_on = False
                else:
                    # Or check if there is a tie
                    if full_check(board):
                        display_board(board)
                        print("=== TIE GAME! ===")
                        game_on = False
                    # No tie and no win? Then next player's turn
                    else:
                        turn = 'O'

            # Player 2 turn
            else:
                # print('Player 2 - game on', turn)
                # Show the board
                display_board(board)

                # Choose position
                position = player_choice(board, turn)

                # Place the marker on the position
                place_marker(board, turn, position)

                # Check if they won
                if win_check(board, turn):
                    display_board(board)
                    print("=== PLAYER 2 HAS WON!!! ===")
                    game_on = False
                else:
                    # Or check if there is a tie
                    if full_check(board):
                        display_board(board)
                        print("=== TIE GAME! ===")
                        game_on = False
                    # No tie and no win? Then next player's turn
                    else:
                        turn = 'X'


        if not game_on_choice():
            break
        else:
            play()


play()
