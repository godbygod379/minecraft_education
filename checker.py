E=AIR
W=WHITE_CONCRETE
B=BLACK_CONCRETE

board = [
        [WHITE_CONCRETE,AIR,W,AIR,W,AIR,W,AIR],
        [AIR,AIR,AIR,AIR,AIR,AIR,AIR,AIR],
        [AIR,AIR,AIR,AIR,AIR,AIR,AIR,AIR],
        [AIR,AIR,AIR,AIR,AIR,AIR,AIR,AIR],
        [AIR,AIR,AIR,AIR,AIR,AIR,AIR,AIR],
        [AIR,AIR,AIR,AIR,AIR,AIR,AIR,AIR],
        [AIR,AIR,AIR,AIR,AIR,AIR,AIR,AIR],
        [AIR,AIR,AIR,AIR,AIR,AIR,AIR,AIR]
    ]

def draw_board(x, y, z):
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = WHITE_CONCRETE
            else:
                color = BLACK_CONCRETE
            blocks.place(color, world(x+i,y,z+j))

def draw_pieces(x, y, z, board):
    player.say("Drawing pieces")

    for i in range(8):
        for j in range(8):
            player.say("hi")
            block = board[i][j]
            player.say(block)
            blocks.place(block, world(x+i,y+1,z+j))
            blocks.place(block, world(x+i,y+2,z+j))

BOARD_X=10
BOARD_Y=280
BOARD_Z=10

# player.say(board[0][0])
# player.say(W)
# draw_board(BOARD_X, BOARD_Y, BOARD_Z)
draw_pieces(BOARD_X, BOARD_Y, BOARD_Z, board)


    # for i in range(8):
    #     for j in range(8):
    #         blocks.place(, world(x, y, z))
