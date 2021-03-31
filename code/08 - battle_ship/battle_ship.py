"""
x Create some kind of collection to keep track of a game board for battleship (10 x 10 squares).
x Write a function that draws your game board. You can see a tic tac toe version here, but your map could look anyway you want.
x Add means of keeping tracks of a few boats of different size (grey areas in pictures). This could (but doesn’t have to) mean a key for each square.
x Add functions for adding boats to your game board.
x Change your draw function to indicate if a boat is placed in the square, perhaps by writing a ”B”?
Create a shoot function that takes two parameters and sets a value in the corresponding square in your game board collection. For instance shoot(”D”, 7) to indicate a shot here.
Change the draw function to print out shots, for instance with X.
Keep track of misses on the board.
Draw misses by printing out, for instance, ”M”.
"""
board = {
    " ": "1234567890",
    "A": "----------",
    "B": "----------",
    "C": "----------",
    "D": "----------",
    "E": "----------",
    "F": "----------",
    "G": "----------",
    "H": "----------",
    "I": "----------",
    "J": "----------"
}

boats = [
    {
        "name": "boat1",
        "squares": [
            "A1", "A2", "A3"
        ],
        "status": "sunk"
    }
]

board_alt = {
    "A": {
        "name": "A1",
        "value": "-",
        "shot": false
    },
    "B": "----------",
    "C": "----------",
    "D": "----------",
    "E": "----------",
    "F": "----------",
    "G": "----------",
    "H": "----------",
    "I": "----------",
    "J": "----------"
}


def draw_board():
    for row, col in board.items():
        print(row, col)


def add_boat(goal):
    old_row = list(board[goal[0]])
    old_row[int(goal[1]) - 1] = "B"
    board[goal[0]] = "".join(old_row)


def shoot(goal):
    old_row = list(board[goal[0]])
    if old_row[int(goal[1]) - 1] == "B":
        print("Hit!")
    else:
        print("Miss!")

    old_row[int(goal[1]) - 1] = "X"
    board[goal[0]] = "".join(old_row)


add_boat(input("Var vill du sätta båten? (t ex A5) "))
shoot(input("Var vill du skjuta? (t ex A5) "))

draw_board()
