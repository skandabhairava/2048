import random

SIZE = 5
DIGITS_SIZE = 1

#Generating board
if SIZE%2==0: SIZE=SIZE+1 #if size is even, make it an odd num
BOARD = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
BOARD[SIZE//2][SIZE//2] = 1

""" BOARD = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0],
    [2, 0, 0, 0, 0]
] """

def show_board(board):
    print(" "+"_"*((DIGITS_SIZE+1)*SIZE))
    for y in board:
        print("|", end="")
        for x in y:
            if x!=0:
                print(f"{' '*(DIGITS_SIZE-len(str(x)))}{x}", end=" ")
            else: print(f"{' '*(DIGITS_SIZE)}", end=" ")
            #print(x, end=" ")
        print("|")
    print(" "+"‾"*((DIGITS_SIZE+1)*SIZE))
    print()

def gen_new_num(board):

    spaces = len(board)*SIZE
    free_spaces = spaces

    while free_spaces:
        free_spaces = 0
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 0 and random.randint(0, 49) == 0:
                    board[y][x] = 2
                    return
                if board[y][x] == 0:
                    free_spaces += 1

    return False

def move_up(board):
    global DIGITS_SIZE
    for x in range(SIZE):
        for y in range(len(board)):
            set_data, set_j, find = None, [], []
            for j in range(y+1, len(board)):
                if board[j][x] != 0 and set_data is None:
                    set_data = board[j][x]
                    set_j.append(j)
                    find.append(board[j][x])
                elif board[j][x] == set_data:
                    set_j.append(j)
                    find.append(board[j][x])
                elif board[j][x] != 0:
                    break

            if set_data is not None:
                if set_data == board[y][x]:
                    board[y][x] += sum(find)
                    for dy in set_j: board[dy][x] = 0
                elif board[y][x] == 0:
                    board[y][x] = sum(find)
                    for dy in set_j: board[dy][x] = 0

                if len(str(board[y][x])) > DIGITS_SIZE: DIGITS_SIZE = len(str(board[y][x]))
                if board[y][x] == 2048: return True

    if gen_new_num(board) is False: return False

def move_down(board):
    global DIGITS_SIZE
    for x in range(SIZE):
        for y in range(len(board)-1, -1, -1):
            set_data, set_j, find = None, [], []
            for j in range(y-1, -1, -1):
                if board[j][x] != 0 and set_data is None:
                    set_data = board[j][x]
                    set_j.append(j)
                    find.append(board[j][x])
                elif board[j][x] == set_data:
                    set_j.append(j)
                    find.append(board[j][x])
                elif board[j][x] != 0:
                    break

            if set_data is not None:
                if set_data == board[y][x]:
                    board[y][x] += sum(find)
                    for dy in set_j: board[dy][x] = 0
                elif board[y][x] == 0:
                    board[y][x] += sum(find)
                    for dy in set_j: board[dy][x] = 0

                if len(str(board[y][x])) > DIGITS_SIZE: DIGITS_SIZE = len(str(board[y][x]))
                if board[y][x] == 2048: return True

    if gen_new_num(board) is False: return False

def move_right(board):
    global DIGITS_SIZE
    for y in range(len(board)):
        for x in range(SIZE-1, -1, -1):
            set_data, set_i, find = None, [], []
            for i in range(x-1, -1, -1):
                if board[y][i] != 0 and set_data is None:
                    set_data = board[y][i]
                    set_i.append(i)
                    find.append(board[y][i])
                elif board[y][i] == set_data:
                    set_i.append(i)
                    find.append(board[y][i])
                elif board[y][i] != 0:
                    break

            if set_data is not None:
                if set_data == board[y][x]:
                    board[y][x] += sum(find)
                    for dx in set_i: board[y][dx] = 0
                elif board[y][x] == 0:
                    board[y][x] += sum(find)
                    for dx in set_i: board[y][dx] = 0

                if len(str(board[y][x])) > DIGITS_SIZE: DIGITS_SIZE = len(str(board[y][x]))
                if board[y][x] == 2048: return True

    if gen_new_num(board) is False: return False

def move_left(board):
    global DIGITS_SIZE
    for y in range(len(board)):
        for x in range(SIZE):
            set_data, set_i, find = None, [], []
            for i in range(x+1, SIZE):
                if board[y][i] != 0 and set_data is None:
                    set_data = board[y][i]
                    set_i.append(i)
                    find.append(board[y][i])
                elif board[y][i] == set_data:
                    set_i.append(i)
                    find.append(board[y][i])
                elif board[y][i] != 0:
                    break

            if set_data is not None:
                if set_data == board[y][x]:
                    board[y][x] += sum(find)
                    for dx in set_i: board[y][dx] = 0
                elif board[y][x] == 0:
                    board[y][x] += sum(find)
                    for dx in set_i: board[y][dx] = 0

                if len(str(board[y][x])) > DIGITS_SIZE: DIGITS_SIZE = len(str(board[y][x]))
                if board[y][x] == 2048: return True

    if gen_new_num(board) is False: return False

while True:
    print("\n"*30)
    show_board(BOARD)
    move = input("WASD: ").upper()
    if move == "" or move[0] not in "WASD":
        print("That option doesn't exist, please try again.\n\n")
        continue

    if move == "W":
        action = move_up(BOARD)
        if action is False:
            print("\n"*40)
            show_board(BOARD)
            print("GAME OVER")
            break
        elif action is True:
            print("\n"*40)
            show_board(BOARD)
            print("YOU WON THE GAME")
            break
    elif move == "S":
        action = move_down(BOARD)
        if action is False:
            print("\n"*40)
            show_board(BOARD)
            print("GAME OVER")
            break
        elif action is True:
            print("\n"*40)
            show_board(BOARD)
            print("YOU WON THE GAME")
            break
    elif move == "D":
        action = move_right(BOARD)
        if action is False:
            print("\n"*40)
            show_board(BOARD)
            print("GAME OVER")
            break
        elif action is True:
            print("\n"*40)
            show_board(BOARD)
            print("YOU WON THE GAME")
            break
    elif move == "A":
        action = move_left(BOARD)
        if action is False:
            print("\n"*40)
            show_board(BOARD)
            print("GAME OVER")
            break
        elif action is True:
            print("\n"*40)
            show_board(BOARD)
            print("YOU WON THE GAME")
            break