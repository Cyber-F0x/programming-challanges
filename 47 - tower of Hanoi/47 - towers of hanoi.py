class Disk:
    def __init__(self, size):
        self.size = size


def print_board(board):
    for row in board:
        print row


def init_board():
    rows, cols = (3, 3)
    board = [[0 for i in range(cols)] for j in range(rows)]
    big = Disk(3)
    medium = Disk(2)
    small = Disk(1)
    board[0][0] = small.size
    board[1][0] = medium.size
    board[2][0] = big.size
    return board


def get_input():
    string = raw_input("Move:")
    commands = {
        "left": 0,
        "center": 1,
        "right": 2
    }

    ans = string.split(" ")
    if len(ans) is not 2:
        print "source, dest"
        return
    if ans[0] not in commands:
        print "Invalid command"
        return
    elif ans[1] not in commands:
        print "Invalid command"
        return
    elif (ans[1] == ans[0]):
        print "Cant move to same col"
        return
    else:
        sor = commands[ans[0]]
        des = commands[ans[1]]
        return sor, des


def move(vals, board):
    source, dest = vals
    source_val = 0
    source_coord = 0
    row_one = board[0]
    row_two = board[1]
    row_tre = board[2]
    if row_one[source] != 0:
        source_val = board[0][source]
        source_coord = (source, 0)
    elif row_two[source] != 0:
        source_val = board[1][source]
        source_coord = (source, 1)
    elif row_tre[source] != 0:
        source_val = board[2][source]
        source_coord = (source, 2)
    # now do the thing in reverse
    y, x = source_coord
    if row_tre[dest] == 0:
        board[2][dest] = source_val
        board[x][y] = 0
    elif row_two[dest] == 0:
        if board[2][dest] > source_val:

            board[1][dest] = source_val
            board[x][y] = 0
        else:
            board[x][y] = source_val
            print "Nope"
    elif row_one[dest] == 0:
        if board[1][dest] > source_val:
            board[0][dest] = source_val
            board[x][y] = 0
        else:
            board[x][y] = source_val
            print "Nope"
    print_board(board)


def main():
    board = init_board()
    print "Game starting"
    print "move source_col, dest col"
    print_board(board)
    while 1:
        vals = get_input()
        if vals is not None:
            move(vals, board)


if __name__ == '__main__':
    main()
