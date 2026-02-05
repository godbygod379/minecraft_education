# Uloha: 
#

DEBUG = True

A=AIR
W=PALE_OAK_FENCE
B=DARK_OAK_FENCE

BOARD_X=10
BOARD_Y=265
BOARD_Z=10

board = [
        [W,A,W,A,W,A,W,A],
        [A,W,A,W,A,W,A,W],
        [W,A,W,A,W,A,W,A],
        [A,A,A,A,A,A,A,A],
        [A,A,A,A,A,A,A,A],
        [A,B,A,B,A,B,A,B],
        [B,A,B,A,B,A,B,A],
        [A,B,A,B,A,B,A,B]
]

def log(msg):
    if DEBUG == True:
        player.say(msg)

def draw_board(x, y, z):
    log("Drawing board")
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = WHITE_CONCRETE
            else:
                color = BLACK_CONCRETE
            blocks.place(color, world(x+i,y,z+j))

def draw_pieces(x, y, z):
    log("Drawing pieces")

    for i in range(8):
        for j in range(8):
            block = board[i][j]
            log(str(block))
            blocks.place(block, world(x+i,y+1,z+j))

# def move(pos1, pos2):
#     log(str(pos1))
#     log(str(pos2))
#     x1 = pos1 // 10
#     x2 = pos2 % 10
#     y1 = pos1 // 10
#     y2 = pos2 % 10

#     log(str(x1) + str(x2) + str(y1) + str(y2))

#     # ak je na pos1 panacik tak napisem ze tah je nelegaly
#     # a nespravim nic
#     # ak sa vykonal tah, tak sa na pos2 umiestni vzduch
#     # callback z chatu
#     board[x1][y1] = board[x2][y2]
#     board[x1][y1] = A


# player.on_chat("m", move)

draw_board(BOARD_X, BOARD_Y, BOARD_Z)
draw_pieces(BOARD_X, BOARD_Y, BOARD_Z)
