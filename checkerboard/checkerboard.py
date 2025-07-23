#!/usr/bin/python

def covercheckerboard(board, lab=1, top=0, left=0, side=None):
    if side is None: side=len(board)

    # Side length of board
    s= side//2

    # Offset outer/inner offsets
    offsets = (0, -1), (side-1, 0)

    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            # if outer corner is not set ...
            if not board[top+dy_outer][left+dx_outer]:
                # ... label inner corner:
                board[top+s+dy_inner][left+s+dx_inner] = lab
    # Next label
    lab += 1
    if s>1:
        for dy in [0,s]:
            for dx in [0,s]:
                # Recursive calls, if s is atleast 2
                lab = covercheckerboard(board, lab, top+dy, left+dx, s)
    # Return the next available label:
    return lab

# Main problem

board = [[0]*8 for i in range(8)]
board[7][7] = -1
print(covercheckerboard(board))

# print labels
for row in board:
    print((" %2i"*8) % tuple(row))
