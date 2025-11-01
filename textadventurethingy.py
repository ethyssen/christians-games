# # win condition checker
# # display the board


# board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
# playable_pieces = ["x", "o"]


# def print_board(board):
#     print(" -------")
#     for row in board:
#         print(f"| {row[0]} {row[1]} {row[2]} |")
#     print(" -------")


# def get_move() -> str:
#     for i in range(1000):
#         value = input("What will you play: ")
#         if value not in playable_pieces:
#             print("use x or o lowercase")
#             continue
#         return value
#     return "you are stupid and shouldn't be playing this. go back to school"


# print_board(board)

# for i in range(10000000000000):
#     row_picked = int(input("What row would you like to set: "))
#     col_picked = int(input("What col would you like to set: "))
#     value = get_move()
#     board[row_picked][col_picked] = value
#     print_board(board)

import time

for i in range(50 - 15):
    print(
        "You are standing knee deep in muck at the gate. A slit in the gate opens and the guard asks you a question."
    )
    orb_count = int(input("How many orbs did you collect this year: "))

    # handle too many orbs
    if orb_count >= 50:
        time.sleep(3)
        print("You are lying. You return to the mines for another year.")
        time.sleep(1)
        continue

    # handle too few orbs
    if orb_count < 20:
        time.sleep(2)
        print("Insufficient. You return to the mines for another year.")
        time.sleep(1)
        continue

    # orbs are sufficient
    time.sleep(1)
    print("The gate opens.")
    time.sleep(1)
    break

print("you dance and frolic in your joy")
