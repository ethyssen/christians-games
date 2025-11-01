# win condition checker
# display the board


board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
playable_pieces = ["x", "o"]


def print_board(board):
    print(" -------")
    for row in board:
        print(f"| {row[0]} {row[1]} {row[2]} |")
    print(" -------")


def get_move() -> str:
    for i in range(1000):
        value = input("What will you play: ")
        if value not in playable_pieces:
            print("use x or o lowercase")
            continue
        return value
    return "you are stupid and shouldn't be playing this. go back to school"


print_board(board)

for i in range(10000000000000):
    row_picked = int(input("What row would you like to set: "))
    col_picked = int(input("What col would you like to set: "))
    value = get_move()
    board[row_picked][col_picked] = value
    print_board(board)
