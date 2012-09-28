#Any live cell with fewer than two live neighbours dies, as if caused by under-population.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overcrowding.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
from time import sleep

def live_cell(x, y, board):
    if board[x][y] == "1":
        cell = "alive"
    else:
        cell = "dead"
    cellcount = 0
    if board[x-1][y-1] == "1": cellcount += 1
    if board[x-1][y] == "1": cellcount += 1
    try:
        if board[x-1][y+1] == "1": cellcount += 1
    except: pass
    try:
        if board[x][y+1] == "1": cellcount += 1
    except: pass
    if board[x][y-1] == "1": cellcount += 1
    try:
        if board[x+1][y-1] == "1": cellcount += 1
    except: pass
    try:
        if board[x+1][y] == "1": cellcount += 1
    except: pass
    try:
        if board[x+1][y+1] == "1": cellcount += 1
    except: pass
    if cell == "alive":
        if cellcount == 2 or cellcount == 3:
            return True
        else:
            return False
    if cell == "dead":
        if cellcount == 3:
            return True
        else:
            return False

def conway(patter):
    pattern = patter.split()
    newpattern = list(pattern)
    line = 0
    cell = 0
    while True:
        while True:
            if live_cell(line, cell, pattern):
                newpatternline = list(newpattern[line])
                newpatternline[cell] = "1"
                newpattern[line] = "".join(newpatternline)
            else:
                newpatternline = list(newpattern[line])
                newpatternline[cell] = "0"
                newpattern[line] = "".join(newpatternline)
            if cell >= len(pattern[0])-1:
                break
            cell += 1
        if line >= len(pattern)-1:
            break
        line += 1
        cell = 0
    newpattern = "\n".join(newpattern)
    return newpattern

def main():
    patter = open("patter.txt", "rb").read()
    while True:
        new = conway(patter)
        print new
        print "\n\n"
        sleep(1)
        patter = new


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
