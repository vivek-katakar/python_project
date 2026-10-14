
# Program for Tic Tac Toe

board = ["0", "1", "2",
         "3", "4", "5",
         "6", "7", "8"]

players = {
    'x': 'player_1',
    'o': 'player_2'
}

winning_combination = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

occupied = set()


def display_board():
    print()
    print("-----------------")
    print(board[0], "|", board[1], "|", board[2])
    print("-----------------")
    print(board[3], "|", board[4], "|", board[5])
    print("-----------------")
    print(board[6], "|", board[7], "|", board[8])
    print("-----------------")


def check_winner(symbol):
    for combination in winning_combination:
        if all(board[i] == symbol for i in combination):
            return True
    return False


def make_move(symbol):
    while True:
        try:
            choice = int(input(
                f"{players[symbol]} choose position (0-8): "
            ))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice < 0 or choice > 8:
            print("Enter a number between 0 and 8.")
            continue

        if choice in occupied:
            print("This position is already occupied.")
            continue

        board[choice] = symbol
        occupied.add(choice)
        break


print("Welcome to Tic Tac Toe!")

current_player = 'x'

while True:
    display_board()
    make_move(current_player)

    if check_winner(current_player):
        display_board()
        print(players[current_player], "wins!")
        break

    if len(occupied) == 9:
        display_board()
        print("It's a draw!")
        break

    if current_player == 'x':
        current_player = 'o'
    else:
        current_player = 'x'

print("Thanks for playing!")
